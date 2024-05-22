from concurrent.futures import ThreadPoolExecutor

numbers = [1,2,300,301,43,544,65,34,232,111,435,88,888,999,6,664]
numbers_sort = {'от 1 до 300':[],'от 301 до 500':[],'от 501 до 700':[],'от 701 до 999':[]}

def sort_numbers(num):
    if 1<=num<=300:
        numbers_sort['от 1 до 300'].append(num)
    elif 301 <= num <= 500:
        numbers_sort['от 301 до 500'].append(num)
    elif 501 <= num <= 700:
        numbers_sort['от 501 до 700'].append(num)
    elif 701 <= num <= 999:
        numbers_sort['от 701 до 999'].append(num)

def main():
    with ThreadPoolExecutor(max_workers=len(numbers)) as executor:
        executor.map(sort_numbers,numbers)
    for diapason, collection in numbers_sort.items():
        collection.sort()
        print(f"Числа в массиве {diapason} {collection}")

main()