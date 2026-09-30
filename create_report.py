from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, PageBreak, 
    Table, TableStyle, ListFlowable, ListItem, KeepTogether
)
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Create the PDF
doc = SimpleDocTemplate(
    "/home/workdir/artifacts/TalentForge_AI_Project_Report.pdf",
    pagesize=A4,
    rightMargin=0.75*inch,
    leftMargin=0.75*inch,
    topMargin=0.7*inch,
    bottomMargin=0.7*inch
)

styles = getSampleStyleSheet()

# Custom Styles
styles.add(ParagraphStyle(
    name='MainTitle',
    parent=styles['Title'],
    fontSize=22,
    leading=28,
    alignment=TA_CENTER,
    spaceAfter=6,
    textColor=HexColor('#1a365d'),
    fontName='Helvetica-Bold'
))

styles.add(ParagraphStyle(
    name='SubTitle',
    parent=styles['Normal'],
    fontSize=14,
    leading=18,
    alignment=TA_CENTER,
    spaceAfter=4,
    textColor=HexColor('#2c5282'),
    fontName='Helvetica-Bold'
))

styles.add(ParagraphStyle(
    name='SectionHeading',
    parent=styles['Heading1'],
    fontSize=14,
    leading=18,
    spaceBefore=16,
    spaceAfter=8,
    textColor=HexColor('#1a365d'),
    fontName='Helvetica-Bold'
))

styles.add(ParagraphStyle(
    name='SubHeading',
    parent=styles['Heading2'],
    fontSize=12,
    leading=15,
    spaceBefore=12,
    spaceAfter=6,
    textColor=HexColor('#2b6cb0'),
    fontName='Helvetica-Bold'
))

styles.add(ParagraphStyle(
    name='BodyTextJustify',
    parent=styles['Normal'],
    fontSize=10.5,
    leading=15,
    alignment=TA_JUSTIFY,
    spaceAfter=8,
    fontName='Helvetica'
))

styles.add(ParagraphStyle(
    name='BulletText',
    parent=styles['Normal'],
    fontSize=10.5,
    leading=14,
    leftIndent=15,
    spaceAfter=3,
    fontName='Helvetica'
))

styles.add(ParagraphStyle(
    name='CenterText',
    parent=styles['Normal'],
    fontSize=11,
    leading=14,
    alignment=TA_CENTER,
    spaceAfter=4,
    fontName='Helvetica'
))

styles.add(ParagraphStyle(
    name='FooterStyle',
    parent=styles['Normal'],
    fontSize=8,
    alignment=TA_CENTER,
    textColor=HexColor('#718096')
))

story = []

# ==================== TITLE PAGE ====================
story.append(Spacer(1, 1.5*inch))
story.append(Paragraph("TalentForge AI", styles['MainTitle']))
story.append(Spacer(1, 8))
story.append(Paragraph("Intelligent Resume & Job Matching Copilot", styles['SubTitle']))
story.append(Spacer(1, 6))
story.append(Paragraph("using NLP and Generative AI", styles['CenterText']))
story.append(Spacer(1, 30))

story.append(Paragraph("A Project Report", styles['CenterText']))
story.append(Spacer(1, 20))

story.append(Paragraph("Submitted in partial fulfillment of the requirements<br/>for the award of the degree of", styles['CenterText']))
story.append(Spacer(1, 12))
story.append(Paragraph("<b>Bachelor of Technology</b><br/>in<br/><b>Computer Science and Engineering</b>", styles['CenterText']))
story.append(Spacer(1, 40))

story.append(Paragraph("Submitted by", styles['CenterText']))
story.append(Paragraph("<b>[Your Full Name]</b>", styles['CenterText']))
story.append(Paragraph("Roll No: [Your Roll Number]", styles['CenterText']))
story.append(Spacer(1, 30))

story.append(Paragraph("Under the Guidance of", styles['CenterText']))
story.append(Paragraph("<b>[Guide Name]</b>", styles['CenterText']))
story.append(Spacer(1, 40))

story.append(Paragraph("<b>[Your College / University Name]</b>", styles['CenterText']))
story.append(Paragraph("Academic Year 2025-26", styles['CenterText']))

story.append(PageBreak())

