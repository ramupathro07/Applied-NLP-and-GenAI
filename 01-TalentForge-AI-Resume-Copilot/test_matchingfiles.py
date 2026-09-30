from utils import extract_text_from_resume, extract_resume_info, extract_job_info, calculate_match, generate_match_analysis
import json

# 1. Resume
resume_path = "data/resumes/pdf/graphite-resume-template-blue.pdf"  # change if needed
resume_text = extract_text_from_resume(resume_path)
resume_info = extract_resume_info(resume_text)

# 2. Job Description (you can paste any JD text here)
job_text = """
We are looking for an Administrative Assistant with experience in Microsoft Office, Google Workspace, HubSpot, and excellent communication skills. 
Candidate should have at least 2 years of experience in administrative roles. 
Knowledge of QuickBooks is a plus.
"""

job_info = extract_job_info(job_text)

# 3. Calculate Match
match_result = calculate_match(resume_info, job_info)

# 4. Generate Analysis
analysis = generate_match_analysis(resume_info, job_info, match_result)

# Final Output
print("\n========== RESUME INFO ==========")
print(json.dumps(resume_info, indent=2))

print("\n========== JOB INFO ==========")
print(json.dumps(job_info, indent=2))

print("\n========== MATCH RESULT ==========")
print(json.dumps(match_result, indent=2))

print("\n========== AI ANALYSIS ==========")
print(json.dumps(analysis, indent=2))