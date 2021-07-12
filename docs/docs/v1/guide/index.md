# Introduction

## Import Lottery

```python
from pancakeswap_lottery import Lottery
```

## Create Instance

To retrieve data from the lottery smart-contract, create an instance of the `Lottery` class:

```python
lottery = Lottery()
```

## Example
```python
from pancakeswap_lottery import Lottery

lottery = Lottery()

# Lottery round #432
issue_index = 432

# Date and time of lottery round
lottery_date = lottery.get_lottery_date(issue_index)

# Total rewards of lottery round
total_rewards = lottery.get_total_rewards(issue_index)
```

For more examples, see [Examples](examples.md).