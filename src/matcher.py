from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(job_desc_text, resume_text):
    """
    Calculates the cosine similarity between the preprocessed job description 
    and the resume using TF-IDF vectors.
    """
    if not job_desc_text or not resume_text:
        return 0.0
        
    vectorizer = TfidfVectorizer()
    # Fit and transform the texts together to share the same vocabulary
    tfidf_matrix = vectorizer.fit_transform([job_desc_text, resume_text])
    
    # Calculate cosine similarity between the first (JD) and second (Resume) vectors
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])
    return similarity[0][0]

def skill_gap_analysis(required_skills, candidate_skills):
    """
    Compares required skills with candidate skills.
    Returns matched skills, missing skills, and a percentage match score.
    """
    req_set = set(s.lower() for s in required_skills)
    cand_set = set(s.lower() for s in candidate_skills)
    
    matched = req_set.intersection(cand_set)
    missing = req_set.difference(cand_set)
    extra = cand_set.difference(req_set) # Candidate's additional skills
    
    match_percentage = (len(matched) / len(req_set) * 100) if req_set else 100.0
    
    return {
        "matched": list(matched),
        "missing": list(missing),
        "extra": list(extra),
        "match_percentage": match_percentage
    }

if __name__ == "__main__":
    # Quick test
    jd = "data science, python, machine learning, deep learning"
    resume = "I know python, machine learning, and sql"
    print("Similarity:", calculate_similarity(jd, resume))
    print("Skill Gap:", skill_gap_analysis(["python", "machine learning", "deep learning"], ["python", "machine learning", "sql"]))
