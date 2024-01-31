import multiprocessing
import time
from random import randint

def sum_arr(sub_arr, return_dict, index):
    local_start_time = time.time()
    sum_sub = sum(sub_arr)
    local_end_time = time.time()
    return_dict[index] = (sum_sub, local_end_time - local_start_time)

if __name__ == '__main__':
    n_element = 1000000
    n_processes = 101
    arr = [randint(1, 100) for _ in range(n_element)]

    manager = multiprocessing.Manager()
    return_dict = manager.dict()

    processes = []
    for i in range(n_processes):
        start = i * (n_element // n_processes)
        end = start + (n_element // n_processes)
        sub_arr = arr[start:end]
        p = multiprocessing.Process(target=sum_arr, args=(sub_arr, return_dict, i))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    total_sum = 0
    for i in range(n_processes):
        total_sum += return_dict[i][0]
        print(f"Процесс {i}: Время выполнения - {return_dict[i][1]} секунд.")

    print("Сумма элементов массива:", total_sum)


