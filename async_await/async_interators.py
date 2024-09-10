import asyncio

"""
Based on https://realpython.com/python-async-iterators/
"""

"""
I/O bound operations
- file system operations
- network operations
- database operations
- user input and output operations
- external device operations

Python has an EVENT LOOP for asynchronous operations e.g. run by asyncio.run()

"""

class AsyncRange:
    def __init__(self, start, stop):
        self.data = range(start, stop)

    async def __aiter__(self):
        """
            Implemented method allows to be instanced of ASYNC ITERABLE (not ITERATOR)
        """
        for i in self.data:
            await asyncio.sleep(0.5)
            yield i



async def main():
    async for i in AsyncRange(1, 10):
        print(i)


asyncio.run(main())

"""
Create generator
"""
async def async_range(start, stop):
    for i in range(start, stop):
        await asyncio.sleep(0.5)
        yield i

