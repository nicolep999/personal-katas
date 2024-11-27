def vowel_filter(function):

    def wrapper():
        result = function()
        return [x for x in result if x in "aeiouy"]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
