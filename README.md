# PancakeSwap Lottery - Web3 client

A Python client for accessing [PancakeSwap Lottery](https://pancakeswap.finance/lottery) smart contract information through Web3.py.

## Documentation
```python
from pancakeswap_lottery import Lottery

lottery = Lottery()
```

### Current lottery
#### get_issue_index
```python
>>> lottery.get_issue_index()
435
```

#### get_total_amount (Prize pool)
```python
>>> lottery.get_total_amount()
34977.25
```

#### get_allocation (Prize pool allocation)
```python
>>> lottery.get_allocation()
{'1': 50, '2': 20, '3': 10}
```

#### get_total_addresses
```python
>>> lottery.get_total_addresses()
200
```

#### get_drawed
```python
>>> lottery.get_drawed()
False
```

#### get_drawing_phase
```python
>>> lottery.get_drawing_phase()
False
```

#### get_last_timestamp
```python
>>> lottery.get_last_timestamp(epoch=False)
2021-03-27 11:38:49
```

### Past lotteries (with issue index)

#### get_total_rewards (Prize pool)
```python
>>> lottery.get_total_rewards(432)
51384.125
```

#### get_history_numbers
```python
>>> lottery.get_history_numbers(432)
[2, 13, 7, 3]
```

#### get_history_amount (Numers of tickets matched)
```python
>>> lottery.get_history_amount(432)
{'4': 1, '3': 34, '2': 718}
```

#### get_matching_reward_amount
```python
>>> lottery.get_matching_reward_amount(432, 3)
34
```

### Past lotteries (with tokenid)
#### get_lottery_numbers
```python
>>> lottery.get_lottery_numbers(1328060)
[11, 5, 14, 6]
```

#### get_reward_view
```python
>>> lottery.get_reward_view(1328060)
0
```

### Lottery metadata
#### get_max_number
```python
>>> lottery.get_max_number()
14
```

#### get_min_price
```python
>>> lottery.get_min_price()
1
```

### Other
#### get_cake (CAKE contract address)
```python
>>> lottery.get_cake()
0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82
```

#### get_lotteryNFT (PLT-token contract address)
```python
>>> lottery.get_lotteryNFT()
0x5e74094Cd416f55179DBd0E45b1a8ED030e396A1
```

#### get_balance_of(address)
```python
>>> lottery.get_balance_of("0xc13456A34305e9265E907F70f76B1BA6E2055c8B")
2673
```