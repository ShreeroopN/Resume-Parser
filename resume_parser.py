import pdfplumber
import docx
import spacy
import re
import json
import os

import warnings
warnings.filterwarnings("ignore", message="CropBox missing from /Page, defaulting to MediaBox")

# Load spaCy model for named entity recognition (NER)
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file_path):
    with pdfplumber.open(file_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()
        return text

def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    text = ""
    for para in doc.paragraphs:
        text += para.text + "\n"
    return text

def extract_contact_info(text):
    doc = nlp(text)
    
    # Extract emails and phone numbers using spaCy NER (can improve with regex if needed)
    emails = []
    phones = []
    
    for ent in doc.ents:
        if ent.label_ == "EMAIL":
            emails.append(ent.text)
        elif ent.label_ == "PHONE":
            phones.append(ent.text)
    
    return emails, phones

def extract_name_and_education(text):
    
    name_match = re.search(r"([A-Z][a-z]+(?: [A-Z][a-z]+)+)", text)
    name = name_match.group(0) if name_match else "Unknown"

   
    education_keywords = ["B.Tech", "M.Tech", "Bachelor", "Master", "Ph.D", "Degree"]
    education = [line for line in text.splitlines() if any(keyword in line for keyword in education_keywords)]
    
    return name, education

def parse_resume(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()

    
    if file_extension == '.pdf':
        text = extract_text_from_pdf(file_path)
    elif file_extension == '.docx':
        text = extract_text_from_docx(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a .pdf or .docx file.")
    
    
    emails, phones = extract_contact_info(text)
    
    
    name, education = extract_name_and_education(text)
    
    
    resume_data = {
        "name": name,
        "contact": {
            "email": emails[0] if emails else "Not Provided",
            "phone": phones[0] if phones else "Not Provided"
        },
        "education": education,
        "skills": [],  
        "experience": [],  
        "projects": [],  
        "certifications": [],  
        "languages": [],  
        "links": []  
    }
    
    return resume_data


def main():
    file_path = input("Enter the path to the resume (PDF or DOCX): ")
    try:
        resume_json = parse_resume(file_path)
        print("Parsed Resume Data:")
        print(json.dumps(resume_json, indent=4))  
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
