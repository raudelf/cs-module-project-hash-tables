def word_count(s):
    dictionary = {}
    ignored_char = [
        '"', ":", ";", ",", ".", "-", "+", "=", "/", "\\", "|", "[", "]", "{", "}", "(", ")", "*", "^", "&"
    ]

    new_string = s.lower()

    for char in ignored_char:
        new_string = new_string.replace(char, "")

    words = new_string.split()

    if len(words) == 0:
        return dictionary

    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1

    return dictionary


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
