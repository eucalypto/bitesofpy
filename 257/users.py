def get_users(passwd: str) -> dict:
    """Split password output by newline,
      extract user and name (1st and 5th columns),
      strip trailing commas from name,
      replace multiple commas in name with a single space
      return dict of keys = user, values = name.
    """
    def sanitize(name):
        if name == '':
            return 'unknown'
        return ' '.join(part for part in name.strip(',').split(',') if part != '')
        # I don't like this solution because it has some python trickery that is not plain

    lines = [line.split(':') for line in passwd.strip().splitlines()]
    return {user: sanitize(name) for user, _, _, _, name, *_ in lines}
