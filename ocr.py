# app/ocr.py
import pytesseract
from PIL import Image
import fitz  # PyMuPDF for PDF

def extract_text_from_document(filepath):
    if filepath.endswith(".pdf"):
        return extract_text_from_pdf(filepath)
    else:
        return extract_text_from_image(filepath)

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text
