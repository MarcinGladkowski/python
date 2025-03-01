"""
Threading

Concurrency: multiple tasks run in overlapping time periods
Parallelism: multiple tasks run at the same time, leveraging multiple CPUs (mostly)
"""
import threading
import time
from concurrent.futures import ThreadPoolExecutor

def threaded_function():
    for number in range(3):
        print(f"Printing from {threading.current_thread().name}. {number=}")
        time.sleep(0.1)

with ThreadPoolExecutor(max_workers=4, thread_name_prefix="Worker") as executor:
    """
    By context switching, the Python interpreter pauses executions and runs another thread
    """
    for _ in range(4):
        executor.submit(threaded_function)

"""
import sys
sys.getswitchinterval() # returns 0.005s -> 5 milliseconds
"""


"""
GIL - global interpreter lock

The GIL is a mutex that protects access to Python objects, preventing multiple threads from executing Python bytecodes at once.
This means that only one thread can execute Python code at a time, even on multi-core systems.

Single bytecodes are atomic. GIL allow only one thread to execute Python bytecodes at a time.
"""

