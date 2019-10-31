def fizzbuzz(num):
    words = []
    if num % 3 == 0:
        words.append("Fizz")
    if num % 5 == 0:
        words.append("Buzz")
    if words != []:
        return " ".join(words)
    else:
        return num
