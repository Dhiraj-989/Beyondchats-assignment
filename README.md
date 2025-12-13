# Conversation Evaluation Script

Setup
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
![Architecture of evaluation pipeline_page-0001](https://github.com/user-attachments/assets/800ea3eb-9e43-4863-a7ea-985ec0b87ea7)

## Why This Approach ?

I kept the solution simple and easy to understand:
- Fully local and lightweight  
- No external API calls  
- No embeddings or heavy ML models  
- Uses fast string-based checks   

---

## Scaling

- No additional LLM or external API calls are made during evaluation, eliminating inference costs and network latency.

- All metrics are computed using lightweight string operations with linear-time complexity --> O(n).

- Evaluation is bounded to the latest user query, model response, and a fixed set of context chunks, ensuring predictable latency.

- Minimal dependencies and local computation keep the per-request cost negligible, even at large scale.
