def concatenate(*args, **kwargs):
    end_result = ""
    for arg in args:
        end_result += arg
    for key, value in kwargs.items():
        if key in end_result:
            end_result = end_result.replace(key, value)
    return end_result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java="Java"))
