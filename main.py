import re


def check_password_strength(password):
    # Initialize score and feedback list
    score = 0
    feedback = []

    # Check password length
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    else:
        score += 1

    # Check for lowercase letters
    if not re.search(r'[a-z]', password):
        feedback.append("Password should include at least one lowercase letter.")
    else:
        score += 1

    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        feedback.append("Password should include at least one uppercase letter.")
    else:
        score += 1

    # Check for digits
    if not re.search(r'\d', password):
        feedback.append("Password should include at least one digit.")
    else:
        score += 1

    # Check for special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("Password should include at least one special character.")
    else:
        score += 1

    # Provide feedback based on the score
    if score == 5:
        return "Password is strong!", feedback
    elif 3 <= score < 5:
        return "Password is moderate.", feedback
    else:
        return "Password is weak.", feedback


def main():
    # Get the user's password input
    password = input("Enter your password to check its strength: ")

    # Check the password strength
    strength, feedback = check_password_strength(password)

    # Print the strength result
    print(f"\nPassword Strength: {strength}")

    # Print any feedback provided
    if feedback:
        print("Feedback to improve your password:")
        for suggestion in feedback:
            print(f"- {suggestion}")


if __name__ == "__main__":
    main()
