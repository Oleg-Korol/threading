import queue
import threading
import time

elements = ['телевизор', 'холодильник', 'микроволновка', 'утюг', 'чайник',
            'пылесос', 'стиральная машина', 'кофеварка', 'фен', 'утюг']

def add_item(q):
    for item in elements:
        q.put(item)
        time.sleep(0.5)
        print(f'Добавлен: {item}')
    print(f'Все элементы добавлены')

def get_item(q):
    while True:
        try:
            item = q.get()
        except queue.Empty:
            continue
        else:
            print(f'Извлечен: {item}')
            time.sleep(1)
            q.task_done()

def main():
    q = queue.Queue()
    tread1 = threading.Thread(target=add_item,args=(q,), daemon=True)
    tread1.start()

    tread2 = threading.Thread(target=get_item,args=(q,), daemon=True)
    tread2.start()

    tread1.join()
    q.join()

    print(f'Все элементы очереди обработаны')

if __name__ == '__main__':
    main()