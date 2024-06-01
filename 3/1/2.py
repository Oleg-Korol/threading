from  concurrent.futures import ThreadPoolExecutor
from functools import reduce
from operator import mul

list1 = [16,10,7]
list2 = [0,7,9]
list3 = [8,19,3]
list4 = [1,0,9]

def  multiply(numbs):
    if 0 in numbs:
        raise ValueError("Обнаружено умножение на ноль")
    else:
        return reduce(mul, numbs)

def main():
    with ThreadPoolExecutor(len(list1)) as executor:
        for numbs in zip(list1,list2,list3,list4):
            try:
                res = executor.submit(multiply,numbs)
                print(f"Результат: {res.result()}")
            except ValueError as e:
                print((f"Обработано исключение: {e}"))

main()

