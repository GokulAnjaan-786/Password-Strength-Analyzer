def check_strength(password):

    score = 0
    feedback = []

    if len(password) >= 8:
        score += 2
    else:
        feedback.append("Password should contain at least 8 characters.")

    if any(char.isupper() for char in password):
        score += 2
    else:
        feedback.append("Add uppercase letters.")

    if any(char.islower() for char in password):
        score += 2
    else:
        feedback.append("Add lowercase letters.")

    if any(char.isdigit() for char in password):
        score += 2
    else:
        feedback.append("Add numbers.")

    special = "!@#$%^&*()"

    if any(char in special for char in password):
        score += 2
    else:
        feedback.append("Add special symbols.")

    return score, feedback