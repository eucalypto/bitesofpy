import string
import secrets


def gen_key(parts=4, chars_per_part=8):
    alphabet = string.ascii_uppercase + string.digits
    return '-'.join(
        [''.join(
            [secrets.choice(alphabet) for _ in range(chars_per_part)]
        ) for _ in range(parts)
        ]
    )


if __name__ == '__main__':
    print(gen_key())
    print(gen_key(parts=2, chars_per_part=3))
