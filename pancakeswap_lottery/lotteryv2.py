from datetime import datetime
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

    def _status(self, statusid):
        status = {
            1: "Open",
            2: "_Unknown_",
            3: "Claimed",
        }

        return status[statusid]

    def view_lottery(self, lotteryround):
        data = self.lottery_contract.functions.viewLottery(lotteryround).call()

        d = {
            "status": self._status(data[0]),
            "startTime": datetime.fromtimestamp(data[1]),
            "endTime": datetime.fromtimestamp(data[2]),
            "priceTicketInCake": data[3] / self.decimals,
            "discountDivisor": data[4],
            "rewardsBreakdown": data[5],
            "treasuryFee": data[6],
            "cakePerBracket": {
                "match_1": round(data[7][0] / self.decimals),
                "match_2": round(data[7][1] / self.decimals),
                "match_3": round(data[7][2] / self.decimals),
                "match_4": round(data[7][3] / self.decimals),
                "match_5": round(data[7][4] / self.decimals),
                "match_6": round(data[7][5] / self.decimals),
            },
            "countWinnersPerBracket": {
                "match_1": data[8][0],
                "match_2": data[8][1],
                "match_3": data[8][2],
                "match_4": data[8][3],
                "match_5": data[8][4],
                "match_6": data[8][5],
            },
            "firstTicketId": data[9],
            "firstTicketIdNextLottery": data[10],
            "amountCollectedInCake": data[11] / self.decimals,
            "finalNumber": data[12],
        }

        return d

    def current_round(self):
        """Get current lottery round number

        Examples:
            >>> lottery.current_round()
            8
        """
        return self.lottery_contract.functions.currentLotteryId().call()

    def current_ticket(self):
        """Get current ticket id

        Examples:
            >>> lottery.current_ticket()
            38963
        """
        return self.lottery_contract.functions.currentTicketId().call()

    def prize_pool(self, lotteryround=None):
        """Get total prize pool size in CAKE

        Args:
            lotteryround (:obj:`int`, optional): Lottery round

        Examples:
            >>> lottery.prize_pool()
            141947
        """

        if not lotteryround:
            lotteryround = self.current_round()

        data = self.view_lottery(lotteryround)
        amount = data.get("amountCollectedInCake")

        return round(amount)

    def draw_date(self, lotteryround=None):
        """Get lottery draw date

        Args:
            lotteryround (:obj:`int`, optional): Lottery round

        Examples:
            >>> lottery.draw_date()
            141947
        """

        if not lotteryround:
            lotteryround = self.current_round()

        lottery = self.view_lottery(lotteryround)
        lotter_date = lottery.get("endTime")

        return lotter_date

    def prize_pool_allocation(self, lotteryround=None):
        """Get prize pool allocation in CAKE

        Allocation percentages:
        - Match first 1: 1%
        - Match first 2: 3%
        - Match first 3: 6%
        - Match first 4: 10%
        - Match first 5: 20%
        - Match first 6: 40%
        - Burn Pool: 20%

        Args:
            lotteryround (:obj:`int`, optional): Lottery round

        Examples:
            >>> lottery.prize_pool_allocation()
            {
                'match_1': 1419,
                'match_2': 4258,
                'match_3': 8517,
                'match_4': 14195,
                'match_5': 28389,
                'match_6': 56779,
                'burn': 28389
            }
        """
        if not lotteryround:
            lotteryround = self.current_round()

        data = self.view_lottery(lotteryround)
        prize_pool = data.get("amountCollectedInCake")

        d = {
            "match_1": round(prize_pool * 0.01),
            "match_2": round(prize_pool * 0.03),
            "match_3": round(prize_pool * 0.06),
            "match_4": round(prize_pool * 0.1),
            "match_5": round(prize_pool * 0.2),
            "match_6": round(prize_pool * 0.4),
            "burn": round(prize_pool * 0.2),
        }

        return d

    def ticket_price(self, lotteryround=None):
        """Get ticket price in CAKE

        Args:
            lotteryround (:obj:`int`, optional): Lottery round

        Examples:
            >>> lottery.ticket_price()
            0.34
        """

        if not lotteryround:
            lotteryround = self.current_round()

        lottery = self.view_lottery(lotteryround)
        price = lottery.get("priceTicketInCake")

        return price

    def status(self, lotteryround=None):
        """Get status of lottery round

        Args:
            lotteryround (:obj:`int`, optional): Lottery round

        Examples:
            >>> lottery.status()
            Open
        """

        if not lotteryround:
            lotteryround = self.current_round()

        data = self.view_lottery(lotteryround)
        lottery_status = data.get("status")

        return lottery_status

    def winners_per_bracket(self, lotteryround):
        """Get number of winners per prize bracket

        Args:
            lotteryround (int): Lottery round

        Examples:
            >>> lottery.winners_per_bracket(lotteryround=16)
            {
                'match_1': 19133,
                'match_2': 1921,
                'match_3': 188,
                'match_4': 21,
                'match_5': 1,
                'match_6': 1
            }
        """

        data = self.view_lottery(lotteryround)
        d = data.get("countWinnersPerBracket")

        return d

    def cake_per_bracket(self, lotteryround):
        """Get amount of CAKE won per ticket in each prize bracket

        Args:
            lotteryround (int): Lottery round

        Examples:
            >>> lottery.cake_per_bracket(lotteryround=16)
            {
                'match_1': 0.10150861284172895,
                'match_2': 3.0330519877680375,
                'match_3': 61.98396668619574,
                'match_4': 924.8401378575238,
                'match_5': 38843.285790016,
                'match_6': 77686.571580032
            }
        """

        data = self.view_lottery(lotteryround)
        d = data.get("cakePerBracket")

        return d

    def winning_probability(self, numbers_matched=None):
        """Get percentage probability of winning the lottery

        Args:
            numbers_matched (:obj:`int`, optional): Number of winning numbers matched

        Examples:
            >>> lottery.winning_probability()
            {
                'match_1': 10.0,
                'match_2': 1.0,
                'match_3': 0.1,
                'match_4': 0.01,
                'match_5': 0.001,
                'match_6': 0.0001
            }
        """
        possible_numbers = 10
        matchballs = [1, 2, 3, 4, 5, 6]
        probability_pct = {}

        if numbers_matched:
            if numbers_matched not in range(1, 7):
                return "Pick a number between 1 and 6"

            e = possible_numbers ** numbers_matched
            odds = 1 / e * 100

            return float(f"{odds:.4f}")

        for matchball in matchballs:
            e = possible_numbers ** matchball
            odds = 1 / e * 100
            probability_pct.update({f"match_{matchball}": float(f"{odds:.4f}")})

        return probability_pct

    def winning_numbers(self, lotteryround):
        """Get winning numbers for lottery round

        Args:
            lotteryround (int): Lottery round

        Examples:
            >>> lottery.winning_numbers(lotteryround=16)
            0
        """
        data = self.view_lottery(lotteryround)
        final_number = str(data.get("finalNumber"))
        final_number = final_number[::-1][:-1]

        return final_number

    def ticket_winnings(self, lotteryround, ticketid):
        """Get lottery winnings (CAKE) for a given ticket and round

        Args:
            lotteryround (int): Lottery round
            ticketid (int): Ticket id

        Examples:
            >>> lottery.ticket_winnings(lotteryround=15, ticketid=567093)
            865.536634168
        """
        winnings = 0
        brackets = [0, 1, 2, 3, 4, 5]

        for bracket in brackets:
            data = self.lottery_contract.functions.viewRewardsForTicketId(
                lotteryround, ticketid, bracket
            ).call()

            if data > 0:
                winnings = data / self.decimals

        return winnings

    def address_winnings(self, address, lotteryround):
        """Get lottery winnings (CAKE) for a given address and round

        Args:
            address (int): BSC address
            lotteryround (int): Lottery round

        Examples:
            >>> lottery.address_winnings("0x621D6ee5FA9634d86396C13fAaD6A7827606A6d7", lotteryround=16)
            {'tickets': 8, 'ticketids': [634970, 634971, 634972, 634973, 634974, 634975, 634976, 634977], 'winning_tickets': [634970, 634971]}
        """
        userinfo = self.lottery_contract.functions.viewUserInfoForLotteryId(
            self.w3.toChecksumAddress(address),
            lotteryround,
            0,
            100,
        ).call()

        count = 0
        winning_tickets = []

        for i in userinfo[2]:
            if i is True:
                winning_tickets.append(userinfo[0][count])
            count += 1

        d = {
            "tickets": userinfo[3],
            "ticketids": userinfo[0],
            "winning_tickets": winning_tickets,
        }

        return d
