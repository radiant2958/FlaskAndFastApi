import asyncio
import aiohttp
import time

async def download_image_async(url, session):
    start_time = time.time()
    image_name = url.split('/')[-1]
    async with session.get(url) as response:
        if response.status == 200:
            with open(image_name, 'wb') as file:
                while True:
                    chunk = await response.content.read(1024)
                    if not chunk:
                        break
                    file.write(chunk)
    end_time = time.time()
    print(f"{image_name} асинхронно скачан за {end_time - start_time:.4f} секунд.")

async def main_async(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [download_image_async(url, session) for url in urls]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    urls = []  
    start_time = time.time()
    asyncio.run(main_async(urls))
    end_time = time.time()
    print(f"Общее время асинхронного скачивания: {end_time - start_time:.4f} секунд.")
