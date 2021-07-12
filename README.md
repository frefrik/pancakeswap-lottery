# PancakeSwap Lottery 🥞 - Web3 client

![PyPI version](https://img.shields.io/pypi/v/pancakeswap-lottery)
![PyPI downloads](https://img.shields.io/pypi/dm/pancakeswap-lottery)
![Licence](https://img.shields.io/github/license/frefrik/pancakeswap-lottery)
![Python version](https://img.shields.io/pypi/pyversions/pancakeswap-lottery)

A Python client for accessing [PancakeSwap Lottery](https://pancakeswap.finance/lottery) smart contract information through [Web3.py](https://github.com/ethereum/web3.py).

---

**Documentation**: https://frefrik.github.io/pancakeswap-lottery

**Examples**: https://frefrik.github.io/pancakeswap-lottery/guide/examples

**Source Code**: https://github.com/frefrik/pancakeswap-lottery

**PyPI**: https://pypi.org/project/pancakeswap-lottery

---

## Installation
Install from [PyPI](https://pypi.org/project/pancakeswap-lottery/):
```
pip install pancakeswap-lottery
```

## Usage
```python
from pancakeswap_lottery import LotteryV2

lottery = LotteryV2()

# Current lottery round number
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
status = lottery.status(lotteryround=10)
draw_date = lottery.draw_date(lotteryround=10)
ticket_price = lottery.ticket_price(lotteryround=10)
prize_pool = lottery.prize_pool(lotteryround=10)
allocation = lottery.prize_pool_allocation(lotteryround=10)
```

### Response previews
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

>>> lottery.ticket_winnings(lotteryround=15, ticketid=567093)
865.536634168

>>> lottery.address_winnings("0x621D6ee5FA9634d86396C13fAaD6A7827606A6d7", lotteryround=16)
{'tickets': 8, 'ticketids': [634970, 634971, 634972, 634973, 634974, 634975, 634976, 634977], 'winning_tickets': [634970, 634971]}

 >>> lottery.winning_numbers(lotteryround=16)
743350

>>> lottery.winners_per_bracket(lotteryround=16)
{'match_1': 19133, 'match_2': 1921, 'match_3': 188, 'match_4': 21, 'match_5': 1, 'match_6': 1}

>>> lottery.cake_per_bracket(lotteryround=16)
{'match_1': 0, 'match_2': 3, 'match_3': 62, 'match_4': 925, 'match_5': 38843, 'match_6': 77687}

>>> lottery.winning_probability()
{'match_1': 10.0, 'match_2': 1.0, 'match_3': 0.1, 'match_4': 0.01, 'match_5': 0.001, 'match_6': 0.0001}
```

<details>
<summary>Lottery V1</summary>

## Usage (Lottery V1)
```python
from pancakeswap_lottery import Lottery

lottery = Lottery()

# Current lottery round
issue_index = lottery.get_issue_index()

# Total pot (CAKE) of current lottery round
total_amount = lottery.get_total_amount()

# Prize pool allocation (percent)
allocation = lottery.get_allocation()

# Total addresses
total_addresses = lottery.get_total_addresses()

# Drawed 
drawed = lottery.get_drawed()

# Drawing phase
drawing_phase = lottery.get_drawing_phase()

# Last timestamp
timestamp = lottery.get_last_timestamp(epoch=False)

# Date and time of lottery round
lottery_date = lottery.get_lottery_date(432)

# Total rewards of lottery round
total_rewards = lottery.get_total_rewards(432)

# Winning numbers of lottery round
history_numbers = lottery.get_history_numbers(432)

# Numbers of tickets matched
history_amount = lottery.get_history_amount(432)

# Numers of tickets matched a specified number
matching_reward_amount = lottery.get_matching_reward_amount(432, 3)

# Lottery numbers for a given ticket
lottery_numbers = lottery.get_lottery_numbers(1328060)

# Rewards for a given ticket
reward_view = lottery.get_reward_view(1328060)

# Max number
max_number = lottery.get_max_number()

# CAKE contract address
cake_contract = lottery.get_cake()

# PLT-token contract address
lottery_contract = lottery.get_lotteryNFT()

# Total number of tickets bought by a given address
balance = lottery.get_balance_of("0xc13456A34305e9265E907F70f76B1BA6E2055c8B")
```

### Response previews (Lottery V1)
```python
>>> lottery.get_issue_index()
435

>>> lottery.get_total_amount()
34977.25

>>> lottery.get_allocation()
{'1': 50, '2': 20, '3': 10}

>>> lottery.get_total_addresses()
200

>>> lottery.get_drawed()
False

>>> lottery.get_drawing_phase()
False

>>> lottery.get_last_timestamp(epoch=False)
2021-03-27 11:38:49

>>> lottery.get_lottery_date(432)
2021-03-26 02:00:00+00:00

>>> lottery.get_total_rewards(432)
51384.125

>>> lottery.get_history_numbers(432)
[2, 13, 7, 3]

>>> lottery.get_history_amount(432)
{'4': 1, '3': 34, '2': 718}

>>> lottery.get_matching_reward_amount(432, 3)
34

>>> lottery.get_lottery_numbers(1328060)
[11, 5, 14, 6]

>>> lottery.get_reward_view(1328060)
0

>>> lottery.get_max_number()
14

>>> lottery.get_min_price()
1

>>> lottery.get_cake()
0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82

>>> lottery.get_lotteryNFT()
0x5e74094Cd416f55179DBd0E45b1a8ED030e396A1

>>> lottery.get_balance_of("0xc13456A34305e9265E907F70f76B1BA6E2055c8B")
2673
```
</details>

## Donate
If you found this library useful and want to support my work feel free to donate a small amount 🙏🏻

- 🥞 CAKE: 0xCFad66049e2C9Bc28647B2e2e3449B6B7C602d42
- Ξ ETH: 0x7E916c46157f012Fb8dece4A042Dc603e8d627Df
- ₿ BTC: bc1qgn2mdf5wsxft33s3ea8sh060y85mzntzs8cuu7

## License

This project is licensed under the terms of the MIT license.

## Disclaimer

This project is not affiliated with the PancakeSwap team.