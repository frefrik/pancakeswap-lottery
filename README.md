# PancakeSwap Lottery - Web3 client

A Python client for accessing [PancakeSwap Lottery](https://pancakeswap.finance/lottery) smart contract information through [Web3.py](https://github.com/ethereum/web3.py).


## Install
```
pip install pancakeswap-lottery
```

## Usage
```python
from pancakeswap_lottery import Lottery

lottery = Lottery()
```

<details>
    <summary><b>Current Lottery queries (realtime)</b></summary>

- [Issue Index](#issue-index)
- [Total Amount](#total-amount)
- [Allocation](#allocation)
- [Total Addresses](#total-addresses)
- [Drawed](#drawed)
- [Drawing Phase](#drawing-phase)
- [Last Timestamp](#last-timestamp)
</details>
<details>
    <summary><b>Past Lottery queries (using issue index)</b></summary>

- [Total rewards](#total-rewards)
- [History Numbers](#history-numbers)
- [History Amount](#history-amount)
- [Matching Reward Amount](#matching-reward-amount)
</details>
<details>
    <summary><b>Past Lottery queries (using tokenid)</b></summary>

- [Lottery Numbers](#lottery-numbers)
- [Reward View](#reward-view)
</details>
<details>
    <summary><b>Misc.</b></summary>

- [Max Number](#max-number)
- [Min Price](#min-price)
- [Cake](#cake)
- [LotteryNFT](#lotterynft)
- [Balance Of](#balance-of)
</details>

---
### Current Lottery queries (realtime)
#### Issue Index
Current lottery round
```python
>>> lottery.get_issue_index()
435
```

#### Total Amount
Total pot (CAKE) of current lottery round
```python
>>> lottery.get_total_amount()
34977.25
```

#### Allocation
Prize pool allocation (percent)
```python
>>> lottery.get_allocation()
{'1': 50, '2': 20, '3': 10}
```

#### Total Addresses
```python
>>> lottery.get_total_addresses()
200
```

#### Drawed
True if currenty lottery round is drawed
```python
>>> lottery.get_drawed()
False
```

#### Drawing Phase
True if currenty lottery round is in drawing phase
```python
>>> lottery.get_drawing_phase()
False
```

#### Last Timestamp

```python
>>> lottery.get_last_timestamp(epoch=False)
2021-03-27 11:38:49
```

### Past Lottery queries (using issue index)


#### Total rewards
Total pot (CAKE)
```python
>>> lottery.get_total_rewards(432)
51384.125
```

#### History Numbers
Winning numbers of lottery round
```python
>>> lottery.get_history_numbers(432)
[2, 13, 7, 3]
```

#### History Amount
Numbers of tickets matched
```python
>>> lottery.get_history_amount(432)
{'4': 1, '3': 34, '2': 718}
```

#### Matching Reward Amount
Numers of tickets matched a specified number
```python
>>> lottery.get_matching_reward_amount(432, 3)
34
```

### Past Lottery queries (using tokenid)

#### Lottery Numbers
Lottery numbers for a given ticket
```python
>>> lottery.get_lottery_numbers(1328060)
[11, 5, 14, 6]
```

#### Reward View
Rewards for a given ticket
```python
>>> lottery.get_reward_view(1328060)
0
```


### Misc.

#### Max Number
```python
>>> lottery.get_max_number()
14
```

#### Min Price
Price for one ticket (CAKE)
```python
>>> lottery.get_min_price()
1
```
#### Cake
CAKE contract address
```python
>>> lottery.get_cake()
0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82
```

#### LotteryNFT
PLT-token contract address
```python
>>> lottery.get_lotteryNFT()
0x5e74094Cd416f55179DBd0E45b1a8ED030e396A1
```

#### Balance Of
Get total number of tickets bought by a given address
```python
>>> lottery.get_balance_of("0xc13456A34305e9265E907F70f76B1BA6E2055c8B")
2673
```