"""
Share data between coroutines using asyncio.Queue
- FIFO
- Save without race conditions
"""
import asyncio
from random import random

from dict.dict_ordering import value


# coroutine to generate work
async def producer(queue):
    print("Producer: running")
    for i in range(10):
        value = random()
        # block to simulate work
        await asyncio.sleep(value)
        # add to the queue
        await queue.put(value)

    # send all done signal
    await queue.put(None)
    print("Producer: done")

# entry point coroutine
async def main():
    # create the shared queue
    queue = asyncio.Queue()
    # run the consumer as an independent task
    await asyncio.create_task(producer(queue))
    # consume items from the queue until a None is seen
    while True:
        # get a value from a queue
        value = await queue.get()
        # check for a "no more data" value
        if not value:
            break
        # report the value
        print(f"Got {value}")

# start asyncio program
asyncio.run(main())

