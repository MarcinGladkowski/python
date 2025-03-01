import time
from concurrent.futures import ThreadPoolExecutor

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def withdraw(self, amount):
        if self.balance >= amount:
            new_balance = self.balance - amount
            time.sleep(0.1)  # Simulate a delay
            self.balance = new_balance
        else:
            raise ValueError("Insufficient balance")

"""Both threads are trying to withdraw money from the same account balance 1000!!!"""
account = BankAccount(1000)

with ThreadPoolExecutor(max_workers=2) as executor:
    executor.submit(account.withdraw, 500)
    executor.submit(account.withdraw, 700)
"""
The result it's not deterministic. Returns 300 or 500.
"""
print(f"Final account balance: {account.balance}")