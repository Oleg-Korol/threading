import threading

def write_to_file_without_lock(file_name, number):
    with open(file_name, 'a') as f:
        f.write(f"{number}\n")
    print(f"Записано число {number}")

# Имя файла для записи
file_name = "numbers_without_lock.txt"

# Очистка файла перед записью
with open(file_name, 'w') as f:
    pass

# Создание и запуск 5000 потоков
for i in range(5000):
    threading.Thread(target=write_to_file_without_lock, args=(file_name, i)).start()



