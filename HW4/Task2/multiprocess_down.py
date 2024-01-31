import requests
from multiprocessing import Pool
import time

def download_image(url):
    start_time = time.time()
    image_name = url.split('/')[-1]
    response = requests.get(url)
    if response.status_code == 200:
        with open(image_name, 'wb') as file:
            file.write(response.content)
    end_time = time.time()
    return f"{image_name} скачан за {end_time - start_time:.4f} секунд."

def download_images_multiprocess(urls):
    with Pool() as pool:
        results = pool.map(download_image, urls)
        for result in results:
            print(result)

if __name__ == "__main__":
    urls = []  
    start_time = time.time()
    download_images_multiprocess(urls)
    end_time = time.time()
    print(f"Общее время многопроцессорного скачивания: {end_time - start_time:.4f} секунд.")
