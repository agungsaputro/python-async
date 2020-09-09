import aiohttp
import asyncio
import json

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        api_key= 'c65a3f8532f1acbd869f9e1a22ffc3d9'
        reanu = await fetch(session, f'https://api.themoviedb.org/3/person/6384/tv_credits?api_key={api_key}')
        res1 = json.loads(reanu)
        # print(json.dumps(res1, indent=6))
        file(res1,"get_moviedb_001.json")

def file(data, filename='data.json'):
    save = open(filename, 'w')
    save.write(json.dumps(data, indent=4))
    save.close()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())