import math
from concurrent.futures import ThreadPoolExecutor

# Функция для вычисления числа Фибоначчи
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


# Функция для вычисления суммы квадратных корней чисел в диапазоне
def sum_of_square_roots(start, end):
    total =0
    for num in range(start,end + 1):
        total+= math.sqrt(num)
    return total


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)



# Создайте пул потоков
with ThreadPoolExecutor(max_workers=3) as exucuter:
    # Отправка задач в пул потоков
    fib_result =  exucuter.submit(fibonacci, 20).result() # Например, вычисляем 20-е число Фибоначчи
    sqrt_result = exucuter.submit(sum_of_square_roots, 1, 50).result() # Сумма квадратных корней чисел от 1 до 50
    fact_result =  exucuter.submit(factorial, 20).result() # Факториал числа 20

    # Получение и вывод результатов задач
    print(f"20-е число Фибоначчи: {fib_result}")
    print(f"Сумма квадратных корней чисел от 1 до 50: {sqrt_result}")
    print(f"Факториал числа 20: {fact_result}")