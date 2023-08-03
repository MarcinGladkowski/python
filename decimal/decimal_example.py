"""
Decimal module
* Use Decimal when the precision is important - money!
* To Decimal construct inject only string values!
"""
from decimal import Decimal, ROUND_UP

# Without module
rate = 1.45
seconds = 3 * 60 + 42
cost = rate * seconds / 60
print(cost)

rate = Decimal('1.45')
seconds = Decimal(3 * 60 + 42)
cost = rate * seconds / Decimal(60)
print(cost)

"""
no decimal vs decimal
5.364999999999999 vs 5.365 (is correct)
"""

print(Decimal('1.45'))
print(Decimal(1.45)) # lost precision

"""
Calculate really small numbers, possible round to 0
"""
rate = Decimal('0.05')
seconds = Decimal(5)
cost = rate * seconds / Decimal(60)
print(cost)
print(round(cost, 2)) # 0


rounded = cost.quantize(Decimal('0.01'), rounding=ROUND_UP)
print(f'Cost {cost} after rounding is {rounded}')