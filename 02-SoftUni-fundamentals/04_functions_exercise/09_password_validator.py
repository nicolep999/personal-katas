def password_validator(password):
    is_valid = True

    if not (6 <= len(password) <= 10):
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not password.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    digit_count = sum(1 for char in password if char.isdigit())
    if digit_count < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print("Password is valid")


user_input = input()
password_validator(user_input)
