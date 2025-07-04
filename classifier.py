
def classify_document(text):
    text_lower = text.lower()
    if "diagnosis" in text_lower or "treatment" in text_lower:
        return "medical_claim"
    elif "vehicle" in text_lower or "accident" in text_lower:
        return "vehicle_claim"
    elif "property" in text_lower:
        return "property_claim"
    else:
        return "generic_claim"
