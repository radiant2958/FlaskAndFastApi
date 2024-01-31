import asyncio
from random import randint
import time

async def sum_arr(sub_arr, index):
    start_time = time.time()
    await asyncio.sleep(0.1)  # Имитация асинхронной задержки
    sum_sub_arr = sum(sub_arr)
    end_time = time.time()
    return index, sum_sub_arr, end_time - start_time

async def main():
    n_element = 1000000
    n_tasks = 100
    arr = [randint(1, 100) for _ in range(n_element)]

    tasks = []
    for i in range(n_tasks):
        start = i * (n_element // n_tasks)
        end = start + (n_element // n_tasks)
        sub_arr = arr[start:end]
        tasks.append(asyncio.create_task(sum_arr(sub_arr, i)))

    results = await asyncio.gather(*tasks)

    total_sum = 0
    for index, sum_sub_arr, duration in results:
        print(f"Задача {index}: Время выполнения - {duration:.4f} секунд.")
        total_sum += sum_sub_arr

    print("Сумма элементов массива:", total_sum)

if __name__ == "__main__":
    asyncio.run(main())
