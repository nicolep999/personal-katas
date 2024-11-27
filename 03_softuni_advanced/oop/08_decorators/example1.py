def hello_function():

    def say_hi():
        return "Hi"

    return say_hi


result = hello_function()  # Making reference
print(result())  # calling say_hi function


def print_message(message):

    def message_sender():
        print(message)

    message_sender()
