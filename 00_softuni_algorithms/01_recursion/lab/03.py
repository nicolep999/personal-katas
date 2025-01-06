n = int(input())


def print_figure(n):

    if n <= 0:
        return
    # Pre-action
    print("*" * n)
    print_figure(n - 1)  # Post-action
    print("#" * n)


print_figure(n)
