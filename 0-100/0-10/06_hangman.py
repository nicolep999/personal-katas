from random_word import RandomWords
import pyfiglet

word_list = RandomWords()


def console_art_elements():
    text = "HANGMAN"
    ascii_art = pyfiglet.figlet_format(text)
    print(ascii_art)


def new_word_getter() -> str:
    current_word = word_list.get_random_word()
    return current_word


def main() -> None:
    console_art_elements()
    game_word = new_word_getter()
    current_play_word = "_" * len(game_word)
    player_lives = 7
    while True:
        user_input = input("Choose your letter: ")
        if user_input not in game_word:
            print(f"Letter {user_input} is not in the word")
            player_lives -= 1
            if player_lives == 0:
                print(f"You lose, the word was '{game_word}'")
                break
        else:
            for index in range(len(game_word)):
                if game_word[index] == user_input:
                    temp_word = list(current_play_word)
                    temp_word[index] = user_input
                    current_play_word = "".join(temp_word)
        print(current_play_word)
        if current_play_word == game_word:
            print("You win!")
            break


if __name__ == "__main__":
    main()
