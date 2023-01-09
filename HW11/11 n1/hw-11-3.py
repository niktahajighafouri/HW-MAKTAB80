from datetime import datetime
from persiantools.jdatetime import JalaliDate

d1 = [int(x) for x in input('enter first date (yyyy-mm-dd-hour-min-sec):').split('-')]
d2 = [int(x) for x in input('enter first date (yyyy-mm-dd-hour-min-sec):').split('-')]
d1_ = datetime(d1[0], d1[1], d1[2], d1[3], d1[4], d1[5])
d2_ = datetime(d2[0], d2[1], d2[2], d2[3], d2[4], d2[5])
difference = d2_ - d1_
print(f'difference of two dates in seconds is: {difference.total_seconds()}')
print(f'two dates in jalali are: \n {JalaliDate(d1_)}\n {JalaliDate(d2_)}')
