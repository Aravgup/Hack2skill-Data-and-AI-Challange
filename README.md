# AI-Powered Candidate Ranking System

### Redrob × India Runs Data & AI Challenge Submission

## Overview

This project was developed as part of the **Redrob – India Runs Data & AI Challenge**.

The objective of the challenge was to design and build an intelligent candidate ranking system capable of evaluating and ranking candidate profiles against a given Job Description (JD) at scale.

Traditional recruitment systems often rely heavily on keyword matching, which can overlook strong candidates and reward keyword stuffing. This solution uses **semantic understanding and multi-signal ranking** to identify the most relevant candidates while remaining computationally efficient and explainable.

The final system processes candidate profiles, evaluates relevance against a job description, ranks candidates, and generates a submission-ready CSV output.

---

## Problem Statement

Given:

* A Job Description (JD)
* Large-scale candidate profile data
* Candidate behavioural and profile signals

Build a ranking system that:

* Understands candidate relevance beyond keyword matching
* Produces explainable ranking decisions
* Scales efficiently under compute constraints
* Returns ranked candidates in the required submission format

---

## Solution Approach

This project follows a **retrieval + ranking pipeline**.

### 1. Job Description Processing

The uploaded `.docx` Job Description is extracted and converted into text.

### 2. Candidate Data Processing

Candidate information is loaded from `candidates.jsonl`.

Relevant profile attributes are extracted:

* Skills
* Professional headline
* Candidate summary
* Experience information

These attributes are merged into a unified candidate representation.

### 3. Semantic Embedding

Both:

* Job Description
* Candidate Profiles

are converted into vector embeddings using:

**SentenceTransformer → all-MiniLM-L6-v2**

This enables semantic similarity comparison instead of direct keyword matching.

### 4. Candidate Ranking

Each candidate receives a score based on:

```text
Final Score =
0.85 × Semantic Similarity
+
0.15 × Experience Score
```

Additional tie-breaking logic ensures:

* Higher score ranked first
* Equal scores → Candidate ID ascending

### 5. Submission Generation

Top candidates are exported into:

```plaintext
outputs/ranked_candidates.csv
```

Format:

```csv
candidate_id,rank,score,reasoning
```

---

## Project Structure

```plaintext
redrob-hackathon/
│
├── app.py
├── validate_submission.py
├── requirements.txt
│
├── data/
│   ├── candidates.jsonl
│   ├── candidate_schema.json
│   ├── job_description.docx
│   ├── redrob_signals_doc.docx
│
├── outputs/
│   └── ranked_candidates.csv
│
├── src/
│   ├── read_data.py
│   ├── embed.py
│   ├── rank.py
│   └── export.py
│
└── models/
```

---

## Installation

Clone the repository:

```bash
git clone <repository-link>
cd redrob-hackathon
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Project

Generate rankings:

```bash
python app.py
```

Validate submission:

```bash
python validate_submission.py outputs/ranked_candidates.csv
```

---

## Output

Generated file:

```plaintext
outputs/ranked_candidates.csv
```

Example:

```csv
candidate_id,rank,score,reasoning
CAND_001,1,0.98231,Strong semantic alignment with JD
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* SentenceTransformers
* Scikit-learn
* Python-docx
* VS Code

---

## Design Decisions

This solution was intentionally designed to:

* Prioritize semantic understanding over keyword matching
* Remain lightweight and CPU-friendly
* Produce explainable ranking outputs
* Follow challenge validation constraints

---

## Future Improvements

Potential enhancements:

* Hybrid BM25 + Semantic Retrieval
* Behavioural signal integration
* Candidate anomaly detection
* Re-ranking using gradient boosting
* Explainable AI dashboards

---

## Team

Developed for the **Redrob × India Runs Data & AI Challenge**.

Built with a focus on practical retrieval, scalable ranking, and explainable candidate evaluation.
