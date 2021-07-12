# Introduction

## Import Lottery

```python
from pancakeswap_lottery import LotteryV2
```

## Create Instance

To retrieve data from the lottery smart-contract, create an instance of the `LotteryV2` class:

```python
lottery = LotteryV2()
```

## Example
```python
from pancakeswap_lottery import LotteryV2

lottery = LotteryV2()

# Lottery draw date and time of lottery round draw
draw_date = lottery.draw_date(lotteryround=16)

# Total prize pool of lottery round
prize_pool = lottery.prize_pool(lotteryround=16)
```

For more examples, see [Examples](examples.md).