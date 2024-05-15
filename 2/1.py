from concurrent.futures import ThreadPoolExecutor

results = []

# Функция для преобразования строки в верхний регистр
def to_uppercase(string):
    string = string.upper()
    return string

# Создание пула потоков
with ThreadPoolExecutor(max_workers=len(strings)) as executor:
    for string in strings:
        future = executor.submit(to_uppercase,string)
        results.append(future.result())
    # Вывод результатов задач
for result in results:
    print(result)