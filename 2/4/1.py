import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError

data = [("asdf", 0.7), ("ghjk", 1.4), ("zxcl", 3.2), ("vbnm", 4.1), ("poiu", 2.7), ("ytre", 0.3), ("wqsx", 1.1)]
data = sorted(data,key=lambda x:x[1])
def my_task(name, time_work):
    time.sleep(time_work)
    return name

def main():
    with ThreadPoolExecutor(max_workers=len(data)) as executor:
        try:
            results = executor.map(lambda x: my_task(*x), data, timeout=1.5)
            for res in results:
                print(res)
        except TimeoutError:
            pass

main()
