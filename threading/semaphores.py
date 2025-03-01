"""
Semaphores are used to control access to a shared resource.
A semaphore is a counter that is used to control the number of threads that can access a shared resource at the same time.
The semaphore is initialized to the maximum number of threads that can access the resource at the same time.
Each time a thread accesses the resource, the semaphore is decremented.
When the semaphore reaches zero, the resource is locked and no other threads can access it.
When a thread is done with the resource, it increments the semaphore, allowing other threads to access the resource.

Useful while resources are limited, like a database connection pool.
"""
import random
import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Semaphore with a maximum of 2 resources (tellers)
teller_semaphore = threading.Semaphore(2)

def now():
    return time.strftime("%H:%M:%S")

def serve_customer(name):
    print(f"{now()}: {name} is waiting for a teller.")
    with teller_semaphore:
        print(f"{now()}: {name} is being served by a teller.")
        # Simulate the time taken for the teller to serve the customer
        time.sleep(random.randint(1, 3))
        print(f"{now()}: {name} is done being served.")

customers = [
    "Customer 1",
    "Customer 2",
    "Customer 3",
    "Customer 4",
    "Customer 5",
]

with ThreadPoolExecutor(max_workers=5) as executor:
    for customer_name in customers:
        thread = executor.submit(serve_customer, customer_name)

print(f"{now()}: All customers have been served.")