# ==================== ABSTRACT ====================
story.append(Paragraph("ABSTRACT", styles['SectionHeading']))
story.append(Paragraph(
    "In the modern recruitment landscape, organizations receive a large volume of resumes for every job opening. "
    "Traditional Applicant Tracking Systems (ATS) primarily rely on keyword matching, which often fails to understand "
    "the semantic meaning of skills and experience. This leads to inefficient screening, missed suitable candidates, "
    "and increased manual effort for recruiters.",
    styles['BodyTextJustify']
))
story.append(Paragraph(
    "This project presents <b>TalentForge AI</b>, an intelligent resume and job matching system built using Natural Language "
    "Processing (NLP) and Generative AI. The system can process both PDF and DOCX resumes, extract structured information "
    "such as skills, education, experience, projects, and certifications using Large Language Models (LLMs), and compare "
    "them against job descriptions. It calculates a meaningful match score, identifies skill gaps, generates an explainable "
    "analysis, and suggests relevant interview questions.",
    styles['BodyTextJustify']
))
story.append(Paragraph(
    "A user-friendly web interface was developed using Streamlit, allowing recruiters and users to upload resumes, paste "
    "job descriptions, and receive instant AI-powered insights. The system demonstrates how modern Generative AI techniques "
    "can make the recruitment process faster, more transparent, and skill-focused.",
    styles['BodyTextJustify']
))
story.append(Paragraph(
    "<b>Keywords:</b> Natural Language Processing, Generative AI, Resume Parsing, Job Matching, Large Language Models, "
    "Streamlit, Information Extraction, Semantic Matching",
    styles['BodyTextJustify']
))

story.append(PageBreak())

# ==================== INTRODUCTION ====================
story.append(Paragraph("1. INTRODUCTION", styles['SectionHeading']))

story.append(Paragraph("1.1 Background", styles['SubHeading']))
story.append(Paragraph(
    "Recruitment is a critical function in every organization. With the increasing number of job applications, "
    "manual screening of resumes has become impractical. Most companies use Applicant Tracking Systems (ATS) to "
    "filter candidates. However, the majority of these systems still depend on simple keyword matching. This approach "
    "has significant limitations because it does not understand context, synonyms, or the actual meaning of skills.",
    styles['BodyTextJustify']
))
story.append(Paragraph(
    "For example, a candidate who writes “Python programming” may be rejected if the job description only mentions "
    "“Python development”, even though both mean the same skill. Similarly, important soft skills and project experience "
    "are often overlooked. There is a clear need for a smarter system that can understand resumes and job descriptions "
    "at a deeper level.",
    styles['BodyTextJustify']
))

story.append(Paragraph("1.2 Problem Statement", styles['SubHeading']))
story.append(Paragraph(
    "The major problems identified in the current recruitment process are:",
    styles['BodyTextJustify']
))
story.append(Paragraph("• Heavy dependence on keyword-based matching which ignores semantic meaning.", styles['BulletText']))
story.append(Paragraph("• High time and cost involved in manual resume screening.", styles['BulletText']))
story.append(Paragraph("• Difficulty in identifying skill gaps of candidates.", styles['BulletText']))
story.append(Paragraph("• Lack of explainable results from existing ATS tools.", styles['BulletText']))
story.append(Paragraph("• Absence of automatic generation of relevant interview questions.", styles['BulletText']))

story.append(Paragraph("1.3 Objectives", styles['SubHeading']))
story.append(Paragraph(
    "The primary objectives of this project are:",
    styles['BodyTextJustify']
))
story.append(Paragraph("1. To develop a system that can extract structured information from resumes in PDF and DOCX formats.", styles['BulletText']))
story.append(Paragraph("2. To understand job descriptions using Generative AI techniques.", styles['BulletText']))
story.append(Paragraph("3. To calculate an intelligent match score between a candidate’s resume and a job description.", styles['BulletText']))
story.append(Paragraph("4. To identify missing skills and provide a clear skill gap analysis.", styles['BulletText']))
story.append(Paragraph("5. To automatically generate relevant interview questions based on the match analysis.", styles['BulletText']))
story.append(Paragraph("6. To provide a clean and user-friendly web interface for easy interaction.", styles['BulletText']))

story.append(Paragraph("1.4 Scope of the Project", styles['SubHeading']))
story.append(Paragraph(
    "The system supports English language resumes in PDF and DOCX formats. It focuses on extracting key information "
    "such as personal details, skills, education, work experience, projects, and certifications. The matching is primarily "
    "skill-based with Generative AI explanations. The current version is designed as a working prototype suitable for "
    "academic demonstration and can be extended for real-world use.",
    styles['BodyTextJustify']
))

