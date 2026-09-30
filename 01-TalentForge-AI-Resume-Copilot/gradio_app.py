import gradio as gr
import os
from utils import (
    extract_text_from_resume,
    extract_resume_info,
    extract_job_info,
    calculate_match,
    generate_match_analysis
)
import json

def process_resume_and_job(resume_file, job_description):
    if resume_file is None:
        return "Please upload a resume.", "", "", "", "", ""
    
    if not job_description or job_description.strip() == "":
        return "Please paste a Job Description.", "", "", "", "", ""

    try:
        # Save uploaded file temporarily
        file_path = resume_file.name
        file_ext = os.path.splitext(file_path)[1].lower()
        
        temp_path = f"temp_resume{file_ext}"
        with open(temp_path, "wb") as f:
            f.write(open(file_path, "rb").read())

        # Pipeline
        resume_text = extract_text_from_resume(temp_path)
        resume_info = extract_resume_info(resume_text)
        job_info = extract_job_info(job_description)
        match_result = calculate_match(resume_info, job_info)
        analysis = generate_match_analysis(resume_info, job_info, match_result)

        # Clean temp file
        if os.path.exists(temp_path):
            os.remove(temp_path)

        # Prepare outputs
        score = match_result.get("match_score", 0)
        candidate_name = resume_info.get("name", "Candidate")

        matched = "\n".join([f"✅ {s}" for s in match_result.get("matched_skills", [])]) or "None"
        missing = "\n".join([f"❌ {s}" for s in match_result.get("missing_skills", [])]) or "None"

        explanation = analysis.get("match_explanation", "No explanation available")
        skill_gap = analysis.get("skill_gap_analysis", "No analysis available")
        recommendation = analysis.get("recommendation", "No recommendation")

        questions = analysis.get("interview_questions", [])
        questions_text = "\n".join([f"{i+1}. {q}" for i, q in enumerate(questions)]) or "No questions generated"

        score_text = f"### Match Score: {score}%\n\n**Candidate:** {candidate_name}\n\n**Recommendation:** {recommendation}"

        return score_text, matched, missing, explanation, skill_gap, questions_text

    except Exception as e:
        return f"Error occurred: {str(e)}", "", "", "", "", ""


# ====================== GRADIO UI ======================
with gr.Blocks(title="TalentForge AI", theme=gr.themes.Soft()) as demo:

    gr.Markdown("""
    # 🤖 TalentForge AI
    ### Intelligent Resume & Job Matching Copilot
    Upload a resume and paste a job description to get AI-powered matching, skill gap analysis, and interview questions.
    """)

    with gr.Row():
        with gr.Column():
            resume_input = gr.File(label="📄 Upload Resume (PDF or DOCX)", file_types=[".pdf", ".docx"])
            job_input = gr.Textbox(label="💼 Job Description", lines=12, placeholder="Paste the complete job description here...")
            analyze_btn = gr.Button("🔍 Analyze Match", variant="primary")

        with gr.Column():
            score_output = gr.Markdown(label="Match Score")
            
            with gr.Row():
                matched_output = gr.Textbox(label="✅ Matched Skills", lines=6)
                missing_output = gr.Textbox(label="❌ Missing Skills", lines=6)

            explanation_output = gr.Textbox(label="📝 Match Explanation", lines=4)
            skillgap_output = gr.Textbox(label="🔍 Skill Gap Analysis", lines=4)
            questions_output = gr.Textbox(label="🎤 Interview Questions", lines=8)

    analyze_btn.click(
        fn=process_resume_and_job,
        inputs=[resume_input, job_input],
        outputs=[score_output, matched_output, missing_output, explanation_output, skillgap_output, questions_output]
    )

    gr.Markdown("---\nBuilt with NLP + Generative AI | TalentForge AI")

# Launch
demo.launch()