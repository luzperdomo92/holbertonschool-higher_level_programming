#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for iter, character in enumerate(text):
        if (text[iter - 1] == "." or text[iter - 1] == "?" or
                text[iter - 1] == ":") and character == " ":
            continue

        print(character, end="")
        if character == "." or character == "?" or character == ":":
            print("\n")
