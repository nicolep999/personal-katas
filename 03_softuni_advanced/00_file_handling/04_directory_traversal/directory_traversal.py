import os


def create_report_file(directory, storage):
    with open(os.path.join(directory, "report.txt"), "w") as file:
        for extension, files in sorted(storage.items()):
            file.write(f".{extension}\n")
            for f in sorted(files):
                file_path = os.path.join(directory, f)
                file.write(f"- - - {f}\n")


def main():
    storage = {}
    directory = "../04_directory_traversal/"

    for file in os.listdir(directory):
        f = os.path.join(directory, file)
        if os.path.isfile(f):
            file_extension = file.split(".")[-1]
            if file_extension not in storage:
                storage[file_extension] = []
            storage[file_extension].append(file)

        else:
            for sub_file in os.listdir(f):
                sub_file_path = os.path.join(f, sub_file)
                if os.path.isfile(sub_file_path):
                    file_extension = sub_file.split(".")[-1]
                    if file_extension not in storage:
                        storage[file_extension] = []
                    storage[file_extension].append(sub_file)

    create_report_file(directory, storage)


if __name__ == "__main__":
    main()
