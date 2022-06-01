# Exer-16-Manipulating-Dates-Involving-Time-Zones.py

from datetime import datetime
from pytz import timezone

d = datetime(2022, 5, 31, 9, 00, 0)
print(d)

central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)

d = datetime(2013, 3, 10, 1, 45)
loc_d = central.localize(d)
print(loc_d)

from datetime import timedelta
import pytz

later = loc_d + timedelta(minutes=30)
print(later) # wrong result

later = central.normalize(loc_d + timedelta(minutes=30))
print(later)  # correct

print(loc_d)
utc_d = loc_d.astimezone(pytz.utc)
print(utc_d)

later_utc = utc_d + timedelta(minutes=30)
print(later_utc.astimezone(central))

print(pytz.country_timezones['IN'])
print(pytz.country_timezones['TR'])
