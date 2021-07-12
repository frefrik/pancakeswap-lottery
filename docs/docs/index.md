<p align="center">
    <img src="img/pancake-lottery.png" title="Image credit: https://pancakeswap.medium.com" alt="Image credit: https://pancakeswap.medium.com" />
</p>
<p align="center">
    <em>Python client for accessing <a href="https://pancakeswap.finance/lottery" target="_blank">PancakeSwap Lottery</a> smart contract information through <a href="https://github.com/ethereum/web3.py" target="_blank">Web3.py</a></em>
</p>
<p align="center">
    <a href="https://pypi.org/project/pancakeswap-lottery" target="_blank">
        <img src="https://img.shields.io/pypi/v/pancakeswap-lottery" alt="PyPI version">
    </a>
    <img src="https://img.shields.io/pypi/dm/pancakeswap-lottery" alt="PyPI downloads">
    <img src="https://img.shields.io/github/license/frefrik/pancakeswap-lottery" alt="Licence">
    <img src="https://img.shields.io/pypi/pyversions/pancakeswap-lottery" alt="Python version">
</p>

---

**Documentation**: <a target="_blank" href="https://frefrik.github.io/pancakeswap-lottery">https://frefrik.github.io/pancakeswap-lottery</a>

**Examples**: <a target="_blank" href="https://frefrik.github.io/pancakeswap-lottery/guide/examples">https://frefrik.github.io/pancakeswap-lottery/guide/examples</a>

**Source Code**: <a target="_blank" href="https://github.com/frefrik/pancakeswap-lottery">https://github.com/frefrik/pancakeswap-lottery</a>

**PyPI**: <a target="_blank" href="https://pypi.org/project/pancakeswap-lottery">https://pypi.org/project/pancakeswap-lottery</a>

---

## Overview

pancakeswap-lottery is a python interface to PancakeSwap Lottery smart contract endpoints.

## Requirements

Python 3.8+

- [Web3.py](https://github.com/ethereum/web3.py) - A python interface for interacting with the Ethereum blockchain and ecosystem.

## Installation

<div class="termynal" data-termynal data-ty-typeDelay="40" data-ty-lineDelay="700">
    <span data-ty="input">pip install pancakeswap-lottery</span>
    <span data-ty="progress"></span>
    <span data-ty>Successfully installed pancakeswap-lottery</span>
    <a href="#" data-terminal-control="">restart ↻</a>
</div>

## Usage
=== "Example"
    ```python
    from pancakeswap_lottery import LotteryV2

    lottery = LotteryV2()

    # Get current lottery round number
    current_round = lottery.current_round()

    # Current ticket id
    ticketid = lottery.current_ticket()

    # Status of lottery round
    status = lottery.status()

    # Lottery draw date and time of lottery round
    draw_date = lottery.draw_date()

    # Ticket price in CAKE
    ticket_price = lottery.ticket_price()

    # Total prize pool of lottery round in CAKE
    prize_pool = lottery.prize_pool()

    # Prize pool allocation in CAKE
    allocation = lottery.prize_pool_allocation()

    # Winning numbers for lottery round
    winning_numbers = lottery.winning_numbers(lotteryround=16)

    # Get lottery winnings (CAKE) for a given address and round
    address_winnings = lottery.address_winnings(address="0x621D6ee5FA9634d86396C13fAaD6A7827606A6d7", lotteryround=16)

    # Get lottery winnings (CAKE) for a given ticket and round
    ticket_winnings = lottery.ticket_winnings(lotteryround=10, ticketid=158408)

    # Number of winners per prize bracket
    winners = lottery.winners_per_bracket(lotteryround=16)

    # Amount of CAKE won per ticket in each prize bracket
    cake_per_bracket = lottery.cake_per_bracket(lotteryround=16)

    # Percentage probability of winning the lottery
    winning_probability = lottery.winning_probability()

    # Data from historic lottery rounds can also be pulled
    ticket_price_hist = lottery.ticket_price(lotteryround=10)
    prize_pool_hist = lottery.prize_pool(lotteryround=10)
    allocation_hist = lottery.prize_pool_allocation(lotteryround=10)
    draw_date_hist = lottery.draw_date(lotteryround=10)
    status_hist = lottery.status(lotteryround=10)
    ```

=== "Data"
    ```python
    >>> lottery.current_round()
    20

    >>> lottery.current_ticket()
    1124981

    >>> lottery.status()
    Open

    >>> lottery.draw_date()
    2021-07-12 20:00:00

    >>> lottery.ticket_price()
    0.32

    >>> lottery.prize_pool()
    63024

    >>> lottery.prize_pool_allocation()
    {'match_1': 630, 'match_2': 1891, 'match_3': 3781, 'match_4': 6302, 'match_5': 12605, 'match_6': 25210, 'burn': 12605}

    >>> lottery.winning_numbers(lotteryround=16)
    743350

    >>> lottery.address_winnings("0x621D6ee5FA9634d86396C13fAaD6A7827606A6d7", lotteryround=16)
    {'tickets': 8, 'ticketids': [634970, 634971, 634972, 634973, 634974, 634975, 634976, 634977], 'winning_tickets': [634970, 634971]}

    >>> lottery.ticket_winnings(lotteryround=15, ticketid=567093)
    865.536634168

    >>> lottery.winners_per_bracket(lotteryround=16)
    {'match_1': 19133, 'match_2': 1921, 'match_3': 188, 'match_4': 21, 'match_5': 1, 'match_6': 1}

    >>> lottery.cake_per_bracket(lotteryround=16)
    {'match_1': 0, 'match_2': 3, 'match_3': 62, 'match_4': 925, 'match_5': 38843, 'match_6': 77687}

    >>> lottery.winning_probability()
    {'match_1': 10.0, 'match_2': 1.0, 'match_3': 0.1, 'match_4': 0.01, 'match_5': 0.001, 'match_6': 0.0001}
    ```

## License

This project is licensed under the terms of the MIT license.

## Disclaimer

This project is not affiliated with the PancakeSwap team.