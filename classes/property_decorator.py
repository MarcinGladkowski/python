"""
Examples of usage a @property decorator based on 'leaky bucket' algorithm
"""
from datetime import datetime, timedelta


class Bucket:
    def __init__(self, period) -> None:
        self.period_delta = timedelta(seconds=period)
        self.reset_time = datetime.now()
        self.quota = 0

    def __repr__(self) -> str:
        return f'Bucket(quota={self.quota})'


def fill(bucket, amount):
    now = datetime.now()
    if (now - bucket.reset_time) > bucket.period_delta:
        bucket.quota = 0
        bucket.reset_time = now
    bucket.quota += amount


def deduct(bucket, amount):
    now = datetime.now()
    if (now - bucket.reset_time) > bucket.period_delta:
        return False
    if bucket.quota - amount < 0:
        return False
    bucket.quota -= amount
    return True


bucket = Bucket(60)
fill(bucket, 100)
print(bucket)

if deduct(bucket, 99):
    print('Need 99 data')
else:
    print('There is no 99 data')
print(bucket)

