NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""
    output = []
    for name in names:
        firstname, lastname = name.split()
        name = firstname.capitalize() + " " + lastname.capitalize()
        if name not in output:
            output.append(name)
        else:
            continue

    return output


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    names.sort(key=lambda x: x.split()[-1], reverse=True)
    return names


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)
    shortest = names[0].split()[0]
    for name in names:
        first_name = name.split()[0]
        if len(first_name) < len(shortest):
            shortest = first_name
    return shortest


if __name__ == '__main__':
    print(dedup_and_title_case_names(NAMES))
    print(sort_by_surname_desc(NAMES))
    print(shortest_first_name(NAMES))
