
def route_claim(info, complexity_score):
    if complexity_score <= 3:
        return {
            "status": "auto_processed",
            "message": "Claim auto-approved and queued for payment."
        }
    else:
        return {
            "status": "needs_human_review",
            "priority_score": complexity_score,
            "message": "Claim forwarded to human reviewer."
        }
