
import streamlit as st
import os
from app.ocr import extract_text_from_document
from app.classifier import classify_document
from app.extractor import extract_information
from app.complexity import assess_complexity
from app.router import route_claim

st.set_page_config(page_title="Claims Automation", layout="wide")
st.title(" Claims Automation & Complexity Routing System")

uploaded_file = st.file_uploader("Upload a Claim Document (PDF/Image/TXT)", type=["pdf", "png", "jpg", "jpeg", "txt"])

if uploaded_file:
    os.makedirs("data", exist_ok=True)

    filepath = os.path.join("data", uploaded_file.name)
    with open(filepath, "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("🔄 Processing document..."):
        text = extract_text_from_document(filepath)
        doc_type = classify_document(text)
        info = extract_information(text, doc_type)
        score = assess_complexity(info)
        decision = route_claim(info, score)

    st.subheader("📑 Document Type:")
    st.write(doc_type)

    st.subheader("🔍 Extracted Information:")
    st.json(info)

    st.subheader("📊 Complexity Score:")
    st.write(score)

    st.subheader("🔀 Routing Decision:")
    st.json(decision)
