"""
GIL doesn't allow execute threads at the same time
It's useful when we want to use slow system calls/blocking I/O calls
"""

import time, select, socket
from threading import Thread


def factorize(number):
    for i in range(1, number + 1):
        if number % i == 0:
            yield i


numbers = [123545, 45345345]

start = time.time()

for number in numbers:
    list(factorize(number))

end = time.time()
delta = end - start

print(f'Operation took {delta:.3f} second')

'''
Using Threads
'''


class FactorizeThread(Thread):
    def __init__(self, number):
        super().__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))


thread_start = time.time()
threads = []
for number in numbers:
    thread = FactorizeThread(number)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

thread_end = time.time()
thread_delta = thread_end - thread_start

print(f'Operation on threads took {thread_delta:.3f} second')

"""
Important! 

Implementation using threads isn't faster then normal invocation!
"""

system_start = time.time()


def slow_systemcall():
    select.select([socket.socket()], [], [], 0.1)


for _ in range(5):
    slow_systemcall()

system_end = time.time()
system_delta = system_start - system_end

print(f'Operation on system call took {thread_delta:.3f} second')

"""
Leave the main thread and not block other calculations!
"""

thread_start = time.time()
threads = []
for _ in range(5):
    thread = Thread(target=slow_systemcall)
    thread.start()
    threads.append(thread)


def compute_helicopter_location(index):
    # ....
    pass


for i in range(5):
    compute_helicopter_location(i)


for thread in threads:
    thread.join()

thread_end = time.time()
thread_delta = thread_end - thread_start
print(f'Operation on helicopter took {thread_delta:.3f} second')
