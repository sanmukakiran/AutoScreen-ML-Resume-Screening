import re

# A predefined knowledge base / gazetteer of skills.
SKILLS_DB = [
    "python", "c", "c++", "c#", "java", "sql", "machine learning", "deep learning",
    "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch", "aws", "gcp", "azure",
    "django", "flask", "rest apis", "rest api", "postgresql", "mysql", "docker",
    "git", "linux", "ci/cd", "react", "angular", "tableau", "seo", "google analytics",
    "data processing", "predictive models", "nlp", "kubernetes", "javascript", "typescript"
]

def extract_skills(text):
    """
    Extracts predefined technical skills and keywords from the text using regular expressions.
    This avoids heavy NLP libraries like spaCy which are currently crashing on Python 3.14.
    """
    if not isinstance(text, str):
        return []

    text_lower = text.lower()
    extracted_skills = set()
    
    for skill in SKILLS_DB:
        # Special handling for skills with non-word characters which \b struggles with
        if skill in ["c++", "c#"]:
            # naive check, could be improved but sufficient for our dataset
            if skill in text_lower.split() or f" {skill} " in f" {text_lower} ":
                extracted_skills.add(skill)
        else:
            pattern = r'\b' + re.escape(skill) + r'\b'
            if re.search(pattern, text_lower):
                extracted_skills.add(skill)
        
    return list(extracted_skills)

if __name__ == "__main__":
    sample = "I am a Data Scientist! I have 4+ years of experience in Python, C++, and pandas."
    print("Original:", sample)
    print("Extracted Skills:", extract_skills(sample))
