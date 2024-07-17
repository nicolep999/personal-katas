import random
import string


my_list = string.digits + string.ascii_letters


def user_password(length) -> str:
    user_password = ""
    for _ in range(length):
        user_password += str(random.choice(my_list))
    return user_password


def main():
    while True:
        user_length = int(input("Please choose your desired password length: "))
        user_new_password = user_password(user_length)
        print(user_new_password)


if __name__ == "__main__":
    main()
