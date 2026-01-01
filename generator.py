import secrets
import string

def generate_password(length=12):
    # Characters to choose from
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*"
    
    # Ensure at least one of each required type to pass the checker
    password = [
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice("!@#$%^&*")
    ]
    
    # Fill the rest
    password += [secrets.choice(alphabet) for _ in range(length - 3)]
    
    # Shuffle so the fixed characters aren't always at the start
    secrets.SystemRandom().shuffle(password)
    
    return "".join(password)