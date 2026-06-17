#
# $ python -m pip install aiohttp
#
import asyncio
import aiohttp

async def main():
    print("Hello...")
    await asyncio.sleep(1)
    print("...world!")
    

RATE_LIMIT_DELAY = 1

async def fetch_page(session, url):
    async with session.get(url) as response:
        print(f"{url} - {response.status}")
    await asyncio.sleep(RATE_LIMIT_DELAY)     
    
    
async def main_pages():
    urls = [
        "https://httpbin.org/get",
        "https://httpbin.org/ip",
        "https://httpbin.org/headers",
    ]
    
    async with aiohttp.ClientSession() as session:
        for url in urls:
            await fetch_page(session, url)
    
    
if __name__ == '__main__':
    asyncio.run(main_pages())