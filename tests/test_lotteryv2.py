import pytest

from pancakeswap_lottery import LotteryV2

lottery = LotteryV2()


@pytest.fixture
def ticketid():
    return 158408


@pytest.fixture
def lotteryround():
    return 10


@pytest.fixture
def address():
    return "0x621D6ee5FA9634d86396C13fAaD6A7827606A6d7"


def test_w3_is_connected():
    assert lottery.w3.is_connected()


def test_current_ticket():
    r = lottery.current_ticket()
    assert r


def test_prize_pool():
    r = lottery.prize_pool()
    assert r


def test_draw_date():
    r = lottery.draw_date()
    assert r


def test_prize_pool_allocation():
    r = lottery.prize_pool_allocation()
    assert r


def test_ticket_price():
    r = lottery.ticket_price()
    assert r


def test_status():
    r = lottery.status()
    assert r


def test_winners_per_bracket(lotteryround):
    r = lottery.winners_per_bracket(lotteryround)
    assert r


def test_cake_per_bracket(lotteryround):
    r = lottery.cake_per_bracket(lotteryround)
    assert r


def test_winning_probability():
    r = lottery.winning_probability()
    assert r


def test_winning_numbers(lotteryround):
    r = lottery.winning_numbers(lotteryround)
    assert r


def test_ticket_winnings(lotteryround, ticketid):
    r = lottery.ticket_winnings(lotteryround, ticketid)
    assert r


def test_address_winnings(address, lotteryround):
    r = lottery.address_winnings(address, lotteryround)
    assert r
