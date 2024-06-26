#Напишите программу, которая создает 2 потока.
# В первый поток передайте целевую функцию, которая будет выводить числа от 1 до 5 с интервалом в 0.5 секунд,
# а во второй — целевую функцию, которая будет выводить числа от 6 до 10 с интервалом 1 секунды.
# Дождитесь завершения работы обоих потоков и в главном потоке выведите:

#Оба потока завершили свою работу.



#Импортируйте все необходимое
import  threading
import time


#Создайте целевую функцию
def aim_func(time_sleep:float, n_start: int, n_end: int) -> None:
    for i in range(n_start,n_end + 1):
        print(i)
        time.sleep(time_sleep)

#Создайте и запустите потоки согласно условию задачи
thred_1 = threading.Thread(target=aim_func, args=(0.5,1,5))
thred_2 = threading.Thread(target=aim_func, args=(1,6,10))
thred_1.start()
thred_2.start()

#Дождитесь завершения потоков
thred_1.join()
thred_2.join()

#Не забудьте вывести информацию о завершении работы потоков
print('Оба потока завершили свою работу')