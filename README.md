Conversation Evaluation Script

This assignment contains a small evaluation pipeline that scores an AI’s response based on relevance, completeness, and hallucination.
It also measures latency and gives a rough cost estimate.

How to run it

Clone the repository:

git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>


Install the required package:

pip install json5


Run the script:

python evaluate.py


After running, you will get an evaluation_output.json file that contains all the scores.

What the Script Does

Loads the sample conversation JSON.

Finds the last user query and the last model response.

Loads context chunks from the vector JSON.

Runs three evaluation checks:

Relevance – checks if the response matches the main parts of the query.

Completeness – checks if the answer covers enough information.

Hallucination – checks if the response is supported by the given context.

Measures runtime.

Estimates a rough cost based on word count.

Saves everything into a JSON result file.

All evaluations are done using simple string-based logic.

Why I Built It This Way

I kept the solution lightweight because it's easy to understand and doesn’t require complex setup.
Everything runs locally, and there are:

no embeddings,

no external API calls,

no large models involved.

This makes the script easy to maintain, test, and modify.

How This Scales

The script uses basic Python string operations, which run very quickly.
There is no heavy computation involved, and each conversation is evaluated independently.
Because of this, the approach can scale to large volumes (even millions of evaluations) while keeping latency and cost low.

Files Included

evaluate.py — main evaluation script

sample-chat-conversation-02.json — conversation input

sample_context_vectors-01.json — context chunks

evaluation_output.json — output file created by the script

README.md — project documentation
