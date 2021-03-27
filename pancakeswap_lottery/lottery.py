import os
import json
from datetime import datetime
from web3 import Web3


def _load_abi(abi_name):
    path = f"{os.path.dirname(os.path.abspath(__file__))}/assets/"
    with open(os.path.abspath(path + f"{abi_name}.abi")) as f:
        abi: str = json.load(f)
    return abi


class Lottery:
    def __init__(self, provider="https://bsc-dataseed1.binance.org:443"):
        self.w3 = Web3(Web3.HTTPProvider(provider))

        contract_addresses = {
            "lottery": "0x3C3f2049cc17C136a604bE23cF7E42745edf3b91",
            "token": "0x5e74094Cd416f55179DBd0E45b1a8ED030e396A1",
        }

        self.lottery_contract = self._load_contract(
            abi_name="lottery", address=contract_addresses["lottery"]
        )

        self.token_contract = self._load_contract(
            abi_name="token", address=contract_addresses["token"]
        )

        self.decimals = 10 ** 18

    def _load_contract(self, abi_name, address):
        return self.w3.eth.contract(address=address, abi=_load_abi(abi_name))

    def get_total_rewards(self, issue_index):
        total_rewards = self.lottery_contract.functions.getTotalRewards(
            issue_index
        ).call()

        return total_rewards / self.decimals

    def get_drawed(self):
        return self.lottery_contract.functions.drawed().call()

    def get_drawing_phase(self):
        return self.lottery_contract.functions.drawingPhase().call()

    def get_matching_reward_amount(self, issue_index, matching_num):
        matching_reward_amount = (
            self.lottery_contract.functions.getMatchingRewardAmount(
                issue_index, matching_num
            ).call()
        )

        return int(matching_reward_amount / self.decimals)

    def get_lottery_numbers(self, tokenid):
        return self.token_contract.functions.getLotteryNumbers(tokenid).call()

    def get_reward_view(self, tokenid):
        return self.lottery_contract.functions.getRewardView(tokenid).call()

    def get_history_numbers(self, issue_index):
        history_numbers = []

        for i in range(0, 4):
            number = self.lottery_contract.functions.historyNumbers(
                issue_index, i
            ).call()
            history_numbers.append(number)

        return history_numbers

    def get_history_amount(self, issue_index):
        history_amount = {}

        for i in range(1, 4):
            winner = self.lottery_contract.functions.historyAmount(
                issue_index, i
            ).call()

            if i == 1:
                history_amount["4"] = int(winner / self.decimals)
            elif i == 2:
                history_amount["3"] = int(winner / self.decimals)
            elif i == 3:
                history_amount["2"] = int(winner / self.decimals)

        return history_amount

    def get_issue_index(self):
        return self.lottery_contract.functions.issueIndex().call()

    def get_last_timestamp(self, epoch=False):
        last_timestamp = self.lottery_contract.functions.lastTimestamp().call()

        if epoch:
            return last_timestamp
        else:
            return datetime.fromtimestamp(last_timestamp)

    def get_max_number(self):
        return self.lottery_contract.functions.maxNumber().call()

    def get_min_price(self):
        min_price = self.lottery_contract.functions.minPrice().call()

        return int(min_price / self.decimals)

    def get_total_addresses(self):
        return self.lottery_contract.functions.totalAddresses().call()

    def get_total_amount(self):
        total_amount = self.lottery_contract.functions.totalAmount().call()

        return total_amount / self.decimals

    def get_allocation(self):
        allocation = {}

        for i in range(0, 3):
            alloc = self.lottery_contract.functions.allocation(i).call()
            allocation[f"{i + 1}"] = alloc

        return allocation

    def get_cake(self):
        return self.lottery_contract.functions.cake().call()

    def get_lotteryNFT(self):
        return self.lottery_contract.functions.lotteryNFT().call()

    def get_balance_of(self, address):
        return self.token_contract.functions.balanceOf(address).call()
