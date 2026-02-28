🚀 AutoScreen — ML-Based Resume Screening System

An intelligent NLP-powered system that automatically ranks resumes against a job description using semantic similarity and skill matching.

📌 Problem Statement

Recruiters often spend hours manually screening resumes for a single role. This process is:

Time-consuming

Inconsistent

Prone to human bias

Difficult to scale

AutoScreen automates the first round of resume screening using Natural Language Processing (NLP) and Machine Learning.

🎯 What AutoScreen Does

Given:

📄 A Job Description

📑 Multiple Resumes

The system:

✅ Extracts technical skills
✅ Computes semantic similarity (TF-IDF + Cosine Similarity)
✅ Calculates skill match percentage
✅ Identifies missing skills
✅ Ranks candidates automatically

The result: A clear, explainable shortlist of candidates.

⚙️ Key Features
🧠 NLP Text Preprocessing

Text cleaning

Stopword removal

Tokenization

Lemmatization (NLTK)

🛠 Skill Extraction Engine

Built using spaCy

Custom phrase matching

Extracts technologies like Python, AWS, SQL, React, etc.

📊 Semantic Matching (TF-IDF)

Converts text to numerical vectors

Computes Cosine Similarity between:

Resume vector

Job Description vector

🏆 Intelligent Ranking System

Final Score combines:

Similarity Score

Skill Match %

Candidates are ranked from most relevant to least relevant.

🔎 Explainable Output

For each candidate, the system provides:

Similarity Score

Skill Match %

Matched Skills

Missing Skills

Final Rank

🗂 Project Structure
AutoScreen/
│
├── data/
│   ├── job_descriptions/
│   └── resumes/
│
├── src/
│   ├── preprocessing.py
│   ├── skill_extractor.py
│   └── matcher.py
│
├── main.py
├── requirements.txt
└── README.md
🔄 How It Works (Step-by-Step)

1️⃣ Input Collection
Reads job description and resumes from /data.

2️⃣ Text Processing
Cleans and normalizes text using NLP techniques.

3️⃣ Skill Extraction
Identifies technical skills using spaCy phrase matching.

4️⃣ Vectorization
Transforms text using TF-IDF.

5️⃣ Similarity Scoring
Calculates Cosine Similarity between resume and job description.

6️⃣ Ranking & Reporting
Generates:

Ranked results in console

screening_report.csv for Excel

💻 Installation & Setup
1️⃣ Prerequisites

Python 3.8+

2️⃣ Install Dependencies
pip install -r requirements.txt

The first run will automatically download:

NLTK corpora

spaCy model (en_core_web_sm)

▶️ Usage

Place job description in:

data/job_descriptions/

Place resumes in:

data/resumes/

Run:

python main.py
📈 Output

The system generates:

📊 Ranked candidate list in terminal

📄 screening_report.csv for detailed evaluation

The CSV includes:

Candidate Name

Similarity Score

Skill Match %

Matched Skills

Missing Skills

Final Rank

🧪 Tech Stack

Python

NLTK

spaCy

Scikit-learn

TF-IDF Vectorizer

Cosine Similarity

Pandas

📌 Future Improvements

Streamlit Web Interface

PDF Resume Support

Deep Learning (BERT embeddings)

REST API integration

Database support

📜 License

This project is for educational and research purposes.