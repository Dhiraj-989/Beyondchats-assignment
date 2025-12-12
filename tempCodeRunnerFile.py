# def check_hallucination(response, chunks):
    resp_sentences = response.lower().split(".")
    hallucinated = 0

    for sent in resp_sentences:
        sent = sent.strip()
        if not sent:
            continue

        found = False
        for ch in chunks:
            # check first 15 letters of the sentence or any word in the sentence appears in the chunk 
            if chunks[:15] in ch.lower() or any(word in ch.lower() for word in sent.split()):
                found = True
                break

            if not found:
                hallucinated += 1

        total = 
