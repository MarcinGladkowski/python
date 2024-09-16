"""
wait() for collection of tasks
Gets collection of awaitable tasks
By default wait for all completed tasks

Possible modes:
ALL_COMPLETED
FIRST_COMPLETED
FIRST_EXCEPTION

returns tuple for two sets:
- first (return all elements meets conditions)
- second (return all elements does not meets conditions)
"""

"""
wait for all tasks to complete

done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
"""

"""
wait for the first task to fail

done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)
"""
import asyncio
import random

async def task_coro(arg) -> int:
    # random value
    value = random.random()
    # suspend and sleep
    await asyncio.sleep(value)
    # report the argument and value
    return arg * value


# main coroutine
async def main():
    # create many independent tasks
    tasks = [asyncio.create_task(task_coro(i)) for i in range(100)]
    # suspend and run all coroutines
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    # report the result from first task
    task = done.pop()
    print(f"First task got: {task.result()}")

# create the coroutine and run it in the event loop
asyncio.run(main())
