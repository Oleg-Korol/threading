import math
import time
from concurrent.futures import ThreadPoolExecutor

def square_factorial_number(num):
    print(f'Обработка числа {num} началась')
    time.sleep(num/10)
    return math.factorial(num) if num<=7 else pow(num,2)

executor = ThreadPoolExecutor(max_workers=7)
resalts = executor.map(square_factorial_number,[19, 1, 4, 13, 10, 7, 16])
executor.shutdown()
print(f'Сумма обработанных чисел равна {sum(resalts)}')