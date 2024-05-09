import threading

def process_data(i):
    thread_data.data = f'{i}'
    print(f"Данные в локальном хранилище: {thread_data.data}")

thread_data = threading.local()
threads = []

for i in range(3):
    thread = threading.Thread(target=process_data, args=('HELLO LOCAL STORAGE!',))
    threads.append(thread)
    thread.start()

for trd in threads:
    trd.join()