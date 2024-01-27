import pytest

from transactions import process_transactions


def test_xxxxx():
    result = process_transactions([{"amount": 5, "type": "credit"},{"amount": 5, "type": "credit"}])
    assert result == 10



def test_input_not_a_dict():
    with pytest.raises(ValueError):
        process_transactions([-1])

def test_invalid_transaction_type():
    with pytest.raises(ValueError):
        process_transactions([{"amount": 5, "type": "jablko"}])


def test_invalid_transaction_amount():
    with pytest.raises(ValueError):
        process_transactions([{"amount": "kot", "type": "debit"}])


def test_insufficient_debit_transaction():
    with pytest.raises(ValueError):
        process_transactions([{"amount": 10, "type": "debit"}])


def test_invalid_transaction_account_balance():
    with pytest.raises(ValueError):
        process_transactions([{"amount": "100", "type": "debit"}])


def test_transactions_list_is_empty():
    with pytest.raises(ValueError):
        process_transactions([])


def test_dictionary():
    with pytest.raises(ValueError):
        process_transactions([{"type": "debit"}])


def test_negative_amount():
    with pytest.raises(ValueError):
        process_transactions([{"amount": -10,"type": "credit"}])


def test_amount():
    result = process_transactions([{"amount": 5, "type": "credit"},{"amount": 2, "type": "debit"}])
    assert result == 3

