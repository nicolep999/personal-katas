def main():

    n_of_electrons = int(input())
    shells_list = []
    shells_position = 1

    while n_of_electrons > 0:

        current_electrons = 2 * shells_position**2

        if current_electrons > n_of_electrons:
            shells_list.append(n_of_electrons)
            break

        n_of_electrons -= current_electrons

        shells_list.append(current_electrons)

        shells_position += 1
    print(shells_list)


main()
