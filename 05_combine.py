import aiohttp
import asyncio
import json

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with aiohttp.ClientSession() as session:
        post = await fetch(session, 'https://jsonplaceholder.typicode.com/posts')
        user = await fetch(session, 'https://jsonplaceholder.typicode.com/users')

        dataPost = json.loads(post)
        dataUser = json.loads(user)

        for p in dataPost:
            p['user'] = [u for u in dataUser if u['id'] == p['userId']] 
            result = json.dumps(p, indent=6)
            print(result)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())