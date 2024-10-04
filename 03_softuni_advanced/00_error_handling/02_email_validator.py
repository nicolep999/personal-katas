class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


while True:
    email = input()

    if email == "End":
        break

    try:
        if email.count("@") != 1:
            raise MustContainAtSymbolError("Email must contain @")

        name, domain_part = email.split("@")
        domain = domain_part.split(".")[-1]

        if len(name) <= 4:
            raise NameTooShortError("Name must be more than 4 characters")

        if domain not in ["com", "bg", "org", "net"]:
            raise InvalidDomainError(
                "Domain must be one of the following: .com, .bg, .org, .net"
            )

        print("Email is valid")

    except (NameTooShortError, MustContainAtSymbolError, InvalidDomainError) as e:
        raise e
