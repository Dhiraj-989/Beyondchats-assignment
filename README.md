# Conversation Evaluation Script

This assignment contains a small evaluation pipeline that scores an AI’s response based on relevance, completeness, and hallucination. It also measures latency and gives a rough cost estimate.

---

## How to Run

### 1. Clone the repository
```bash
git clone https://github.com/Dhiraj-989/Beyondchats-assignment.git
cd Beyondchats-assignment
```

### 2. Install the required package
```bash
pip install json5
```

### 3. Run the script
```bash
python script.py
```

After running, an `evaluation_output.json` file will be created with all the scores.

---

## What the Script Does

- Loads the sample conversation JSON  
- Finds the last user query and the last model response  
- Loads context chunks from the vector JSON  
- Runs three evaluation checks:
  - **Relevance** – checks if the response matches important parts of the query  
  - **Completeness** – checks how much of the query is covered  
  - **Hallucination** – checks whether the response is supported by the context  
- Measures runtime  
- Estimates a rough cost based on word count  
- Saves everything into a JSON output file  

---

Architecture

[Architecture of evaluation pipeline.pdf](https://github.com/user-attachments/files/24141226/Architecture.of.evaluation.pipeline.pdf)

## Why This Approach

I kept the solution simple and easy to understand:
- Fully local and lightweight  
- No external API calls  
- No embeddings or heavy ML models  
- Uses fast string-based checks  
- Easy to read, modify, and extend  

---

## Scaling

The script relies only on basic Python string operations, which are extremely fast.  
Each conversation is evaluated independently, so the process scales well even for large volumes (millions of evaluations).  
Since there are no expensive computations or external services, latency and cost remain minimal.

---

## Files Included

- `evaluate.py` — main evaluation script  
- `sample-chat-conversation-02.json` — chat input  
- `sample_context_vectors-01.json` — context chunks  
- `evaluation_output.json` — output file created by the script  
- `README.md` — documentation  
