def get_profile(name, age, *sports, **awards):
    """Returns profile as dict and makes checks beforehand."""
    # Checks:
    if not isinstance(age, int):
        raise ValueError("Age is not an int")
    if len(sports) > 5:
        raise ValueError("Please give no more than 5 sports")

    profile = {'name': name,
               'age': age}
    if sports:  # if sports not empty
        profile['sports'] = list(sorted(sports))

    if awards:  # if awards not empty
        profile['awards'] = awards

    return profile
