from datetime import datetime, timedelta, timezone


def generate_lottery_date(issue_index):
    first_lottery_date = datetime(2020, 10, 23, 14, 0, 0, 0).replace(
        tzinfo=timezone.utc
    )
    number_of_test_lotteries = 3
    hour = 60 * 60

    lottery_date = first_lottery_date

    if issue_index < 48:
        lottery_date = lottery_date + timedelta(
            seconds=((issue_index - number_of_test_lotteries) * 2 * hour)
        )
    elif issue_index < 225:
        lottery_date = lottery_date + timedelta(
            seconds=(((48 - number_of_test_lotteries) * 2 * hour))
        )

        lottery_date = lottery_date + timedelta(seconds=((issue_index - 47) * 6 * hour))
    else:
        lottery_date = lottery_date + timedelta(
            seconds=((48 - number_of_test_lotteries) * 2 * hour)
        )

        lottery_date = lottery_date + timedelta(seconds=((225 - 48) * 6 * hour))

        lottery_date = lottery_date + timedelta(
            seconds=((issue_index - 224 + number_of_test_lotteries) * 12 * hour)
        )

    return lottery_date
