import pytest

from pancakeswap_lottery import Lottery

lottery = Lottery()


@pytest.fixture
def tokenid():
    return 1328060


@pytest.fixture
def issue_index():
    return 434


@pytest.fixture
def address():
    return "0xc13456A34305e9265E907F70f76B1BA6E2055c8B"


def test_w3_is_connected():
    assert lottery.w3.is_connected()


def test_get_last_timestamp():
    r = lottery.get_last_timestamp()
    assert r


def test_get_history_numbers(issue_index):
    r = lottery.get_history_numbers(issue_index)
    assert r


def test_get_lottery_date(issue_index):
    r = lottery.get_lottery_date(issue_index)
    assert r


def test_get_balance_of(address):
    r = lottery.get_balance_of(address)
    assert r
