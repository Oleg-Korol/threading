import queue
import threading
import time

def get_element(q):
    while not q.empty():
        priority, el = q.get()
        time.sleep(priority / 100)
        print(f'Обработан {el}')
        q.task_done()

def add_element(q, electronix):
    while electronix:
        el = electronix.pop()
        q.put(el)


def main():
    q = queue.PriorityQueue(maxsize=5)

    electronics = [(1, "смартфон"), (15, "ноутбук"), (7, "планшет"), (33, "камера"), (67, "гарнитура"),

                   (4, "телевизор"), (21, "гаджет"), (83, "монитор"), (0, "роутер"), (47, "плеер")]
    electronics.reverse()

    thread = threading.Thread(target=add_element, args=(q, electronics), daemon=True)
    thread.start()

    for _ in range(2):
        threading.Thread(target=get_element, args=(q,), daemon=True).start()

    thread.join()
    q.join()

if __name__ == "__main__":
    main()