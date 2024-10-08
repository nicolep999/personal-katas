import os


def create_text_file(filename):
    open(filename, "w").close()


def add_content_to_file(file, content):
    with open(file, "a") as text_file:
        text_file.write(content + "\n")


def replace_content_in_file(filename, old_string, new_string):
    try:
        with open(filename, "r+") as text_file:
            content = text_file.read()
            content = content.replace(old_string, new_string)
            text_file.seek(0)
            text_file.write(content)
    except FileNotFoundError:
        print(f"An error occurred")


def delete_file(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        print(f"An error occurred")


def main():

    while True:

        user_input = input()
        if user_input == "End":
            break

        command, filename, *args = user_input.split("-")

        commands_mapper = {
            "Create": lambda: create_text_file(filename),
            "Add": lambda: add_content_to_file(filename, " ".join(args)),
            "Replace": lambda: replace_content_in_file(filename, args[0], args[1]),
            "Delete": lambda: delete_file(filename),
        }

        if command in commands_mapper:
            commands_mapper[command]()
        else:
            print("Invalid command")


if __name__ == "__main__":
    main()
