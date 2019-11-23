from contextlib import contextmanager

class Account:

    def __init__(self):
        self._transactions = []

    @property
    def balance(self):
        return sum(self._transactions)

    def __add__(self, amount):
        self._transactions.append(amount)

    def __sub__(self, amount):
        self._transactions.append(-amount)

    # add 2 dunder methods here to turn this class 
    # into a 'rollback' context manager

    # I knew already that you can define a function as a context manager using
    # @contextlib.contextmanager decorator. Now I know that you also can define
    # your own class as context manager.
    # See https://docs.python.org/3.7/reference/datamodel.html#with-statement-context-managers

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        while self.balance < 0:
            self._transactions.pop()
