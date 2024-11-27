def upper(function):
    def wrapper(message):
        result = function(message)
        return result.upper()

    return wrapper


@upper
def print_text(message):
    return message


print(print_text("Hello world"))
