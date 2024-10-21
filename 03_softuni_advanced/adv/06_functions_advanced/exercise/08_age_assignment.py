def age_assignment(*args, **kwargs):
    result = {x: 0 for x in args}
    for key, value in result.items():
        if key[0] in kwargs:
            result[key] = kwargs[key[0]]
    final_result = [
        f"{name} is {age} years old."
        for name, age in sorted(result.items(), key=lambda x: x[0])
    ]
    return "\n".join(final_result)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
