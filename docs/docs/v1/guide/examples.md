# Examples

Here's a few example use cases for this module:

- [Lottery stats](#lottery-stats) - Current lottery round stats
- [Lottery history](#lottery-history) - Past lottery rounds stats

## Lottery stats

Get stats from the current lottery round.

=== "Code"
    ```python
    from datetime import datetime
    from pancakeswap_lottery import Lottery


    def format_datestr(dt):
        now = datetime.now().astimezone()
        total_seconds = int((dt - now).total_seconds())

        days, remainder = divmod(total_seconds, 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)

        d = {
            "total_seconds": total_seconds,
            "days": int(days),
            "hours": int(hours),
            "minutes": int(minutes),
            "seconds": int(seconds),
        }

        if d["hours"] == 0:
            datestr = f"{d['minutes']} minutes"
        else:
            datestr = f"{d['hours']} hours {d['minutes']} minutes"

        return datestr


    def get_lottery_stats():
        lottery = Lottery()

        issue_index = lottery.get_issue_index()
        pool_size = lottery.get_total_amount()

        lottery_date = lottery.get_lottery_date(issue_index)
        drawdate_str = format_datestr(lottery_date)

        allocation = lottery.get_allocation()

        prize_pool_match4 = int(pool_size * allocation.get("1") / 100)
        prize_pool_match3 = int(pool_size * allocation.get("2") / 100)
        prize_pool_match2 = int(pool_size * allocation.get("3") / 100)

        ret_str = "🥞 The CAKE Lottery 🥞"
        ret_str += f"\nRound #{issue_index}"
        ret_str += f"\nDraw in {drawdate_str} ({lottery_date.strftime('%Y-%m-%d %H:%M')})"

        ret_str += "\n\n💰 Pool size"
        ret_str += f"\n{int(pool_size)} CAKE"

        ret_str += "\n\n💵 Prize pool allocation"
        ret_str += f"\nMatch 4: {prize_pool_match4} CAKE"
        ret_str += f"\nMatch 3: {prize_pool_match3} CAKE"
        ret_str += f"\nMatch 2: {prize_pool_match2} CAKE"

        return ret_str


    lottery_stats = get_lottery_stats()
    print(lottery_stats)
    ```

=== "Output"
    ```
    🥞 The CAKE Lottery 🥞
    Round #481
    Draw in 2 hours 2 minutes (2021-04-19 14:00)

    💰 Pool size
    1581 CAKE

    💵 Prize pool allocation
    Match 4: 790 CAKE
    Match 3: 316 CAKE
    Match 2: 158 CAKE
    ```

## Lottery history
Get lottery history data (*Lottery Date*, *Round*, *Prize pool*) from the last `X` rounds.

=== "Code"
    ```python
    from pancakeswap_lottery import Lottery


    def get_lottery_history(last_rounds):
        lottery = Lottery()

        issue_index = lottery.get_issue_index()

        header = ["Lottery Date", "Round", "Prizes (CAKE)"]
        rows = [header]

        for i in range(0, last_rounds):
            issue_index -= 1

            lottery_date = lottery.get_lottery_date(issue_index)
            lottery_date_str = lottery_date.strftime("%Y-%m-%d %H:%M")

            total_rewards = int(lottery.get_total_rewards(issue_index))

            row = [lottery_date_str, issue_index, total_rewards]
            rows.append(row)

        ret_str = "🥞 The CAKE Lottery - History 🥞\n\n"
        ret_str += f"Showing data for last {last_rounds} rounds:\n\n"
        ret_str += "\n".join(["".join([f"{x:>16}" for x in r]) for r in rows])

        return ret_str


    rounds = 10  # get data for last 10 rounds
    lottery_history = get_lottery_history(rounds)
    print(lottery_history)
    ```

=== "Output"
    ```
    🥞 The CAKE Lottery - History 🥞

    Showing data for last 10 rounds:

        Lottery Date           Round   Prizes (CAKE)
    2021-04-19 02:00             480           91715
    2021-04-18 14:00             479           44838
    2021-04-18 02:00             478            3203
    2021-04-17 14:00             477            1736
    2021-04-17 02:00             476           52022
    2021-04-16 14:00             475           47675
    2021-04-16 02:00             474            1736
    2021-04-15 14:00             473            3088
    2021-04-15 02:00             472          113863
    2021-04-14 14:00             471           61936
    ```
