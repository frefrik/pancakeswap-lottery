from datetime import datetime
from web3 import Web3
from .utils import generate_lottery_date, load_abi


class Lottery:
    """Class for accessing PancakeSwap Lottery smart-contract information."""

    def __init__(self, provider="https://bsc-dataseed.binance.org:443"):
        """Initialize the object

        Attributes:
            provider (str): Web3 HTTPProvider.

                Defaults to https://bsc-dataseed.binance.org:443

        Examples:
            lottery = Lottery()
        """
        self.w3 = Web3(Web3.HTTPProvider(provider))

        contract_addresses = {
            "LotteryUpgradeProxy": "0x3C3f2049cc17C136a604bE23cF7E42745edf3b91",
            "LotteryNFT": "0x5e74094Cd416f55179DBd0E45b1a8ED030e396A1",
        }

        self.lottery_contract = self._load_contract(
            abi_name="LotteryUpgradeProxy",
            address=contract_addresses["LotteryUpgradeProxy"],
        )

        self.token_contract = self._load_contract(
            abi_name="LotteryNFT", address=contract_addresses["LotteryNFT"]
        )

        self.decimals = 10 ** 18

    def _load_contract(self, abi_name, address):
        return self.w3.eth.contract(address=address, abi=load_abi(abi_name))

    def get_total_rewards(self, issue_index):
        """Get total rewards of lottery round

        Args:
            issue_index (int): Lottery round

        Examples:
            >>> lottery.get_total_rewards(432)
            51384.125
        """
        total_rewards = self.lottery_contract.functions.getTotalRewards(
            issue_index
        ).call()

        return total_rewards / self.decimals

    def get_lottery_date(self, issue_index):
        """Get date and time of lottery round

        Args:
            issue_index (int): Lottery round

        Examples:
            >>> lottery.get_lottery_date(432)
            2021-03-26 02:00:00+00:00
        """
        lottery_date = generate_lottery_date(issue_index)

        return lottery_date

    def get_drawed(self):
        """Check if current lottery round is drawed

        Examples:
            >>> lottery.get_drawed()
            False
        """
        return self.lottery_contract.functions.drawed().call()

    def get_drawing_phase(self):
        """Get current lottery round drawing phase

        Examples:
            >>> lottery.get_drawing_phase()
            False
        """
        return self.lottery_contract.functions.drawingPhase().call()

    def get_matching_reward_amount(self, issue_index, matching_num):
        """Get number of tickets matched a specified number

        Args:
            issue_index (int): Lottery round
            matching_num (int): Number to match

        Examples:
            >>> lottery.get_matching_reward_amount(432, 3)
            34
        """
        matching_reward_amount = (
            self.lottery_contract.functions.getMatchingRewardAmount(
                issue_index, matching_num
            ).call()
        )

        return int(matching_reward_amount / self.decimals)

    def get_lottery_numbers(self, tokenid):
        """Get lottery numbers for a given ticket

        Args:
            tokenid (int): Lottery ticket id

        Examples:
            >>> lottery.get_lottery_numbers(1328060)
            [11, 5, 14, 6]
        """
        return self.token_contract.functions.getLotteryNumbers(tokenid).call()

    def get_reward_view(self, tokenid):
        """Get rewards for a given ticket

        Args:
            tokenid (int): Lottery ticket id

        Examples:
            >>> lottery.get_reward_view(1328060)
            0
        """
        return self.lottery_contract.functions.getRewardView(tokenid).call()

    def get_history_numbers(self, issue_index):
        """Get winning numbers of lottery round

        Args:
            issue_index (int): Lottery round

        Examples:
            >>> lottery.get_history_numbers(432)
            [2, 13, 7, 3]
        """
        history_numbers = []

        for i in range(0, 4):
            number = self.lottery_contract.functions.historyNumbers(
                issue_index, i
            ).call()
            history_numbers.append(number)

        return history_numbers

    def get_history_amount(self, issue_index):
        """Get numbers of tickets matched

        Args:
            issue_index (int): Lottery round

        Examples:
            >>> lottery.get_history_amount(432)
            {'4': 1, '3': 34, '2': 718}
        """
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
        """Get current lottery round id

        Examples:
            >>> lottery.get_issue_index()
            435
        """
        return self.lottery_contract.functions.issueIndex().call()

    def get_last_timestamp(self, epoch=False):
        """Last updated (timestamp)

        Args:
            epoch (bool): Return as epoch timestamp?

        Examples:
            >>> lottery.get_last_timestamp(epoch=False)
            2021-03-27 11:38:49
        """
        last_timestamp = self.lottery_contract.functions.lastTimestamp().call()

        if epoch:
            return last_timestamp
        else:
            return datetime.fromtimestamp(last_timestamp)

    def get_max_number(self):
        """Get max number

        Examples:
            >>> lottery.get_max_number()
            14
        """
        return self.lottery_contract.functions.maxNumber().call()

    def get_min_price(self):
        """Get current price of 1 ticket

        Examples:
            >>> lottery.get_min_price()
            1
        """
        min_price = self.lottery_contract.functions.minPrice().call()

        return int(min_price / self.decimals)

    def get_total_addresses(self):
        """Get total addresses

        Examples:
            >>> lottery.get_total_addresses()
            200
        """
        return self.lottery_contract.functions.totalAddresses().call()

    def get_total_amount(self):
        """Get total pot (CAKE) of current lottery round

        Examples:
            >>> lottery.get_total_amount()
            34977.25
        """
        total_amount = self.lottery_contract.functions.totalAmount().call()

        return total_amount / self.decimals

    def get_allocation(self):
        """Get prize pool allocation (percent)

        Examples:
            >>> lottery.get_allocation()
            {'1': 50, '2': 20, '3': 10}
        """
        allocation = {}

        for i in range(0, 3):
            alloc = self.lottery_contract.functions.allocation(i).call()
            allocation[f"{i + 1}"] = alloc

        return allocation

    def get_cake(self):
        """Get CAKE contract address

        Examples:
            >>> lottery.get_cake()
            0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82
        """
        return self.lottery_contract.functions.cake().call()

    def get_lotteryNFT(self):
        """Get PLT-token contract address

        Examples:
            >>> lottery.get_lotteryNFT()
            0x5e74094Cd416f55179DBd0E45b1a8ED030e396A1
        """
        return self.lottery_contract.functions.lotteryNFT().call()

    def get_balance_of(self, address):
        """Get total number of tickets bought by a given address

        Args:
            address (str): BSC address

        Examples:
            >>> lottery.get_balance_of("0xc13456A34305e9265E907F70f76B1BA6E2055c8B")
            2673
        """
        return self.token_contract.functions.balanceOf(address).call()
