import threading
import time

def flight_simulation(model:str, flight_time:int):
    print(f"{model} начал полет. Время полета: {flight_time} сек.")
    time.sleep(flight_time)
    print(f"{model} завершил полет.")


def main():
    for model, flight_time in aircrafts.items():
        thread = threading.Thread(target=flight_simulation, args=(model,flight_time))
        thread.start()
    time.sleep(5)
    print(f"Количество активных потоков после 5 секунд: {threading.active_count()}")

main()