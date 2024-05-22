import math
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

numbers=[5, 4, 7, 6, 3]

def factorial(number):
    time.sleep(number/10)
    return (number, math.factorial(number))

def main():
    with ThreadPoolExecutor(max_workers=len(numbers)) as executor:
            results = [executor.submit(factorial, n) for n in numbers]
            for future in as_completed(results):
                n, f = future.result()
                print(f'Факториал числа {n} равен {f}')

main()