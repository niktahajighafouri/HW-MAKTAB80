# Python timedelta() function is present under datetime library which is generally used for calculating differences in dates and also can be used for date manipulations in Python. It is one of the easiest ways to perform date manipulations.

# Syntax : datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0) Returns : Date

# Timedelta function demonstration

from datetime import datetime, timedelta


# Using current time
ini_time_for_now = datetime.now()

# printing initial_date
print("initial_date", str(ini_time_for_now))

# Calculating future dates
# for two years
future_date_after_2yrs = ini_time_for_now + \
    timedelta(days=730)

future_date_after_2days = ini_time_for_now + \
    timedelta(days=2)

# printing calculated future_dates
print('future_date_after_2yrs:', str(future_date_after_2yrs))
print('future_date_after_2days:', str(future_date_after_2days))

# output:
# initial_date 2019-02-27 12:41:45.018389
# future_date_after_2yrs: 2021-02-26 12:41:45.018389
# future_date_after_2days: 2019-03-01 12:41:45.018389
