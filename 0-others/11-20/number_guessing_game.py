import random


def main():
    print("Welcome to the number guessing game!")
    print("1. Easy")
    print("2. Hard")
    user_difficulty = input("Choose a difficulty. Type 1 or 2: ")
    while user_difficulty != "1" and user_difficulty != "2":
        user_difficulty = input("Choose a difficulty. Type 1 or 2: ")
    guesses = 0
    has_won = False
    if user_difficulty == "1":
        guesses = 10
    elif user_difficulty == "2":
        guesses = 5
    current_number = generate_number()
    print(current_number)
    while guesses > 0:
        user_guess = int(input("Guess a number: "))
        if user_guess == current_number:
            print(
                f"{current_number} is the number, you guessed correctly in {guesses} guesses!"
            )
            has_won = True
            break
        guesses -= 1
    if not has_won:
        print(f"Sorry, you lose! The number was {current_number}!")


def generate_number() -> int:
    return random.randint(1, 100)


if __name__ == "__main__":
    main()