story.append(Paragraph("1.5 Organization of the Report", styles['SubHeading']))
story.append(Paragraph(
    "This report is organized as follows: Section 2 presents the literature review. Section 3 discusses system analysis. "
    "Section 4 explains the system design and architecture. Section 5 describes the implementation details. Section 6 "
    "presents the results and discussion. Section 7 concludes the project and suggests future enhancements.",
    styles['BodyTextJustify']
))

# ==================== LITERATURE REVIEW ====================
story.append(Paragraph("2. LITERATURE REVIEW", styles['SectionHeading']))

story.append(Paragraph(
    "Several research works have been carried out in the area of automated resume screening and job matching. "
    "Early systems relied heavily on rule-based and keyword-based approaches. These systems were simple but suffered "
    "from low accuracy because they could not handle variations in language.",
    styles['BodyTextJustify']
))
story.append(Paragraph(
    "With the advancement of Natural Language Processing, researchers started using techniques such as Named Entity "
    "Recognition (NER), TF-IDF, and later transformer-based models like BERT for semantic matching. These approaches "
    "improved the quality of matching by understanding context rather than just exact words.",
    styles['BodyTextJustify']
))
story.append(Paragraph(
    "Recent developments in Large Language Models (LLMs) and Generative AI have opened new possibilities. LLMs can "
    "extract structured information from unstructured text with high accuracy and can also generate human-like explanations. "
    "This project builds upon these advancements by combining document parsing, LLM-based information extraction, "
    "skill matching, and Generative AI analysis into a single practical system.",
    styles['BodyTextJustify']
))
story.append(Paragraph(
    "The proposed system differs from traditional ATS tools by providing explainable results, skill gap analysis, and "
    "automatically generated interview questions, making the recruitment process more transparent and efficient.",
    styles['BodyTextJustify']
))

# ==================== SYSTEM ANALYSIS ====================
story.append(Paragraph("3. SYSTEM ANALYSIS", styles['SectionHeading']))

story.append(Paragraph("3.1 Existing System", styles['SubHeading']))
story.append(Paragraph(
    "Most existing Applicant Tracking Systems work on keyword matching. They scan the resume for specific words "
    "mentioned in the job description. If the exact words are not found, the candidate is filtered out. This method "
    "is fast but inaccurate. It does not understand synonyms, related skills, or the overall suitability of the candidate.",
    styles['BodyTextJustify']
))

story.append(Paragraph("3.2 Proposed System", styles['SubHeading']))
story.append(Paragraph(
    "TalentForge AI is designed to overcome the limitations of traditional systems. It uses the following approach:",
    styles['BodyTextJustify']
))
story.append(Paragraph("• Document parsing to extract clean text from PDF and DOCX files.", styles['BulletText']))
story.append(Paragraph("• Large Language Model based structured information extraction.", styles['BulletText']))
story.append(Paragraph("• Skill-based matching between resume and job description.", styles['BulletText']))
story.append(Paragraph("• Generative AI for match explanation, skill gap analysis, and interview question generation.", styles['BulletText']))
story.append(Paragraph("• A modern web interface built with Streamlit for easy user interaction.", styles['BulletText']))

story.append(Paragraph("3.3 Feasibility Study", styles['SubHeading']))
story.append(Paragraph(
    "<b>Technical Feasibility:</b> The required technologies (Python, Streamlit, Groq LLM API, pdfplumber, python-docx) "
    "are freely available and well-documented. The system can be developed and run on a standard laptop.",
    styles['BodyTextJustify']
))
story.append(Paragraph(
    "<b>Economic Feasibility:</b> Most components used in the project are open-source or offer free tiers, making the "
    "project economically feasible for academic purposes.",
    styles['BodyTextJustify']
))
story.append(Paragraph(
    "<b>Operational Feasibility:</b> The system has a simple user interface. Users only need to upload a resume and "
    "paste a job description to get results, making it operationally feasible.",
    styles['BodyTextJustify']
))

# ==================== SYSTEM DESIGN ====================
story.append(Paragraph("4. SYSTEM DESIGN AND ARCHITECTURE", styles['SectionHeading']))

