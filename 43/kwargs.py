def get_profile(*, name="julian", profession="programmer"):
    return f"{name} is a {profession}"


if __name__ == '__main__':
    print(get_profile())
