from account import Account
import pytest


# write your pytest functions below, they need to start with test_

def set_up_test_account() -> Account:
    account = Account("Gandalf", 100)
    return account


def test_constructor_default_amount():
    owner = "Gandalf"
    account = Account(owner)
    assert account.owner == owner
    assert account.amount == 0


def test_balance_read_only():
    account = set_up_test_account()
    with pytest.raises(AttributeError):
        account.balance = 4


@pytest.mark.parametrize(
    "difference", [137, -137, 500, 0]
)
def test_balance_correct_amount(difference):
    account = set_up_test_account()
    current_balance = account.balance
    # Add another transaction by hand because here we don't test
    # add_transaction()
    account._transactions.append(difference)
    assert current_balance + difference == account.balance


@pytest.mark.parametrize(
    "amount", ["not an int", 13.4]
)
def test_add_transaction_non_int_amount(amount):
    account = set_up_test_account()
    with pytest.raises(ValueError, match='please use int for amount'):
        assert account.add_transaction(amount)


def test_add_transaction_several_steps():
    account = set_up_test_account()
    amount = account.balance
    for transaction in [10, 1000, -300, 20]:
        account.add_transaction(transaction)
        amount += transaction
        assert amount == account.balance


def test_repr():
    account = set_up_test_account()
    assert "Account('Gandalf', 100)" == repr(account)


def test_str():
    account = set_up_test_account()
    assert "Account of Gandalf with starting amount: 100" == str(account)


def test_len():
    account = set_up_test_account()
    for i in range(10):
        assert len(account) == i
        account.add_transaction(i)


def test_getitem():
    account = set_up_test_account()
    for i in range(10):
        account.add_transaction(i * 1000)
    for i in range(10):
        assert i * 1000 == account[i]


def test_eq():
    account1 = set_up_test_account()
    account2 = set_up_test_account()
    assert account1 == account2


def test_lt_really_less_than():
    account1 = set_up_test_account()
    account2 = set_up_test_account()
    account2.add_transaction(1000)
    assert account1 < account2


def test_lt_actually_equal():
    account1 = Account("Gandalf", 1000)
    account2 = Account("Frodo", 1000)
    assert not account1 < account2


def test_add_should_not_raise_exceptions():
    account1 = Account("Gandalf", 1000)
    account2 = Account("Frodo", 100)
    try:
        account1 + account2
    except Exception:
        assert False


def test_add():
    account1 = Account("Gandalf", 1000)
    account1.add_transaction(3)
    account1.add_transaction(4)
    account2 = Account("Frodo", 100)
    account2.add_transaction(5)
    account3 = account1 + account2
    assert "Gandalf&Frodo" == account3.owner
    assert account3.amount == 1100
    assert len(account3) == len(account1) + len(account2)