story.append(Paragraph("4.1 System Architecture", styles['SubHeading']))
story.append(Paragraph(
    "The system follows a modular pipeline architecture consisting of the following layers:",
    styles['BodyTextJustify']
))
story.append(Paragraph("1. <b>Document Ingestion Layer</b> – Accepts PDF/DOCX resumes and job description text.", styles['BulletText']))
story.append(Paragraph("2. <b>Text Extraction & Cleaning Layer</b> – Extracts and cleans text from documents.", styles['BulletText']))
story.append(Paragraph("3. <b>Information Extraction Layer</b> – Uses LLM to extract structured data (skills, education, experience, etc.).", styles['BulletText']))
story.append(Paragraph("4. <b>Matching Engine</b> – Compares resume skills with job required skills and calculates match score.", styles['BulletText']))
story.append(Paragraph("5. <b>Generative AI Analysis Layer</b> – Generates explanations, skill gap analysis, and interview questions.", styles['BulletText']))
story.append(Paragraph("6. <b>Presentation Layer</b> – Streamlit web interface for user interaction and result display.", styles['BulletText']))

story.append(Paragraph("4.2 Workflow", styles['SubHeading']))
story.append(Paragraph(
    "The complete workflow of the system is as follows:",
    styles['BodyTextJustify']
))
story.append(Paragraph("Step 1: User uploads a resume (PDF or DOCX) and pastes a job description.", styles['BulletText']))
story.append(Paragraph("Step 2: System extracts clean text from the resume.", styles['BulletText']))
story.append(Paragraph("Step 3: LLM extracts structured information from both resume and job description.", styles['BulletText']))
story.append(Paragraph("Step 4: Matching engine calculates the match score based on skill overlap.", styles['BulletText']))
story.append(Paragraph("Step 5: Generative AI produces explanation, missing skills analysis, and interview questions.", styles['BulletText']))
story.append(Paragraph("Step 6: Results are displayed on the web interface with option to download the report.", styles['BulletText']))

story.append(Paragraph("4.3 Data Flow", styles['SubHeading']))
story.append(Paragraph(
    "Resume File → Text Extraction → Cleaning → LLM Extraction → Structured JSON → Matching Engine → "
    "Score + Matched/Missing Skills → Generative AI Analysis → Final Report on UI",
    styles['BodyTextJustify']
))

# ==================== IMPLEMENTATION ====================
story.append(Paragraph("5. IMPLEMENTATION", styles['SectionHeading']))

story.append(Paragraph("5.1 Technology Stack", styles['SubHeading']))
story.append(Paragraph("• <b>Programming Language:</b> Python 3.10+", styles['BulletText']))
story.append(Paragraph("• <b>Web Framework:</b> Streamlit", styles['BulletText']))
story.append(Paragraph("• <b>Document Parsing:</b> pdfplumber, python-docx", styles['BulletText']))
story.append(Paragraph("• <b>Large Language Model:</b> Groq API (openai/gpt-oss-20b)", styles['BulletText']))
story.append(Paragraph("• <b>Environment Management:</b> python-dotenv", styles['BulletText']))
story.append(Paragraph("• <b>Other Libraries:</b> json, re, os", styles['BulletText']))

story.append(Paragraph("5.2 Key Modules", styles['SubHeading']))
story.append(Paragraph(
    "<b>utils.py</b> – Contains all core functions: text extraction from PDF/DOCX, text cleaning, "
    "resume information extraction, job information extraction, match score calculation, and AI analysis generation.",
    styles['BodyTextJustify']
))
story.append(Paragraph(
    "<b>llm_helper.py</b> – Handles communication with the Groq Large Language Model API.",
    styles['BodyTextJustify']
))
story.append(Paragraph(
    "<b>application.py</b> – Streamlit based web application that provides the user interface.",
    styles['BodyTextJustify']
))

story.append(Paragraph("5.3 Important Functions", styles['SubHeading']))
story.append(Paragraph("• <b>extract_text_from_resume()</b> – Universal function to read both PDF and DOCX files.", styles['BulletText']))
story.append(Paragraph("• <b>clean_resume_text()</b> – Cleans extracted text by removing noise and extra spaces.", styles['BulletText']))
story.append(Paragraph("• <b>extract_resume_info()</b> – Uses LLM to extract structured resume data in JSON format.", styles['BulletText']))
story.append(Paragraph("• <b>extract_job_info()</b> – Extracts required skills and other details from job description.", styles['BulletText']))
story.append(Paragraph("• <b>calculate_match()</b> – Computes match score based on skill overlap.", styles['BulletText']))
story.append(Paragraph("• <b>generate_match_analysis()</b> – Generates explanation, skill gap analysis, and interview questions.", styles['BulletText']))

