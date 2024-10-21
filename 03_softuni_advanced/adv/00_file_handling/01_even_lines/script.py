CHARS = "-,.!?"
INPUT_LINES = [
    "-I was quick to judge him, but it wasn't his fault.",
    "-Is this some kind of joke?! Is it?",
    "-Quick, hide here. It is safer.",
]


def create_text_file():
    """
    Creates file.txt
    Writes input lines to file.txt, with each line on a new line
    """
    with open("file.txt", "w") as text_file:
        for line in INPUT_LINES:
            text_file.write(line + "\n")


def main():
    create_text_file()
    with open("file.txt") as text_file:
        lines = text_file.readlines()
        for index, line in enumerate(lines):
            if index % 2 == 0:
                for x in CHARS:
                    line = line.replace(x, "@")
                print(" ".join(reversed(line.split())))


if __name__ == "__main__":
    main()
