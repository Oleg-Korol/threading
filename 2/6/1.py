
import time
from concurrent.futures import ThreadPoolExecutor, TimeoutError,wait

data = [("asdf", 0.7), ("ghjk", 1.4), ("zxcl", 3.2), ("vbnm", 4.1), ("poiu", 2.7), ("ytre", 0.3), ("wqsx", 1.1)]
data = sorted(data,key=lambda x:x[1])

def my_task(name, time_work):
    time.sleep(time_work)
    return name

def main():
    with ThreadPoolExecutor(max_workers=len(data)) as executor:
        try:
            results = [executor.submit(my_task,*x) for x in data]
            results_good, results_bad = wait(results,1.5)
            [print(res.result()) for res in results_good]
        except TimeoutError:
            pass

main()

