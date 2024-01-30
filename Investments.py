import pandas as pd
import numpy as np
import locale
from dateutil import rrule
import datetime

def weeks_between(start_date, end_date):
    weeks = rrule.rrule(rrule.WEEKLY, dtstart=start_date, until=end_date)
    return weeks.count()

def days_between(start_date, end_date):
    days = rrule.rrule(rrule.DAILY, dtstart=start_date, until=end_date)
    return days.count()

weeksLeft = weeks_between(datetime.date.today(), datetime.date(2025, 1, 1))
daysLeft = np.busday_count(datetime.date.today(), datetime.date(2025, 1, 1))
locale.setlocale(locale.LC_ALL, 'en_US')


def investment(value, i, percent, length):
    value2 = value * percent
    change = value2 - value

    if (length > 52):
        title = "Day"
        YIncome = change * 260
        YIncomeTitle = "Yearly Income ( * 260 days)"
    else:
        title = "Week"
        YIncome = change * 52
        YIncomeTitle = "Yearly Income ( * 52 weeks)"
    

    return value2, {title: i+1,
        "Total": locale.currency(value2, grouping=True),
        "Change": locale.currency(change, grouping=True),
        YIncomeTitle: locale.currency(YIncome, grouping=True)}

length = daysLeft
percent = 1.03
value = 2812
d = []


print(f"Starting with: {locale.currency(value, grouping=True)} and {percent}%")
for i in range(length):
    value, array = investment(value, i, percent, length)
    d.append(array)

idk = pd.DataFrame(d).reset_index(drop=True)
print(idk.to_markdown())