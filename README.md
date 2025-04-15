# Resume Parser

A Python-based **Resume Parser** that extracts relevant details from **PDF** or **DOCX** formatted resumes and converts it into a structured **JSON** format. This parser uses **spaCy** for Named Entity Recognition (NER) to extract **contact details** like **name**, **email**, and **phone**, as well as **education** information. The parsed data is outputted as a structured JSON object for easy processing.

## Features

- **Extract text** from **PDF** and **DOCX** resume formats.
- Identifies and extracts **contact information** such as **name**, **email**, and **phone**.
- Detects **education-related** information based on common keywords like **B.Tech**, **M.Tech**, **Bachelor**, **Master**, etc.
- Outputs the parsed resume data in a structured **JSON** format.
- Can be easily extended to include other sections such as **skills**, **experience**, **certifications**, etc.

## Requirements

To run the script, make sure to install the following dependencies:

- **pdfplumber**: For extracting text from **PDF** files.
- **python-docx**: For extracting text from **DOCX** files.
- **spaCy**: For Named Entity Recognition (NER) to identify **emails** and **phone numbers**.
- **re**: For regular expression-based parsing of name and education details.

### Install Dependencies

You can install the necessary libraries using pip:

```bash
pip install pdfplumber python-docx spacy
