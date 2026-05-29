import httpx
import asyncio


async def fetch_data():   #this function is special it can pause and do something like getting a data
    async with httpx.AsyncClient() as client:
        response =await client.get("https://httpbin.org/get")
        print(response.status_code)
        print(response.json())

asyncio.run(fetch_data())

#200 means request is sucessful