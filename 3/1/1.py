import concurrent
import time
from concurrent.futures import ThreadPoolExecutor, wait

timeouts = [4, 5, 3, 5, 4, 2, 5, 1, 3, 5, 3, 5, 1, 5, 5, 2, 1, 5, 1, 2]
numbers = [2257, 6217, 6594, 2259, 5284, 3568, 1741, 5462, 7494, 8971, 3157, 3998, 2040, 8828, 8769, 6976, 9367, 1267, 6255, 7322]
def process_number(timeout, number):
    time.sleep(timeout)
    return number

def main():
    with ThreadPoolExecutor(len(timeouts)) as executor:
            futures = [executor.submit(process_number,delay,number) for delay, number in zip(timeouts,numbers)]
            done, _ = wait(futures, timeout=3)
            return sum(res.result() for res in done)

print(main())
