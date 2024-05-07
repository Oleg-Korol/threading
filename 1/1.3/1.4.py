import threading
import time

# Напишите необходимые функции для вычисления суммы и произведения
total_sum = 0
total_mult = 1
def sum_numbeers(numbers = 1000):
    global total_sum
    for n in range(1, numbers + 1):
        total_sum += n


def multiply_numbers(numbers = 10):
    global total_mult
    for i in range(1, numbers):
        total_mult += total_mult * i


# Создайте и запустите потоки с целевыми функциями
thred_1 = threading.Thread(target=sum_numbeers)
thred_1.start()


thred_2 = threading.Thread(target=multiply_numbers)
thred_2.start()
thred_2.join()

# Выведите результаты работы потоков согласно условиям задачи
print(f"Сумма чисел от 1 до 1000: {total_sum}\n"
      f"Произведение чисел от 1 до 10: {total_mult}")