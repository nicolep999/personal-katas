def type_check(type_):
    def check(func):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, type_):
                    return "Bad Type"
            return func(*args)

        return wrapper

    return check


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2("Not A Number"))
