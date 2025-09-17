import asyncio
import time

async def cook_pasta():
    print("Cooking pasta...")
    await asyncio.sleep(10)  # Simulate time taken to cook pasta
    print("Pasta is ready!")
    
async def heat_meatleaf():
    print("Heating meatleaf...")
    await asyncio.sleep(3)  # Simulate time taken to heat meatleaf
    print("Meatleaf is heated!")
    
async def peel_avocado():
    print("Peeling/slicing avocado")
    time.sleep(2)  # 2 min to peel <- I'm slow.
    print("Avocado sliced.")
    
# print(type(cook_pasta())) # <class 'coroutine'>

async def lunch():
    print("Starting lunch preparation...")
    start_time = time.time()
    await asyncio.gather(
        cook_pasta(),
        heat_meatleaf(),
        peel_avocado()
        )
    end = time.time()
    print(f"Lunch is ready! Total time taken: {end - start_time:.2f} seconds")
    
    
asyncio.run(lunch()) # using asyncio