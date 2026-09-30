from utils import extract_text_from_resume, extract_resume_info
import json

# Change to one of your PDF files
pdf_path = "data/resumes/pdf/graphite-resume-template-blue.pdf"

print("Step 1: Extracting text...")
resume_text = extract_text_from_resume(pdf_path)

print("Step 2: Extracting structured information using AI...\n")
info = extract_resume_info(resume_text)

print("=" * 60)
print(json.dumps(info, indent=2))
print("=" * 60)