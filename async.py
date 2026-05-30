import asyncio,  aiofiles

#coroutine is a blueprint 

"""


import httpx
import asyncio


async def fetch_data():   #this function is special it can pause and do something like getting a data
    async with httpx.AsyncClient() as client:
        response =await client.get("https://httpbin.org/get")
        print(response.status_code)
        print(response.json())

asyncio.run(fetch_data())


async def some_function():
    print("start")
    await asyncio.sleep(3)
    print("finished")

asyncio.run(some_function())


"""
#200 means request is sucessful


#Downloading stuff reading 

#reading files 

async def read_file_async(filename):
    async with aiofiles.open(filename,mode='r') as f:
        contents =await f.read()
        print(contents)

async def main():
    await read_file_async('C:\\Users\\armin\\Desktop\\whatevr\\example.txt')


asyncio.run(main())

#fetching user information or check status 




async def information_gathering(user_id):
    name= await asyncio.sleep(3)
    print('complited')


#async func dont return immediately , evnt loop is asyncio.run sets up an event loop that runs the coroutine

asyncio.run(information_gathering("as"))