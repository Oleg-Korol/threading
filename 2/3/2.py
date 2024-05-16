# Напишите свой код
from concurrent.futures import ThreadPoolExecutor

numbers = [2, 17, 8, 11, 14, 5]

def number_square(num):
    res = pow(num, 2)
    return res

def main():
    with ThreadPoolExecutor(max_workers=2) as executor:
        results = executor.map(number_square,numbers)

        [print(res) for res in results]

main()