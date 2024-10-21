class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


pin_code, initial_balance, age = input().split(", ")
initial_balance = float(initial_balance)
age = int(age)

while True:
    command = input()
    if command == "End":
        break

    try:
        command_parts = command.split("#")

        if command_parts[0] == "Send Money":
            amount_to_send = float(command_parts[1])
            entered_pin = command_parts[2]

            if amount_to_send > initial_balance:
                raise MoneyNotEnoughError(
                    "Insufficient funds for the requested transaction"
                )

            if entered_pin != pin_code:
                raise PINCodeError("Invalid PIN code")

            if age < 18:
                raise UnderageTransactionError(
                    "You must be 18 years or older to perform online transactions"
                )

            initial_balance -= amount_to_send
            print(f"Successfully sent {amount_to_send:.2f} money to a friend")
            print(f"There is {initial_balance:.2f} money left in the bank account")

        elif command_parts[0] == "Receive Money":
            amount_to_receive = float(command_parts[1])

            if amount_to_receive < 0:
                raise MoneyIsNegativeError(
                    "The amount of money cannot be a negative number"
                )

            initial_balance += amount_to_receive / 2
            print(
                f"{amount_to_receive / 2:.2f} money went straight into the bank account"
            )

    except (
        MoneyNotEnoughError,
        PINCodeError,
        UnderageTransactionError,
        MoneyIsNegativeError,
    ) as error:
        raise error
