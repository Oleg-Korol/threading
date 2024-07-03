import threading
import time
from random import choice, randint
from threading import Condition, local
from queue import Queue

data = local()

# Списки официантов, поваров и блюд
waiters = ["Анна", "Иван", "Света"]
chefs = ["Шеф_Антон", "Шеф_Сергей", "Шеф_Георгий"]
dishes = ["Борщ", "Салат Цезарь", "Стейк", "Паста Карбонара", "Тирамису"]

# Создаем объект условия
condition =Condition()
my_queue = Queue()
count_dishes_done = 0
l_dishes = len(dishes)

# Функция для официанта (главного потока)
def waiter(waiter_name):
    data.count_dish = 0
    while data.count_dish != 3:
        if dishes:
            with condition:
                dish = choice(dishes)
                dishes.remove(dish)
                my_queue.put(dish)
                data.count_dish += 1
                print(f"{waiter_name} передал заказ на {dish}")
            time.sleep(randint(1, 3))
        else:
            break


# Функция для повара (рабочего потока)
def chef(chef_name):
    global count_dishes_done
    data.count = 0
    while data.count!=3:
        if l_dishes == count_dishes_done:
            break
        elif not my_queue.empty():
            with condition:
                dish = my_queue.get()
                print(f"{chef_name} готовит {dish}...")
            time.sleep(randint(1, 3))
            print(f"{chef_name} закончил готовить {dish}")
            data.count+=1
            count_dishes_done += 1


# Создаем и запускаем потоки официантов и поваров
waiter_threads = [threading.Thread(target=waiter, args=(w,)) for w in waiters]
chef_threads = [threading.Thread(target=chef, args=(c,)) for c in chefs]

for thread in waiter_threads:
    thread.start()

for thread in chef_threads:
    thread.start()

for thread in waiter_threads:
    thread.join()

for thread in chef_threads:
    thread.join()



# Запускаем и ожидаем все потоки