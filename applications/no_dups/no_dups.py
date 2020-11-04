def no_dups(s):
    string_array = []
    final_string = ""

    new_string = s.lower()

    words = new_string.split()

    if len(words) == 0:
        return final_string

    for word in words:
        if word in string_array:
            continue
        else:
            string_array.append(word)
            final_string += word + " "

    return final_string[:-1]


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
