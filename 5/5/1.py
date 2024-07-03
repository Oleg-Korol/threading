import threading
from threading import Semaphore

name_list = [
    "Клиент Веселый Шутник",
    "Клиент Читающий Поэт",
    "Клиент Спешащий Бизнесмен",
    "Клиент Мечтающий Путешественник",
    "Клиент Меланхоличный Художник",
    "Клиент Загадочная Улыбка",
    "Клиент Задумчивый Философ",
    "Клиент Вечно Опаздывающий",
    "Клиент Гадающий на Кофейной Гуще",
    "Клиент Неугомонный Блогер"
]


def client(semaphore, client_name):
    with semaphore:
        print(f"{client_name} нашел свободный столик и заказывает кофе")
        print(f"{client_name} насладился кофе и освобождает столик для следующих гостей")


def main():
    semaphore = Semaphore(3)
    for client_name in name_list:
        thread = threading.Thread(target=client, args=(semaphore, client_name,))
        thread.start()

if __name__== '__main__':
    main()
