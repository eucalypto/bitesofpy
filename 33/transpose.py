from collections import namedtuple


def transpose(data):
    """Transpose a data structure
    1. dict
    data = {'2017-8': 19, '2017-9': 13}
    In:  transpose(data)
    Out: [('2017-8', '2017-9'), (19, 13)]

    2. list of (named)tuples
    data = [Member(name='Bob', since_days=60, karma_points=60,
                   bitecoin_earned=56),
            Member(name='Julian', since_days=221, karma_points=34,
                   bitecoin_earned=78)]
    In: transpose(data)
    Out: [('Bob', 'Julian'), (60, 221), (60, 34), (56, 78)]
    """
    if type(data) is dict:
        # Convert dict entries into tuples
        data = data.items()

    return zip(*data)


def testing():
    mydict = {'2017-8': 19, '2017-9': 13}
    enumerate(mydict)
    # for i in zip(*mydict.items()):
    #     print(i)
    print(list(zip(*mydict.items())))

    Member = namedtuple("Member", "name, since, karma, bitecoins")
    gandalf = Member("Gandalf", "1319-03", 13_332, 1000)
    print(gandalf)
    # print(gandalf._fields)
    print(gandalf[1])
    print(len(gandalf))
    # print(enumerate(gandalf))
    print(list(zip(gandalf, gandalf)))

    print(transpose([gandalf]))

    # for item in transpose([gandalf]):
    #     for data in item:
    #         print(data)


if __name__ == '__main__':
    testing()
