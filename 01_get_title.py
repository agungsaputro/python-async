import aiohttp
import asyncio
import json

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'https://jsonplaceholder.typicode.com/posts')
        data = json.loads(html)

        for i in range(len(data)):
          print(f"title: {data[i]['title']}")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())