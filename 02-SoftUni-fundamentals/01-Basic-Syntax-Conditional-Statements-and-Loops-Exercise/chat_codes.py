message_number = int(input())

for _ in range(0, message_number):
    user_message = int(input())
    if user_message == 88:
        print('Hello')
    elif user_message == 86:
        print('How are you?')
    elif user_message < 88 or user_message == 87:
        print('GREAT!')
    else:
        print('Bye.')
