import time
from concurrent.futures import ThreadPoolExecutor

data = {1.4: 'ljeo', 0.4: 'akwx', 2.3: 'tydx', 2.7: 'qnai', 2.6: 'smgx',
        1.9: 'fhef', 1.6: 'wzag', 2.5: 'hjsz', 2.4: 'gpay', 0.5: 'wxco'}

def task(item):
    delay, task_name =  item
    time.sleep(delay)
    print(f'Задача {task_name} выполнилась.')

with ThreadPoolExecutor(max_workers=5) as executor:
    futures = {executor.submit(task, item):item[0]  for item in data.items()}
    for future in futures:
        if not future.running() and int(str(futures.get(future))[-1])%2 != 0:
            future.cancel()

