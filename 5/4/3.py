import threading
import time
from queue import Queue

clients = ["Алиса", "Владимир", "Сергей"]

class CoffeeShop:
    def __init__(self):
        self.condition = threading.Condition()
        self.my_queue = Queue()
        self.clients_done = False

    def barista(self):
        while True:
            with self.condition:
                while self.my_queue.empty() and not self.clients_done:
                    self.condition.wait()
                if self.my_queue.empty() and self.clients_done:
                    break
                client = self.my_queue.get()
            print(f'Готовим кофе для {client}')
            time.sleep(2)
            print(f'Кофе для {client} готов')
            print(f'{client} получил свой кофе')
            time.sleep(1)

    def client(self, clients_list):
        for name in clients_list:
            with self.condition:
                print(f'{name} зашел в кафе')
                self.my_queue.put(name)
                self.condition.notify_all()
            time.sleep(1)

        with self.condition:
            self.clients_done = True
            self.condition.notify_all()

day = CoffeeShop()
thread1 = threading.Thread(target=day.client, args=(clients,))
thread2 = threading.Thread(target=day.barista)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print('Все посетители получили свой кофе. Работа завершена.')
