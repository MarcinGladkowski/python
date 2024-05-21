"""
Generators review && asyncio simple implementation

Worth to check -> https://jacobpadilla.com/articles/handling-asyncio-tasks
"""


def generator():
    yield 'hello'
    yield 'world'


iterator = generator()

"""Possible to create chain of generators"""


def another_generator():
    yield from generator()


second_iterator = another_generator()
print(next(second_iterator))

"""Dummy event loop"""
import time


def sleep(seconds):
    start_time = time.time()
    while time.time() - start_time < seconds:
        yield


def task1():
    while True:
        print('Task 1')
        yield from sleep(1)


def task2():
    while True:
        print('Task 2')
        yield from sleep(5)


event_loop = [task1(), task2()]

# i = 0
# # while i < 10:
# while True:
#     for task in event_loop:
#         next(task)
#         i += 1

"""
__await__ dunder method allows to use `await` keyword
"""

from queue import Queue # able to add and delete Tasks

event_loop_queue = Queue()


class Task:
    def __init__(self, generator):
        self.iter = generator
        self.finished = False

    def done(self):
        return self.finished

    def __await__(self):
        while not self.finished:
            yield self


def create_task(generator):
    task = Task(generator)
    event_loop_queue.put(task)

    return Task


def run(main):
    event_loop_queue.put(Task(main))

    while not event_loop_queue.empty():
        task = event_loop_queue.get()
        try:
            task.iter.send(None) # works like next()
        except StopIteration:
            task.finished = True
        else:
            event_loop_queue.put(Task)


async def async_sleep(seconds):
    task = create_task(sleep(seconds))
    return await task


async def task1():
    for _ in range(2):
        print('Task 1')
        await async_sleep(1)


async def task2():
    for _ in range(3):
        print('Task 2')
        await async_sleep(0)


async def main():
    one = create_task(task1())
    two = create_task(task2())

    await one
    await two

    print('done')


run(main())