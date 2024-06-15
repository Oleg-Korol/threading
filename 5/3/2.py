from concurrent.futures import ThreadPoolExecutor, wait,ALL_COMPLETED
import time
from threading import Event

# Событие для старта аукциона
auction_start =Event()
# Имена участников аукциона
bidder_names = ["Сергей", "Борис", "Виктор", "Евдоким", "Егор"]

# Функция, представляющая участника аукциона
def bidder(name):
    print(f"Участник {name} готов к аукциону.")
    auction_start.wait()
    print(f"Участник {name} делает ставку на редкую картину.")

# Создание потоков-участников и запуск потоков
def main():
    print("Аукцион начинается!")
    with ThreadPoolExecutor(max_workers=len(bidder_names)) as executor:
        futures = [executor.submit(bidder,name) for name in bidder_names]
        time.sleep(3)
        auction_start.set()
        wait(futures, return_when=ALL_COMPLETED)

main()