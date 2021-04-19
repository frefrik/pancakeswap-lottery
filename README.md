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

### Response previews
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

## Donate
If you found this library useful and want to support my work feel free to donate a small amount 🙏🏻

- 🥞 CAKE: 0xCFad66049e2C9Bc28647B2e2e3449B6B7C602d42
- Ξ ETH: 0x7E916c46157f012Fb8dece4A042Dc603e8d627Df
- ₿ BTC: bc1qgn2mdf5wsxft33s3ea8sh060y85mzntzs8cuu7

## License

This project is licensed under the terms of the MIT license.

## Disclaimer

This project is not affiliated with the PancakeSwap team.