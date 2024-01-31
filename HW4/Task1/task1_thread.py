import threading
import time
from random import randint



n_element = 1000000
n_threads = 100

arr = [randint(1,100) for _ in range(n_element)]


threads = []
results = [0] * n_threads  

def sum_arr(start, end, result, index):
    local_start_time = time.time()  
    sum_sub = sum(arr[start:end])
    result[index] = sum_sub
    local_end_time = time.time()  
    print(f"Поток {index}: Время выполнения - {local_end_time - local_start_time} секунд.")


for i in range(n_threads):
    start = i * (n_element // n_threads)
    end = start + (n_element // n_threads)
    t = threading.Thread(target=sum_arr, args=(start, end, results, i))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

total_sum = sum(results)

print("Сумма элементов массива:", total_sum)