import aiohttp
import asyncio
import json


class fetcher:
    @staticmethod
    async def get(url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()
    
    @staticmethod
    async def post(url,data):
        async with aiohttp.ClientSession() as session:
            async with session.post(url,json=data) as response:
                return await response.text()

    @staticmethod
    async def delete(url):
        async with aiohttp.ClientSession() as session:
            async with session.delete(url) as response:
                return await response.text()

async def main():
        data = {
            "id": 30,
            "name": "Someone"
        }

        data1 = await fetcher.get("https://httpbin.org/get")
        data2 = await fetcher.post("https://httpbin.org/post",data)
        data3 = await fetcher.delete("https://httpbin.org/delete")

        res1 = json.loads(data1)
        res2 = json.loads(data2)
        res3 = json.loads(data3)

        print(json.dumps(res1, indent=6))
        print(json.dumps(res2, indent=6))
        print(json.dumps(res3, indent=6)) 

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())