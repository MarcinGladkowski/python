import asyncio
import random

async def task_coro(arg) -> int:
    # random value
    value = random.random() * 10
    # suspend and sleep
    await asyncio.sleep(value)
    # report the argument and value
    return arg * value


# main coroutine
async def main():
    # create many independent tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(100)]
    # handle tasks in completion order
    for task in asyncio.as_completed(tasks):
        # suspend and get the result from task
        result = await task
        # report the task result
        print(f'> got {result}')


# create the coroutine and run it in the event loop
asyncio.run(main())