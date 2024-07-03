import threading
import time
from threading import Barrier

employee_times = {
    'Алиса': 4.44,
    'Боб': 7.33,
    'Чарли': 7.75,
    }

def start():
    print("Совещание началось!")

def team_meeting(barrier, name, time_to_arrive):
    print(f'{name} начал(а) идти на совещание.')
    time.sleep(time_to_arrive)
    print(f'{name} прибыл(а) на совещание, затратив {time_to_arrive} секунд.')
    barrier.wait()

def main():
    barrier = Barrier(len(employee_times), action= start)
    for employee, time_to_arrive in employee_times.items():
        thread = threading.Thread(target=team_meeting, args=(barrier, employee, time_to_arrive))
        thread.start()

main()