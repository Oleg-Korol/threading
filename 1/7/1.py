#Импортируйте все необходимое
import threading
import time


threds = []

def aim(delay:int) -> None:
    name = threading.current_thread().name
    print(f'Поток {name} запустился.')
    time.sleep(delay)

def main() -> None:
    for name_thred, delay in zip(['A','B'],[2,3]):
        thred = threading.Thread(target = aim, args=(delay,), name=name_thred)
        threds.append(thred)
        thred.start()

main()

time.sleep(2.2)
for trd in threds:
    if trd.is_alive():
        print(f'Поток {trd.name} не завершился за установленное время.')