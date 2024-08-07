import random


def main():
    print("Welcome to the number guessing game!")
    print("1. Easy")
    print("2. Hard")
    user_difficulty = int(input("Choose a difficulty. Type 1 or 2: "))
    while user_difficulty != 1 and user_difficulty != 2:
        user_difficulty = input("Choose a difficulty. Type 1 or 2: ")
    current_number = generate_number()
    print(current_number)
    game_controller(current_number, user_difficulty)


def game_controller(current_number, difficulty):
    guesses = 10 if difficulty == 1 else 5
    has_won = False
    while guesses > 0:
        user_guess = int(input("Guess a number: "))
        if user_guess == current_number:
            print(
                f"{current_number} is the number, you guessed correctly in {guesses} guesses!"
            )
            has_won = True
            break
        if guesses - 1 == 0:
            break
        elif user_guess < current_number:
            print(f"Your guess is too low. {guesses - 1} guesses left.")
        elif user_guess > current_number:
            print(f"Your guess is too high. {guesses - 1} guesses left.")
        guesses -= 1
    if not has_won:
        print(f"Sorry, you lost! The number was {current_number}.")


def generate_number() -> int:
    return random.randint(1, 100)


if __name__ == "__main__":
    main()
