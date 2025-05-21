import re

def check_password_strength(password: str) -> dict:
    """
    Check if a password meets strength requirements.
    
    Args:
        password (str): Password to check
        
    Returns:
        dict: Dictionary containing strength check results and suggestions
    """
    result = {
        "is_strong": False,
        "has_uppercase": False,
        "has_lowercase": False,
        "has_digit": False,
        "has_special": False,
        "is_long_enough": False,
        "suggestions": []
    }
    
    # Check length (minimum 8 characters)
    if len(password) >= 8:
        result["is_long_enough"] = True
    else:
        result["suggestions"].append("Password should be at least 8 characters long")
    
    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        result["has_uppercase"] = True
    else:
        result["suggestions"].append("Add uppercase letters")
    
    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        result["has_lowercase"] = True
    else:
        result["suggestions"].append("Add lowercase letters")
    
    # Check for digits
    if re.search(r'\d', password):
        result["has_digit"] = True
    else:
        result["suggestions"].append("Add numbers")
    
    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        result["has_special"] = True
    else:
        result["suggestions"].append("Add special characters")
    
    # Password is strong if it meets all criteria
    result["is_strong"] = all([
        result["has_uppercase"],
        result["has_lowercase"],
        result["has_digit"],
        result["has_special"],
        result["is_long_enough"]
    ])
    
    return result

# Example usage
if __name__ == "__main__":
    test_passwords = [
        "weakpass",
        "StrongPass123",
        "VeryStrongPass123!",
        "12345678",
        "Password123!"
    ]
    
    for password in test_passwords:
        result = check_password_strength(password)
        print(f"\nPassword: {password}")
        print(f"Is strong: {result['is_strong']}")
        if not result['is_strong']:
            print("Suggestions:")
            for suggestion in result['suggestions']:
                print(f"- {suggestion}") 