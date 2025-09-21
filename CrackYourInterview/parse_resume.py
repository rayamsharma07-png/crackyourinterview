import re
from pdfminer.high_level import extract_text
from docx import Document

def extract_text_from_pdf(file_path):
    return extract_text(file_path)

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def parse_resume(text):
    email = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    phone = re.findall(r"\+?\d[\d -]{8,}\d", text)
    skills_list = ["Python", "JavaScript", "React", "UI/UX", "Node.js"]
    skills = [skill for skill in skills_list if skill.lower() in text.lower()]
    
    return {
        "email": email[0] if email else None,
        "phone": phone[0] if phone else None,
        "skills": skills,
        "raw_text": text
    }
