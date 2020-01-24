def find_number_pairs(numbers, N=10):
    complements = {round(N - number, 2): number for number in numbers}
    pairs = set()
    for number in numbers:
        if number in complements.keys():
            if number == complements.get(number):
                continue
            pairs.add(tuple(sorted((number, complements.get(number)))))
    return list(pairs)
