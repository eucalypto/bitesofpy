import itertools


def friends_teams(friends, team_size=2, order_does_matter=False):
    if order_does_matter:
        return itertools.permutations(friends, team_size)

    return itertools.combinations(friends, team_size)


if __name__ == '__main__':
    friends = "Gandalf, Gimli, Aragorn, Legolas".split(", ")
    for team in friends_teams(friends):
        print(team)

    print("Order does matter:")
    for team in friends_teams(friends, order_does_matter=True):
        print(team)
