import re  # <--- THIS IS REQUIRED

def check_password_strength(email, password):
    feedback = []
    
    # Apple Rule: Check if name before @ is in the password
    username = email.split('@')[0].lower()
    if username and username in password.lower():
        feedback.append(f"Password cannot contain your name '{username}'")

    if len(password) < 8:
        feedback.append("Minimum 8 characters required")
    if not any(char.isdigit() for char in password):
        feedback.append("Include at least one number")
    if not any(char.isupper() for char in password):
        feedback.append("Include at least one uppercase letter")

    is_strong = len(feedback) == 0
    return is_strong, feedback