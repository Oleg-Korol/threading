import queue
import threading


word_count = 0
number_of_lines =0

def count_word(q):
    global word_count
    while not q.empty():
        file_name = q.get()
        with open(file_name, 'r', encoding = 'utf-8') as file:
            text = file.read()
            word_count += len(text.split())
            q.task_done()


def count_str(q2):
    global number_of_lines
    while not q2.empty():
        file_name = q2.get()
        with open(file_name, 'r', encoding = 'utf-8') as file:
            text = file.readlines()
            number_of_lines += len(text)
        q2.task_done()

def main():
    q = queue.Queue(maxsize=3)
    q2 = queue.Queue(maxsize=3)
    for n in range(1,4):
        q.put(f'file{n}.txt')
        q2.put(f'file{4 - n}.txt')

    tread1 = threading.Thread(target=count_word,args=(q,), daemon=True)
    tread1.start()

    tread2 = threading.Thread(target=count_str,args=(q2,), daemon=True)
    tread2.start()

    tread1.join()


    print(word_count, number_of_lines)

if __name__ == '__main__':
    main()


