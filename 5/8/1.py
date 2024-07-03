from concurrent.futures import ThreadPoolExecutor
import time
import threading
from threading import Barrier
from random import randint

car_models = ["Toyota", "BMW", "Audi", "Mercedes", "Ford", "Honda", "Nissan", "Chevrolet", "Volkswagen", "Kia"]


def race(barrier,car_model):
    barrier.wait()
    race_time = randint(1,5)
    time.sleep(race_time)
    print(f"Автомобиль {car_model} финишировал за {race_time:.2f} секунд")


def main():
    barrier = Barrier(len(car_models))
    for car in car_models:
        thread = threading.Thread(target=race, args=(barrier, car))
        thread.start()

if __name__ == '__main__':
    main()