from concurrent.futures import ThreadPoolExecutor, as_completed
import time

def process_number(number):
    time.sleep(0.2)  # Имитация задержки
    return number * 2

def sum_numbers(list):
    total = 0
    for number in list:
        total += process_number(number)
    return total

def main():
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(sum_numbers, list) for list in lists]

        for future in as_completed(futures):
            print(f"Сумма чисел в первом обработанном списке: {future.result()}")
            break

main()
