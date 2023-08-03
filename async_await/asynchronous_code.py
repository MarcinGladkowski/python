import asyncio


async def two():
    print("Starting two...")
    await asyncio.sleep(2)
    print("Hello two")
    return 2


async def four():
    print("Starting four...")
    await asyncio.sleep(2)
    print("Hello four")
    return 4


async def main():
    print(await asyncio.gather(two(), four()))


asyncio.run(main())

"""
Expected output:

Starting two...
Starting four...
Hello two
Hello four
[2, 4]
"""