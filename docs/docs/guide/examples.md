# Examples

Here's a few example use cases for this module:

- [Lottery stats](#lottery-stats) - Current lottery round stats
- [Lottery history](#lottery-history) - Past lottery rounds stats

## Lottery stats

Get stats from the current lottery round.

=== "Code"
    ```python
    from datetime import datetime
    from pancakeswap_lottery import LotteryV2


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
        lottery = LotteryV2()

        lotteryround = lottery.current_round()
        prize_pool = lottery.prize_pool()

        draw_date = lottery.draw_date(lotteryround).astimezone()
        drawdate_str = format_datestr(draw_date)

        allocation = lottery.prize_pool_allocation()

        prize_pool_match1 = allocation.get("match_1")
        prize_pool_match2 = allocation.get("match_2")
        prize_pool_match3 = allocation.get("match_3")
        prize_pool_match4 = allocation.get("match_4")
        prize_pool_match5 = allocation.get("match_5")
        prize_pool_match6 = allocation.get("match_6")

        ret_str = "🥞 The CAKE Lottery 🥞"
        ret_str += f"\nRound #{lotteryround}"
        ret_str += f"\nDraw in {drawdate_str} ({draw_date})"

        ret_str += "\n\n💰 Prize pool"
        ret_str += f"\n{int(prize_pool)} CAKE"

        ret_str += "\n\n💵 Prize pool allocation"
        ret_str += f"\nMatch 6: {prize_pool_match6} CAKE"
        ret_str += f"\nMatch 5: {prize_pool_match5} CAKE"
        ret_str += f"\nMatch 4: {prize_pool_match4} CAKE"
        ret_str += f"\nMatch 3: {prize_pool_match3} CAKE"
        ret_str += f"\nMatch 2: {prize_pool_match2} CAKE"
        ret_str += f"\nMatch 1: {prize_pool_match1} CAKE"

        return ret_str


    lottery_stats = get_lottery_stats()
    print(lottery_stats)
    ```

=== "Output"
    ```
    🥞 The CAKE Lottery 🥞
    Round #20
    Draw in 5 hours 40 minutes (2021-07-12 20:00:00+02:00)

    💰 Prize pool
    63402 CAKE

    💵 Prize pool allocation
    Match 6: 25361 CAKE
    Match 5: 12680 CAKE
    Match 4: 6340 CAKE
    Match 3: 3804 CAKE
    Match 2: 1902 CAKE
    Match 1: 634 CAKE
    ```

## Lottery history
Get lottery history data (*Lottery Date*, *Round*, *Prize pool*) from the last `X` rounds.

=== "Code"
    ```python
    from pancakeswap_lottery import LotteryV2


    def get_lottery_history(last_rounds):
        lottery = LotteryV2()

        lotteryround = lottery.current_round()

        header = ["Lottery Date", "Round", "Prizes (CAKE)"]
        rows = [header]

        for i in range(0, last_rounds):
            lotteryround -= 1

            draw_date = lottery.draw_date(lotteryround)
            draw_date_str = draw_date.strftime("%Y-%m-%d %H:%M")

            prize_pool = int(lottery.prize_pool(lotteryround))

            row = [draw_date_str, lotteryround, prize_pool]
            rows.append(row)

        ret_str = "🥞 The CAKE Lottery - History\n"
        ret_str += f"\nLast {last_rounds} lottery rounds:\n\n"
        ret_str += "\n".join(["".join([f"{x:>16}" for x in r]) for r in rows])

        return ret_str


    rounds = 10  # get data for last 10 rounds
    lottery_history = get_lottery_history(rounds)
    print(lottery_history)
    ```

=== "Output"
    ```
    🥞 The CAKE Lottery - History

    Last 10 lottery rounds:

        Lottery Date           Round   Prizes (CAKE)
    2021-07-12 08:00              19           77631
    2021-07-11 20:00              18          145392
    2021-07-11 08:00              17            5009
    2021-07-10 20:00              16          194216
    2021-07-10 08:00              15           86554
    2021-07-09 20:00              14          100345
    2021-07-09 08:00              13            7988
    2021-07-08 20:00              12          130175
    2021-07-08 08:00              11           76197
    2021-07-07 20:00              10          141947
    ```
