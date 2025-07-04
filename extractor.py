# app/extractor.py
import re

def extract_information(text, doc_type):
    info = {}
    
    # Sample extractions using regex
    name_match = re.search(r"Name:\s*(.*)", text)
    policy_match = re.search(r"Policy\s*ID:\s*(\w+)", text)
    amount_match = re.search(r"Amount:\s*\$?([\d,\.]+)", text)

    info["name"] = name_match.group(1).strip() if name_match else "Unknown"
    info["policy_id"] = policy_match.group(1).strip() if policy_match else "Unknown"
    info["claim_amount"] = amount_match.group(1).strip() if amount_match else "0"

    return info