story.append(Paragraph("5.4 User Interface", styles['SubHeading']))
story.append(Paragraph(
    "The web interface was developed using Streamlit. It allows users to upload a resume, paste a job description, "
    "and click the Analyze button. The system then displays the match score, matched and missing skills, AI-generated "
    "explanation, skill gap analysis, interview questions, and a downloadable report. The interface uses a modern dark "
    "theme with clear visual hierarchy and tabbed sections for better user experience.",
    styles['BodyTextJustify']
))

# ==================== RESULTS ====================
story.append(Paragraph("6. RESULTS AND DISCUSSION", styles['SectionHeading']))

story.append(Paragraph(
    "The system was tested with multiple sample resumes and job descriptions. It successfully extracted structured "
    "information such as name, email, phone, skills, education, and experience from resumes. The match score was "
    "calculated based on the overlap of skills between the resume and the job description.",
    styles['BodyTextJustify']
))
story.append(Paragraph(
    "In one of the test cases, the system achieved a match score of approximately 69–78% depending on the resume and "
    "job description used. The AI analysis correctly identified matched skills and missing skills, and generated "
    "relevant interview questions. The recommendation provided by the system was also consistent with the match score.",
    styles['BodyTextJustify']
))
story.append(Paragraph(
    "The Streamlit interface performed smoothly and displayed all results in a clear and organized manner. Users can "
    "easily download the full analysis report for further use.",
    styles['BodyTextJustify']
))
story.append(Paragraph(
    "<b>Limitations:</b> The current matching is primarily skill-based. It does not yet use deep semantic embeddings "
    "for full contextual understanding. The quality of extraction also depends on the clarity of the resume text and "
    "the performance of the underlying LLM.",
    styles['BodyTextJustify']
))

# ==================== CONCLUSION ====================
story.append(Paragraph("7. CONCLUSION AND FUTURE SCOPE", styles['SectionHeading']))

story.append(Paragraph("7.1 Conclusion", styles['SubHeading']))
story.append(Paragraph(
    "TalentForge AI successfully demonstrates the application of Natural Language Processing and Generative AI in the "
    "recruitment domain. The system can read resumes, understand job descriptions, calculate meaningful match scores, "
    "identify skill gaps, and generate interview questions. The web interface makes the system accessible and practical "
    "for demonstration and real-world testing. Overall, the project achieves its stated objectives and provides a solid "
    "foundation for intelligent recruitment assistance.",
    styles['BodyTextJustify']
))

story.append(Paragraph("7.2 Future Scope", styles['SubHeading']))
story.append(Paragraph("The following enhancements can be made in future versions of the system:", styles['BodyTextJustify']))
story.append(Paragraph("• Integration of semantic embeddings (sentence-transformers) for deeper contextual matching.", styles['BulletText']))
story.append(Paragraph("• Support for ranking multiple resumes against a single job description.", styles['BulletText']))
story.append(Paragraph("• Bias detection and fairness analysis in matching results.", styles['BulletText']))
story.append(Paragraph("• Multilingual resume and job description support.", styles['BulletText']))
story.append(Paragraph("• Integration with real Applicant Tracking Systems and job portals.", styles['BulletText']))
story.append(Paragraph("• Addition of a vector database for storing and searching large volumes of resumes.", styles['BulletText']))

# ==================== REFERENCES ====================
story.append(Paragraph("8. REFERENCES", styles['SectionHeading']))
story.append(Paragraph("1. Related research papers on resume parsing and job matching (MDPI and other journals).", styles['BulletText']))
story.append(Paragraph("2. Groq API Documentation – https://console.groq.com/docs", styles['BulletText']))
story.append(Paragraph("3. Streamlit Documentation – https://docs.streamlit.io", styles['BulletText']))
story.append(Paragraph("4. pdfplumber and python-docx library documentation.", styles['BulletText']))
story.append(Paragraph("5. Hugging Face and sentence-transformers resources for future semantic matching.", styles['BulletText']))

# ==================== APPENDIX ====================
story.append(Paragraph("9. APPENDIX", styles['SectionHeading']))
story.append(Paragraph(
    "The appendix contains screenshots of the working application showing the user interface, match score display, "
    "matched and missing skills, AI analysis, and interview questions generated by the system. These screenshots "
    "demonstrate the successful end-to-end functioning of TalentForge AI.",
    styles['BodyTextJustify']
))
story.append(Paragraph(
    "(Insert your application screenshots here while preparing the final printed report.)",
    styles['BodyTextJustify']
))

# Build PDF
doc.build(story)
print("PDF created successfully: /home/workdir/artifacts/TalentForge_AI_Project_Report.pdf")