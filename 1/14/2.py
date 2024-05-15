import  threading
import time

delays = [1,2,3,4,5]

def my_task(delay:int):
    name_trd = threading.current_thread().name
    print(f'Поток {name_trd} начал работу')
    time.sleep(delay)
    print(f'Поток {name_trd} завершил работу')

def main():
    for delay in delays:
        thread = threading.Thread(target=my_task, args=(delay,))
        thread.start()

    time.sleep(1.5)
    for active_thread in threading.enumerate():
        print(f'{active_thread.name} еще выполняется')

main()

