from utils import extract_text_from_pdf

# Path of your resume
pdf_path = "data/resume.pdf"

# Call the function
text = extract_text_from_pdf(pdf_path)

# Print the result
print(text)