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
print(lottery_date)
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