import aiohttp
import asyncio
import json

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        post = await fetch(session, 'https://res.cloudinary.com/sivadass/raw/upload/v1535817394/json/products.json')
        data = json.loads(post)
        output_dict = [x for x in data if x['category'] == 'fruits']
        output_json = json.dumps(output_dict, indent=4)
        print(output_json)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())