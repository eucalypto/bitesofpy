def get_index_different_char(chars):
    chars = [str(char) for char in chars]
    alphanumerics = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    count_of_alphanumerics = 0
    count_of_non_alphanumerics = 0
    for char in chars:
        if char in alphanumerics:
            count_of_alphanumerics += 1
        else:
            count_of_non_alphanumerics += 1
    look_for_alphanumeric = None
    if count_of_alphanumerics == 1:
        look_for_alphanumeric = True
    elif count_of_non_alphanumerics == 1:
        look_for_alphanumeric = False
    else:
        message = f"This should never be reached. Maybe both categories have more than 1 entries? alphanumeric: {count_of_alphanumerics} non-alpha: {count_of_non_alphanumerics}"
        raise AssertionError(message)

    for index, char in enumerate(chars):
        if look_for_alphanumeric == (char in alphanumerics):
            return index


if __name__ == '__main__':
    print(get_index_different_char([",", "", ",", "8"]))
