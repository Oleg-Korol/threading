from math import factorial
from concurrent.futures import ThreadPoolExecutor

small =[1,2,3]
medium =[1,2,3,4,5]
large =[1,2,3,4,5,6,7,8]
results_small =[]
results_medium =[]
results_large =[]

# Функции для обработки чисел
def square(number):
    return pow(number,2)

def cube(number):
    return pow(number,3)

def my_factorial(number):
    return factorial(number)

# Функция для обработки числа с использованием заданной функции
def process_number(number, function):
    return {number: function(number)}

def main():
    for list_elements,func,name in zip([small,medium,large],[square,cube,my_factorial],[results_small,results_medium, results_large]):
        with ThreadPoolExecutor(max_workers=len(list_elements)) as executor:
            results  = [executor.submit(process_number,number,func) for number in list_elements]
            name.extend([res.result() for res in results])

main()



# Вывод результатов
print("Результаты для маленьких чисел (возведение в квадрат):")
for result in results_small:
    print(result, flush=True)

print("\nРезультаты для средних чисел (возведение в куб):")
for result in results_medium:
    print(result, flush=True)

print("\nРезультаты для больших чисел (факториал):")
for result in results_large:
    print(result, flush=True)