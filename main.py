import os
import glob
import pandas as pd
from src.preprocessing import preprocess_text
from src.skill_extractor import extract_skills
from src.matcher import calculate_similarity, skill_gap_analysis
from src.visualizer import generate_screening_visuals

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

def load_text(filepath):
    """Reads text from a given file path."""
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def process_resumes(job_desc_path, resumes_dir):
    """
    End-to-end pipeline:
    1. Loads and processes Job Description.
    2. Loads and processes all candidate resumes.
    3. Scores, compares, and ranks candidates against the JD.
    """
    print(f"\n--- Loading Job Description from: {job_desc_path} ---")
    jd_raw = load_text(job_desc_path)
    jd_clean = preprocess_text(jd_raw)
    jd_skills = extract_skills(jd_raw)
    
    print(f"Extracted Job Description Required Skills: {jd_skills}\n")
    
    resume_files = glob.glob(os.path.join(resumes_dir, "*.txt"))
    results = []
    
    if not resume_files:
        print("No resumes found in directory.")
        return
        
    print(f"Processing {len(resume_files)} resumes...\n")
    
    for r_path in resume_files:
        filename = os.path.basename(r_path)
        r_raw = load_text(r_path)
        
        # NLP Pipeline
        r_clean = preprocess_text(r_raw)
        r_skills = extract_skills(r_raw)
        
        # Scoring & Analysis
        sim_score = calculate_similarity(jd_clean, r_clean)
        gap_analysis = skill_gap_analysis(jd_skills, r_skills)
        
        results.append({
            "Candidate": filename.replace('.txt', ''),
            "TF-IDF Sim Score": round(sim_score * 100, 2),
            "Skill Match %": round(gap_analysis["match_percentage"], 2),
            "Matched Skills": ", ".join(gap_analysis["matched"]) if gap_analysis["matched"] else "None",
            "Missing Skills": ", ".join(gap_analysis["missing"]) if gap_analysis["missing"] else "None"
        })
    
    # Format the DataFrame and sort by Score
    df = pd.DataFrame(results)
    
    # Composite Ranking Logic: Primary sort by TF-IDF Similarity, secondary by Skill Match
    df = df.sort_values(by=["TF-IDF Sim Score", "Skill Match %"], ascending=[False, False]).reset_index(drop=True)
    df.index = df.index + 1 # Transform 0-index to 1-based Ranking
    
    print("========== Candidate Rankings ==========")
    print(df.to_string())
    print("========================================\n")
    
    # Save the output to a CSV report for recruiters
    output_path = "screening_report.csv"
    df.to_csv(output_path)
    print(f"Saved full report to {output_path}")
    
    # Generate visual reports
    role_name = os.path.basename(job_desc_path).replace('jd_', '').replace('.txt', '').replace('_', ' ').title()
    generate_screening_visuals(df, role_name)
    
    return df

if __name__ == "__main__":
    # Base paths
    jd_path = "data/job_descriptions/jd_data_scientist.txt"
    resumes_dir = "data/resumes"
    
    # Run pipeline
    if os.path.exists(jd_path) and os.path.exists(resumes_dir):
        process_resumes(jd_path, resumes_dir)
        
        # Let's run it again for the Software Engineer role to demonstrate flexibility
        print("\n\n" + "*"*50)
        jd_path_se = "data/job_descriptions/jd_software_engineer.txt"
        process_resumes(jd_path_se, resumes_dir)
        
    else:
        print("Data directories not found. Please ensure data/job_descriptions and data/resumes exist.")
