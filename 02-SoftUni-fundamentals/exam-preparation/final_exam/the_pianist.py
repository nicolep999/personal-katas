def main():
    user_collection = []

    initial_pieces = int(input())

    for x in range(initial_pieces):
        values = input().split("|")
        keys = ("piece", "composer", "key")
        # values = (piece, composer, key)
        collection = dict(zip(keys, values))
        user_collection.append(collection)

    while True:

        command = input()

        if command == "Stop":
            for x in user_collection:
                print(f"{x['piece']} -> Composer: {x['composer']}, Key: {x['key']}")
            break

        command = command.split("|")
        piece = command[1]

        if command[0] == "Remove":
            piece_found = False
            for item in user_collection:
                if item["piece"] == piece:
                    user_collection.remove(item)
                    piece_found = True
                    print(f"Successfully removed {piece}!")
                    break
            if not piece_found:
                print(f"Invalid operation! {piece} does not exist in the collection.")
            continue

        if command[0] == "ChangeKey":
            key = command[2]
            in_collection = False

            for item in user_collection:
                if item["piece"] == piece:
                    in_collection = True
                    item["key"] = key
                    print(f"Changed the key of {piece} to {key}!")
            if not in_collection:
                print(f"Invalid operation! {piece} does not exist in the collection.")
            continue

        if command[0] == "Add":
            composer = command[2]
            key = command[3]

            in_collection = False
            for item in user_collection:
                if item["piece"] == piece:
                    print(f"{piece} is already in the collection!")
                    in_collection = True
            if not in_collection:
                keys = ("piece", "composer", "key")
                values = (piece, composer, key)
                collection = dict(zip(keys, values))
                user_collection.append(collection)
                print(f"{piece} by {composer} in {key} added to the collection!")
            continue


main()
