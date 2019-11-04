import random

MAX_GUESSES = 5
START, END = 1, 20


def get_random_number():
    """Get a random number between START and END, returns int"""
    return random.randint(START, END)


class Game:
    """Number guess class, make it callable to initiate game"""

    def __init__(self):
        """Init _guesses, _answer, _win to set(), get_random_number(), False"""
        self._guesses = set()
        self._answer = get_random_number()
        self._win = False

    def guess(self):
        """Ask user for input, convert to int, raise ValueError outputting
           the following errors when applicable:
           'Please enter a number'
           'Should be a number'
           'Number not in range'
           'Already guessed'
           If all good, return the int"""
        inputstring = input("Guess a number between 1 and 20: ")

        # Check input for validity

        if inputstring == "" or inputstring is None:
            raise ValueError('Please enter a number')

        try:
            number = int(inputstring)
        except ValueError:
            raise ValueError('Should be a number')

        if number < 1 or number > 20:
            raise ValueError('Number not in range')

        if number in self._guesses:
            raise ValueError('Already guessed')

        # checks passed
        self._guesses.add(number)
        return number

    def _validate_guess(self, guess: int) -> bool:
        """Verify if guess is correct, print the following when applicable:
           {guess} is correct!
           {guess} is too low
           {guess} is too high
           Return a boolean"""
        if guess > self._answer:
            print(f"{guess} is too high")
            return False
        elif guess < self._answer:
            print(f"{guess} is too low")
            return False
        elif guess == self._answer:
            print(f"{guess} is correct!")
            return True
        else:
            raise AssertionError("This should never be reached!")

    def __call__(self):
        """Entry point / game loop, use a loop break/continue,
           see the tests for the exact win/lose messaging"""
        while len(self._guesses) < 5:
            try:
                guess = self.guess()
            except ValueError as error:
                print(error)
                continue
            self._win = self._validate_guess(guess)

            if self._win:
                print(f"It took you {len(self._guesses)} guesses")
                break

        if not self._win:
            print(f"Guessed 5 times, answer was {self._answer}")


if __name__ == '__main__':
    game = Game()
    game()
