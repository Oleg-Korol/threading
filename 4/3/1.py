import queue
import threading


def get_element(q):
    while not q.empty():
        el = q.get()
        print(f'Обработка элемента: {el}')

def main():
    data = [15, 13, 7, 19, 3, 1, 11, 5, 9, 17]
    q = queue.LifoQueue(len(data))
    for el in data:
        q.put(el)
    for _ in range(3):
        threading.Thread(target=get_element, args=(q,), daemon=True).start()

if __name__ == "__main__":
    main()