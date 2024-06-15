from concurrent.futures import ThreadPoolExecutor, wait,ALL_COMPLETED
import time
from threading import Event

clients = ["Виктор", "Ирина", "Андрей"]


def bank(event, client):
    print(f'{client} вошел в банк')
    event.wait()
    event.clear()
    cashier(event, client)
    print(f'{client} обслужен и покидает банк')
    event.set()


def cashier(event, client):
    print(f'Обслуживаю клиента {client}')
    time.sleep(1)
    print(f'Клиент {client} обслужен')


def main():
    event = Event()
    with ThreadPoolExecutor() as executor:
        event.set()
        futures = [executor.submit(bank, event, client) for client in clients]
        wait(futures, return_when=ALL_COMPLETED)

    print("Все клиенты обслужены. Банк закрывается.")


if __name__ == "__main__":
    main()