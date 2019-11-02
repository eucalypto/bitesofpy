def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    with open(file_) as file:
        lines = file.readlines()

    character_count = 0
    for line in lines:
        character_count += len(line)

    line_count = len(lines)

    word_count = 0
    for line in lines:
        word_count += len(line.split())

    return f"{line_count}    {word_count}    {character_count} {file_}"


if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))
