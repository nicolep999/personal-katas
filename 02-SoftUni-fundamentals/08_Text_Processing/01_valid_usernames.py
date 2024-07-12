import string


def password_checker(password) -> bool:
    is_valid = True

    allowed_characters = string.ascii_letters + string.digits + "_" + "-"

    if len(password) < 3 or len(password) > 16:
        is_valid = False

    for letter in password:
        if letter not in allowed_characters:
            is_valid = False

    return is_valid


def main():
    user_input = list(map(str, input().split(", ")))
    allowed_passwords = []
    for password in user_input:
        if password_checker(password):
            allowed_passwords.append(password)
    print(*allowed_passwords, sep="\n")


if __name__ == "__main__":
    main()
