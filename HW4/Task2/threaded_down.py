import requests
import threading
import time

def download_image(url):
    start_time = time.time()
    image_name = url.split('/')[-1]
    response = requests.get(url)
    if response.status_code == 200:
        with open(image_name, 'wb') as file:
            file.write(response.content)
    end_time = time.time()
    print(f"{image_name} скачан за {end_time - start_time:.4f} секунд.")

def download_images_thread(urls):
    threads = []
    for url in urls:
        thread = threading.Thread(target=download_image, args=(url,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    urls = []  
    start_time = time.time()
    download_images_thread(urls)
    end_time = time.time()
    print(f"Общее время многопоточного скачивания: {end_time - start_time:.4f} секунд.")
