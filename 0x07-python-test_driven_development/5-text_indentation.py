#!/usr/bin/python3
"""text_indentation mdoule
"""


def text_indentation(text):
    """text_indentation function
        prints a text with 2 new lines after each of these
        characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    should_print = True

    for iter, character in enumerate(text):

        if character == " ":
            if iter == 0 or not should_print:
                should_print = False
                continue
            else:
                print(character, end="")
                continue

        if character == "." or character == "?" or character == ":":
            print(character)
            print("")
            should_print = False
            continue

        should_print = True
        print(character, end="")
