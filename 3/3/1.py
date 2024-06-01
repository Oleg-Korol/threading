from concurrent.futures import ThreadPoolExecutor
import time

data = [(1, "Python"), (2, "Java"), (3, "Go"), (4, "JavaScript"), (5, "C++"),
        (6, "TypeScript"), (7, "PHP"), (8, "Ruby"), (9, "C"), (10, "C#")]

def task(reiting_number, name_language):
    time.sleep(reiting_number/10)
    return f'{name_language} на {reiting_number}-м месте на GitHub в первом квартале 2024 года'

with ThreadPoolExecutor() as executor:
    futures = executor.map(lambda x:task(*x),data)
    [print(res) for res in futures]