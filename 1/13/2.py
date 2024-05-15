import threading

astronauts = ["Алексей Леонов", "Юрий Гагарин", "Джон Гленн"]
tasks = ["Ремонт оборудования", "Проведение экспериментов", "Мониторинг систем"]
intervals = [0.7, 1.3, 1.8]

def action(name,task):
    print(f'{name} выполняет задачу: {task}')

def main():
    for name,task,interval in zip(astronauts,tasks,intervals):
        timer = threading.Timer(interval,action,args=(name,task))
        timer.start()

main()