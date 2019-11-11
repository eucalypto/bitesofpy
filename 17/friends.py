import itertools


def friends_teams(friends, team_size=2, order_does_matter=False):
    func = itertools.combinations \
        if not order_does_matter \
        else itertools.permutations
    return func(friends, team_size)


if __name__ == '__main__':
    friends = "Gandalf, Gimli, Aragorn, Legolas".split(", ")
    for team in friends_teams(friends):
        print(team)

    print("Order does matter:")
    for team in friends_teams(friends, order_does_matter=True):
        print(team)
