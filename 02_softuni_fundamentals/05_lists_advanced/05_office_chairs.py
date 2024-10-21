def main():
    number_of_rooms = int(input())
    have_enough = True
    free_chairs = 0

    for room in range(number_of_rooms):

        user_input = list(map(str, input().split()))

        n_chairs = len(user_input[0])
        n_visitors = int(user_input[1])

        if n_chairs < n_visitors:
            print(f"{n_visitors - n_chairs} more chairs needed in room {room + 1}")
            have_enough = False
        if n_chairs > n_visitors:
            free_chairs += n_chairs - n_visitors

    if have_enough:
        print(f"Game On, {free_chairs} free chairs left")


main()
