from collections import deque

INDENTS = 4


def print_hanging_indents(poem: str):
    lines = poem.strip().split("\n")
    lines = map(str.strip, lines)
    formatted_poem = ""
    is_first_line = True
    indent = " " * INDENTS
    for line in lines:
        if line == "":
            is_first_line = True
            continue
        if is_first_line:
            formatted_poem += line + "\n"
            is_first_line = False
        else:
            formatted_poem += indent + line + "\n"
    print(formatted_poem)



if __name__ == '__main__':
    shakespeare_unformatted = """
                              To be, or not to be, that is the question:
                              Whether 'tis nobler in the mind to suffer

                              The slings and arrows of outrageous fortune,
                              Or to take Arms against a Sea of troubles,
                              """

    print_hanging_indents(shakespeare_unformatted)
