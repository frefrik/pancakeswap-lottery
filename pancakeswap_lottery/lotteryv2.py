from web3 import Web3
from .utils import load_abi


class LotteryV2:
    """Class for accessing PancakeSwap Lottery V2 smart-contract information."""

    def __init__(self, provider="https://bsc-dataseed.binance.org"):
        """Initialize the object

        Attributes:
            provider (str): Web3 HTTPProvider.

                Defaults to https://bsc-dataseed.binance.org

        Examples:
            lottery = LotteryV2()
        """
        self.w3 = Web3(Web3.HTTPProvider(provider))

        contract_addresses = {
            "PancakeSwapLottery": "0x5aF6D33DE2ccEC94efb1bDF8f92Bd58085432d2c",
            "CakeToken": "0x0E09FaBB73Bd3Ade0a17ECC321fD13a19e81cE82",
        }

        self.lottery_contract = self._load_contract(
            abi_name="PancakeSwapLottery",
            address=contract_addresses["PancakeSwapLottery"],
        )

        self.token_contract = self._load_contract(
            abi_name="CakeToken", address=contract_addresses["CakeToken"]
        )

        self.decimals = 10 ** 18

    def _load_contract(self, abi_name, address):
        return self.w3.eth.contract(address=address, abi=load_abi(abi_name))
