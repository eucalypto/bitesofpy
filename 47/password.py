import string

PUNCTUATION_CHARS = list(string.punctuation)

used_passwords = set('PassWord@1 PyBit$s9'.split())


def validate_password(password):
    if len(password) < 6:
        return False
    if len(password) > 12:
        return False

    digits = 0
    lower = 0
    upper = 0
    punctuation = 0
    for char in password:
        if char in string.digits:
            digits += 1
        elif char in string.ascii_lowercase:
            lower += 1
        elif char in string.ascii_uppercase:
            upper += 1
        elif char in PUNCTUATION_CHARS:
            punctuation += 1
    if digits < 1:
        return False
    if lower < 2:
        return False
    if upper < 1:
        return False
    if punctuation < 1:
        return False
    if password in used_passwords:
        return False

    used_passwords.add(password)
    return True




