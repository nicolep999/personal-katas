def cache(func):
    result = {}

    def wrapper(n):
        if n in result:
            return result[n]
        result[n] = func(n)
        return result[n]

    wrapper.log = result
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)
print(fibonacci.log)
