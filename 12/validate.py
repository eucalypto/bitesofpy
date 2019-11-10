from collections import namedtuple

User = namedtuple('User', 'name role expired')
USER, ADMIN = 'user', 'admin'
SECRET = 'I am a very secret token'

julian = User(name='Julian', role=USER, expired=False)
bob = User(name='Bob', role=USER, expired=True)
pybites = User(name='PyBites', role=ADMIN, expired=False)
USERS = (julian, bob, pybites)

# define exception classes here


class UserAccessExpired(Exception):
    pass


class UserNoPermission(Exception):
    pass


class UserDoesNotExist(Exception):
    pass


def get_secret_token(username):
    if username not in [user.name for user in USERS]:
        raise UserDoesNotExist

    this_user = None
    for user in USERS:
        if user.name == username:
            this_user = user
            break

    if this_user.expired:
        raise UserAccessExpired

    if not this_user.role == ADMIN:
        raise UserNoPermission

    return SECRET
