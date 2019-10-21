def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    output = ""
    output += string[n:]
    output += string[:n]
    return output

if __name__ == '__main__':
    print(rotate("abcde", 1))
    print(rotate("abcde", -1))
