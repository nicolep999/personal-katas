from string import punctuation, ascii_letters

INPUT_LINES = [
    "-I was quick to judge him, but it wasn't his fault.",
    "-Is this some kind of joke?! Is it?",
    "-Quick, hide here. It is safer.",
]


def create_text_file():
    with open("file.txt", "w") as text_file:
        for line in INPUT_LINES:
            text_file.write(line + "\n")


def main():
    create_text_file()
    with open("file.txt") as text_file:
        lines = text_file.readlines()
        for index, line in enumerate(lines):
            count_letters = 0
            count_punctuation = 0
            for char in line:
                if char in ascii_letters:
                    count_letters += 1
                elif char in punctuation:
                    count_punctuation += 1

            print(
                f"Line {index + 1}: {line.strip()} ({count_letters})({count_punctuation})"
            )


if __name__ == "__main__":
    main()
