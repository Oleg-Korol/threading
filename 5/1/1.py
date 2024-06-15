import threading
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
import time

cooks_names = ["Алексей", "Марина", "Сергей", "Ирина", "Николай"]

pizzas = {
    "Маргарита": 3,
    "Пепперони": 2,
    "Вегетарианская": 4,
    "Четыре сыра": 5,
    "Гавайская": 3
}

lock = threading.Lock()

def cooker(shef,pizza_info):
    with lock:
        pizza_name, delay = pizza_info
        print(f'{shef} начал(а) готовить пиццу "{pizza_name}".')
        time.sleep(delay)
        print(f'{shef} закончил(а) готовить пиццу "{pizza_name}".')

def main():
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = executor.map(cooker,cooks_names,pizzas.items())
        futures = list(futures)
        print("Все пиццы приготовлены!")

main()







