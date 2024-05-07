# Напишите программу, которая создает 2 потока.
# В первом потоке будет выполняться функция, которая выводит числа от 1 до 5, во втором - функция, которая будет выводить буквы от a до e (англ.).
# Дождитесь выполнения обоих потоков и затем выведите в консоль Готово!.
#
# Для создания и запуска потоков создайте функцию main() .



import threading


def aim_func( n_start: int, n_end: int) -> None:
    for i in range(n_start,n_end + 1):
        print(i)

def letters(letters: str) -> None:
    for letter in 'abcde':
        print(letter)

def main():
    #Создайте и запустите потоки согласно условию задачи
    thred_1 = threading.Thread(target=aim_func, args=(1,5))
    thred_2 = threading.Thread(target=letters, args=('abcde',))
    thred_1.start()
    thred_2.start()

    #Дождитесь завершения потоков
    thred_1.join()
    thred_2.join()

    return True

print('Готово') if main() else None





