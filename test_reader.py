from utils import extract_text_from_resume

pdf_path = "data/resumes/pdf/graphite-resume-template-blue.pdf"  # change if needed

print("Reading and Cleaning Resume...\n")

text = extract_text_from_resume(pdf_path)

print("=" * 60)
print(text[:2000])
print("=" * 60)
print("\nTotal characters after cleaning:", len(text))