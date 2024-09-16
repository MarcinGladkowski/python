import asyncio
from importlib.machinery import all_suffixes

from LLM.main import decoded

"""
keywords: async
Extension for 'def' for defining subroutines.

Can be defined and created but only called via event loop
"""

async def custom_coro():
    """
    Define a coroutine.
    """
    print('hello there')

# create coroutine
coro = custom_coro()

"""Execute coroutine by event loop"""
asyncio.run(coro)

"""
Execute coroutine from a coroutine using 'await' expression
"""

"""
Create and schedule task
"""
#task = asyncio.create_task(custom_coro())

"""
Suspended until task is complete and get return value

value = await task
"""
async def task_coro():
    # report a message
    print('The task is running...')
    # suspend and sleep for a moment
    await asyncio.sleep(1)
    # report a message
    print('The task is done...')
    # return a result
    return 'The answer is 100'

# main coroutine
async def main():
    # run a task independently
    task = asyncio.create_task(task_coro())
    # suspend fo a moment
    await asyncio.sleep(0)
    # wait for the async task to complete
    await task
    # report a result message
    print(f"Got: {task.result()}")


### create the coroutine and run it in the event loop
asyncio.run(main())

