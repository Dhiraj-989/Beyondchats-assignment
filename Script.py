import json5
import json
import time
import re
import difflib

# function to load json file
def load_json(path):
    with open(path, "r") as f:
        data = json5.load(f)
    return data


# load conversation file
chat = load_json("sample-chat-conversation-02.json")

# load retrieved vector context
context = load_json("sample_context_vectors-01.json")


# GET USER QUERY 
conversation = chat.get("conversation_turns", [])
user_query = ""

# loop from the end to find last user message
for item in reversed(conversation):
    if item.get("role") == "User":
        user_query = item.get("message", "")
        break



# GET MODEL RESPONSE 
model_response = ""

#loop from end to find last model response
for item in reversed(conversation):
    if item.get("role") == "AI/Chatbot":
        model_response = item.get("message", "")
        break



#EXTRACT CONTEXT CHUNKS
vector_list = context.get("data", {}).get("vector_data", [])
retrieved_chunks = []

# get the text from each vector entry
for v in vector_list:
    chunk = v.get("text", "")
    if chunk:
        retrieved_chunks.append(chunk)



#RELEVANCE CHECK
def check_relevance(query, response):
    # remove punctuation & special characters
    q = re.sub(r"[^a-zA-Z0-9\s]", " ", query.lower())
    r = response.lower()

    # stop words to ignore because they appear mostly in any sentence
    stop = {
        "the","and","that","this","with","from","have","will","just","about",
        "your","been","into","than","then","them","they","what","when","where",
        "which","also","there","here","were","some","more","want","know","happy",
        "open","like","need","get","have"
    }

    # remoce small/stop words
    q_words = [w for w in q.split() if len(w) > 3 and w not in stop]

    if not q_words:
        return 0.0

    # count matches using exact or similar words
    matches = sum(
        1 for w in q_words
        if w in r or difflib.get_close_matches(w, r.split(), cutoff=0.6)
    )

    return round(matches / len(q_words), 2)



# COMPLETENESS CHECK
def check_completeness(query, response):
    # reuse relevance score
    rel = check_relevance(query, response)

    # check coverage of query keywords
    q_words = [w for w in query.lower().split() if len(w) > 3]
    coverage = sum(1 for w in q_words if w in response.lower())

    if q_words:
        coverage_score = coverage / len(q_words)
    else:
        coverage_score = 0

    # longer answers considered more complete
    length_score = 1.0 if len(response.split()) > 40 else 0.5

    final = (rel + coverage_score + length_score) / 3
    return round(final, 2)



# -------------------- HALLUCINATION CHECK --------------------
def check_hallucination(response, chunks):
    # break response into sentences using "."
    resp_sentences = response.lower().split(".")
    hallucinated = 0

    # go through each sentence
    for sent in resp_sentences:
        sent = sent.strip()
        if not sent:
            continue  # skip empty pieces

        found = False

        # compare sentence with each chunk
        for ch in chunks:
            chunk_lower = ch.lower()

            # check if first 15 characters appear in chunk
            if sent[:15] in chunk_lower:
                found = True
                break

            # check if any word from sentence appears in chunk
            if any(word in chunk_lower for word in sent.split()):
                found = True
                break

        # if sentence didn't match any chunk then its hallucinated
        if not found:
            hallucinated += 1

    # count how many sentences are actually present
    total = len([s for s in resp_sentences if s.strip()])

    if total == 0:
        return 1.0  # no real sentences then consider fully hallucinated

    score = hallucinated / total
    return round(score, 2)



# LATENCY MEASUREMENT
start = time.time()

rel = check_relevance(user_query, model_response)
comp = check_completeness(user_query, model_response)
hall = check_hallucination(model_response, retrieved_chunks)

end = time.time()

latency_ms = round((end - start) * 1000, 2)



# COST ESTIMATION
def estimate_cost(query, response):
    # count total words in query and response
    total_words = len(query.split()) + len(response.split())
    
    # assume 1 word ≈ 1 token (approx.)
    estimated_cost = total_words * 0.0001   # example rate for testing

    return round(estimated_cost, 6)



# final output
result = {
    "user_query": user_query,
    "model_response": model_response,
    "relevance_score": rel,
    "completeness_score": comp,
    "hallucination_score": hall,
    "latency_ms": latency_ms,
    "estimated_cost": estimate_cost(user_query, model_response)
}

print(result)


# write result to json file
with open("evaluation_output.json", "w") as f:
    json.dump(result, f, indent=2)
