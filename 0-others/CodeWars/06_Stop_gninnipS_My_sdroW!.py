# https://www.codewars.com/kata/5264d2b162488dc400000001/
def spin_words(sentence) -> str:
    my_list = list(map(str, sentence.split()))
    for word in my_list:
        if len(word) >= 5:
            new_word = word[::-1]
            word_index = my_list.index(word)
            my_list[word_index] = new_word
    return " ".join(my_list)


print(spin_words("Hey fellow warriors"))
print(spin_words("This is a test"))
print(spin_words("This is another test"))
