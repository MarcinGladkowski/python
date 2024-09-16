import asyncio
import random
"""
RUN MANY COROUTINES

asyncio.gather() - takes multiple awaitables like coroutines or tasks
and return the asyncio.Future object
"""

# run many coroutines
# async def custom_coro(coro_num: int):
#     return f"Coroutine {coro_num}"
#
# future = asyncio.gather(custom_coro(1), custom_coro(2), custom_coro(3))

async def task_coro(arg):
    # random value
    value = random.random()
    # suspend and sleep
    await asyncio.sleep(value)
    # report the argument and value
    print(f'Task {arg} done after {value} seconds')

# main coroutine
async def main():
    # create many coroutines
    coros = [task_coro(i) for i in range(100)]
    # suspend and run all coroutines
    await asyncio.gather(*coros)

asyncio.run(main())
