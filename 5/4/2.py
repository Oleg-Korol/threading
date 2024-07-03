import threading
import time
from threading import Condition
from queue import Queue

clients = ["Алиса", "Владимир", "Сергей"]

class Coffe():
    condition = Condition()
    my_queue = Queue()

    def barista(self):
        while not self.my_queue.empty():
            with self.condition:
                client = self.my_queue.get()
                print(f'Готовим кофе для {client}')
                time.sleep(2)
                print(f'Кофе для {client} готов')
                time.sleep(1)


    def client(self, clients:list):
        for name in clients:
            with self.condition:
                print(f'{name} зашел в кафе')
                self.my_queue.put(name)
            time.sleep(1)


day = Coffe()
thread1 = threading.Thread(target=day.client, args=(clients,))
thread1.start()
thread2 = threading.Thread(target=day.barista)
thread2.start()

with Coffe.condition.wait_for(lambda : day.my_queue.empty()==True):
    print(f'Все посетители получили свой кофе. Работа завершена.')
