from pancakeswap_lottery import Lottery

lottery = Lottery()


print("lottery.get_total_rewards(435):", lottery.get_total_rewards(435))


print("lottery.get_history_numbers(435):", lottery.get_history_numbers(435))


print("lottery.get_history_amount(435):", lottery.get_history_amount(435))


print(
    "lottery.get_matching_reward_amount(435):",
    lottery.get_matching_reward_amount(435, 3),
)

print('min_price', lottery.get_min_price())

print(lottery.get_drawed())

print(lottery.get_drawing_phase())


print(lottery.get_lottery_numbers(1341840))

print(lottery.get_reward_view(1341840))


print(lottery.get_issue_index())


print(lottery.get_last_timestamp(epoch=False))

print(lottery.get_max_number())


print("get_total_addresses")
print(lottery.get_total_addresses())


print(lottery.get_total_amount())

alloc = lottery.get_allocation()

print("lottery.get_allocation():", alloc)


print(lottery.get_cake())


print(lottery.get_lotteryNFT())


print(lottery.get_balance_of("0xAA0C8d29E5b1B1ab774A10d4e85f112A4c823879"))


lottery_date = lottery.get_lottery_date(470)
print("lottery_date:", lottery_date)
