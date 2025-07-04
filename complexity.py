
def assess_complexity(info):
    score = 0

    if info["name"] == "Unknown":
        score += 3
    if info["policy_id"] == "Unknown":
        score += 2
    if info["claim_amount"] == "0":
        score += 5

    return score  
