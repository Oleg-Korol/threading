# import time
# from functools import reduce
# from concurrent.futures import ThreadPoolExecutor, TimeoutError,wait
#
# work_times = [4, 5, 3, 5, 4, 2, 5, 1, 3, 5, 3, 5, 1, 5, 5, 2, 1, 5, 1, 2]
# numbers = [[2, 5], [6, 2], [9, 4], [2, 2], [2, 8], [3, 5], [4, 1], [6, 2],
#            [7, 4], [9, 7], [5, 7], [3, 8], [4, 0], [8, 2], [6, 9], [9, 7],
#            [3, 6], [6, 7], [2, 5], [7, 3]]
# def my_task(numbers:list, delay:int):
#     time.sleep(delay)
#     return reduce(lambda x,y: x*y,numbers) if delay%2==0 else  sum(numbers)
#
# def main():
#     with ThreadPoolExecutor(max_workers=len(numbers)) as executor:
#         try:
#             results = [executor.submit(my_task,list_numbers,delay) for list_numbers,delay in zip(numbers,work_times)]
#             results_good, results_bad = wait(results,2.5)
#             [print(res.result()) for res in results_good]
#         except TimeoutError:
#             pass
# main()

import time
from functools import reduce
from concurrent.futures import ThreadPoolExecutor, TimeoutError,wait

work_times = [4, 5, 3, 5, 4, 2, 5, 1, 3, 5, 3, 5, 1, 5, 5, 2, 1, 5, 1, 2]
numbers = [[2, 5], [6, 2], [9, 4], [2, 2], [2, 8], [3, 5], [4, 1], [6, 2],
           [7, 4], [9, 7], [5, 7], [3, 8], [4, 0], [8, 2], [6, 9], [9, 7],
           [3, 6], [6, 7], [2, 5], [7, 3]]

def my_task(numbers:list, delay:int):
    time.sleep(delay)
    return reduce(lambda x,y: x*y,numbers) if delay % 2==0 else  sum(numbers)

def main():
    with ThreadPoolExecutor(max_workers=len(numbers)) as executor:
        try:
            results = [executor.submit(my_task,n,d) for n,d in zip(numbers,work_times)]
            results_good, results_bad = wait(results,2.5)
            [print(f'({res} : {res.result()}') for res in results_good]
        except TimeoutError:
            pass
main()