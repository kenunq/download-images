import asyncio
import aiohttp
import aiofiles
import datetime


async def download_image(number: int) -> None:
    print(f'start {number}')
    async with aiohttp.ClientSession() as session:
        async with session.get('https://www.python.org/static/img/python-logo.png') as response:
            if response.status == 200:
                async with aiofiles.open(f'static/image{number}.png', 'wb') as f:
                    await f.write(await response.read())
    print(f'stop {number}')


async def main(count: int) -> None:

    tasks = []

    for i in range(count):
        tasks.append(download_image(i))

    await asyncio.gather(*tasks)

    # it = AsyncIterator()
    # async for i in it:
    #     await download_image(i)


if __name__ == '__main__':
    before = datetime.datetime.now()
    asyncio.run(main(5))
    print(datetime.datetime.now() - before)
