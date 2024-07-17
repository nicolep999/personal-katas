def prime_check(int):
    dividers = 1
    for number in range(2, int):
        if int % number == 0:
            dividers += 1
        if dividers > 2:
            print(f"{int} is not a prime number")
            return None
    print(f"{int} is a prime number")


prime_check(27)
prime_check(47)
