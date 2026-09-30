import pdfplumber
from docx import Document
import os

def extract_text_from_pdf(pdf_path):
    """
    This function takes a PDF file path and returns all the text inside it.
    """
    full_text = ""

    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    full_text += text + "\n"

        return full_text.strip()

    except Exception as e:
        return f"Error reading PDF: {str(e)}"


def extract_text_from_docx(docx_path):
    """
    This function reads a Word (.docx) file and returns all the text.
    """
    try:
        doc = Document(docx_path)
        full_text = []

        for para in doc.paragraphs:
            if para.text.strip():
                full_text.append(para.text)

        return "\n".join(full_text)

    except Exception as e:
        return f"Error reading DOCX: {str(e)}"


def extract_text_from_resume(file_path, clean=True):
    """
    Universal function that extracts text from PDF or DOCX
    and optionally cleans it.
    """
    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension == ".pdf":
        text = extract_text_from_pdf(file_path)
    elif file_extension == ".docx":
        text = extract_text_from_docx(file_path)
    else:
        return "Unsupported file format. Please upload PDF or DOCX only."

    if clean and not text.startswith("Error"):
        text = clean_resume_text(text)

    return text
    
import re

def clean_resume_text(text):
    """
    This function cleans the extracted resume text.
    """
    if not text:
        return ""

    # 1. Replace multiple spaces with single space
    text = re.sub(r' +', ' ', text)

    # 2. Replace multiple newlines with single newline
    text = re.sub(r'\n+', '\n', text)

    # 3. Remove special unwanted characters (keep letters, numbers, basic punctuation)
    text = re.sub(r'[^\w\s\n.,@\-\(\)\/\+\#]', ' ', text)

    # 4. Remove spaces before punctuation
    text = re.sub(r'\s+([.,])', r'\1', text)

    # 5. Final strip
    text = text.strip()

    return text

from llm_helper import get_llm_response
import json

def extract_resume_info(resume_text):
    """
    Extracts structured information from resume text using LLM.
    """
    
    prompt = f"""
Extract information from the resume and return ONLY a valid JSON object.
Do not write any explanation or extra text.

Use exactly this JSON structure:

{{
  "name": "",
  "email": "",
  "phone": "",
  "skills": [],
  "education": [
    {{
      "degree": "",
      "institution": "",
      "year": ""
    }}
  ],
  "experience": [
    {{
      "job_title": "",
      "company": "",
      "duration": "",
      "description": ""
    }}
  ],
  "projects": [],
  "certifications": []
}}

Rules:
- If any field is missing, use empty string "" or empty list []
- skills must be a list of strings
- Return only pure JSON, nothing else

Resume Text:
{resume_text[:3500]}
"""

    response = get_llm_response(prompt)
    
    try:
        # Clean possible markdown
        response = response.strip()
        if response.startswith("```json"):
            response = response[7:]
        if response.startswith("```"):
            response = response[3:]
        if response.endswith("```"):
            response = response[:-3]
        response = response.strip()
        
        return json.loads(response)
    except Exception as e:
        return {
            "error": "Failed to parse JSON",
            "raw_response": response,
            "exception": str(e)
        }
        
        
def extract_job_info(job_text):
    """
    Extracts structured information from a Job Description using LLM.
    """
    
    prompt = f"""
Extract information from the Job Description and return ONLY a valid JSON object.
Do not write any explanation.

Use exactly this structure:

{{
  "job_title": "",
  "required_skills": [],
  "preferred_skills": [],
  "experience_required": "",
  "education_required": "",
  "key_responsibilities": []
}}

Rules:
- required_skills and preferred_skills must be lists of strings
- If any field is missing, use empty string or empty list
- Return only pure JSON

Job Description:
{job_text[:3500]}
"""

    response = get_llm_response(prompt)
    
    try:
        response = response.strip()
        if response.startswith("```json"):
            response = response[7:]
        if response.startswith("```"):
            response = response[3:]
        if response.endswith("```"):
            response = response[:-3]
        response = response.strip()
        
        return json.loads(response)
    except Exception as e:
        return {
            "error": "Failed to parse Job Description JSON",
            "raw_response": response,
            "exception": str(e)
        }
        
def calculate_match(resume_info, job_info):
    """
    Calculates match score between Resume and Job Description.
    """
    
    resume_skills = set([skill.lower().strip() for skill in resume_info.get("skills", [])])
    required_skills = set([skill.lower().strip() for skill in job_info.get("required_skills", [])])
    preferred_skills = set([skill.lower().strip() for skill in job_info.get("preferred_skills", [])])

    if not required_skills:
        return {
            "match_score": 0,
            "matched_skills": [],
            "missing_skills": [],
            "message": "No required skills found in Job Description"
        }

    matched_skills = resume_skills.intersection(required_skills)
    missing_skills = required_skills - resume_skills

    # Simple scoring logic
    match_percentage = (len(matched_skills) / len(required_skills)) * 100

    # Bonus for preferred skills
    preferred_matched = resume_skills.intersection(preferred_skills)
    bonus = min(len(preferred_matched) * 3, 15)  # max 15% bonus

    final_score = min(round(match_percentage + bonus, 2), 100)

    return {
        "match_score": final_score,
        "matched_skills": list(matched_skills),
        "missing_skills": list(missing_skills),
        "preferred_matched": list(preferred_matched)
    }
    
def generate_match_analysis(resume_info, job_info, match_result):
    """
    Uses LLM to generate explanation, missing skills analysis and interview questions.
    """
    
    prompt = f"""
You are an expert HR AI assistant.

Given the following information, generate a professional analysis.

Resume Skills: {resume_info.get('skills', [])}
Job Required Skills: {job_info.get('required_skills', [])}
Matched Skills: {match_result.get('matched_skills', [])}
Missing Skills: {match_result.get('missing_skills', [])}
Match Score: {match_result.get('match_score', 0)}%

Return ONLY a valid JSON with this structure:

{{
  "match_explanation": "Write 3-4 lines explaining why this score was given",
  "skill_gap_analysis": "Explain the missing skills and their importance",
  "interview_questions": [
    "Question 1",
    "Question 2",
    "Question 3",
    "Question 4",
    "Question 5"
  ],
  "recommendation": "Short recommendation (Hire / Consider / Reject) with reason"
}}
"""

    response = get_llm_response(prompt)
    
    try:
        response = response.strip()
        if response.startswith("```json"):
            response = response[7:]
        if response.startswith("```"):
            response = response[3:]
        if response.endswith("```"):
            response = response[:-3]
        response = response.strip()
        
        return json.loads(response)
    except Exception as e:
        return {
            "error": "Failed to generate analysis",
            "raw_response": response
        }
        
from llm_helper import get_llm_response
import json