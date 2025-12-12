README
Conversation Evaluation Script

This assignment contains a small evaluation pipeline that scores an AI’s response based on relevance, completeness, and hallucination. It also measures latency and gives a rough cost estimate.

How to run it
Clone the repository:
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>

Install the required package:
pip install json5

Run the script:
python evaluate.py


After running, an evaluation_output.json file will be created with all the scores.

What the Script Does

Loads the sample conversation JSON.

Finds the last user query and the last model response.

Loads context chunks from the vector JSON.

Runs three evaluation checks:

Relevance – checks if the response matches the main parts of the query.

Completeness – checks how much of the query is covered.

Hallucination – checks whether the response is supported by the context.

Measures runtime.

Estimates a rough cost based on word count.

Saves the result into a JSON file.

Why This Approach

Simple and easy to understand.

No external APIs or heavy ML models.

Everything runs locally.

Fast string-based checks.

Easy to extend and modify.

Scaling

The script uses only basic Python operations (string matching, splits, etc.) which are very fast.
Since each conversation is processed independently, it can scale to large volumes easily.
No expensive operations or heavy dependencies are involved.

Files Included

evaluate.py — main script

sample-chat-conversation-02.json — chat input

sample_context_vectors-01.json — context chunks

evaluation_output.json — output file

README.md — documentation
