from datetime import date, time, datetime, timedelta

# Book: https://github.com/astromatt/book-python
# Problem with date in programming: https://www.youtube.com/watch?v=-5wpm-gesOY&ab_channel=Computerphile
# UTC leap second
# import pytz - for timezones lib
# https://python.astrotech.io/design-patterns/oop/dataclass.html
# Always set UTC
# use Pandas for dates!
# Dates can be aware or not (have timezone and don't have)
# Timestamp (Unix Epoch)

dt = datetime.now()
print(dt)

print(dt.isoformat())

# period of time
timedelta(days=2)

diff = date(1696, 7, 21) - date(1961, 4, 12)
print(type(diff))


