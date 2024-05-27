import time
from threading import current_thread
from concurrent.futures import ThreadPoolExecutor

# Список для хранения сообщений
result_lst =[]

# Список уникальных ID для потоков
unique_task_ids = ['StarExplorer42', 'QuantumLeap89', 'CyberWizard77',
                     'GalacticVoyager66', 'MysticCoder11', 'NeuralNinja53',
                     'QuantumRanger88', 'SpaceSurfer15', 'TimeTraveler23',
                     'CosmicSage99']

# Функция инициализации для потоков
def thread_initializer():
    print(f"Инициализация потока {current_thread().name}")

# Функция, выполняемая потоками
def thread_task(task_id):
    time.sleep(1)
    result_lst.append(f"Поток {current_thread().name} выполняет задачу {task_id}")

# Создание пула потоков с функцией инициализации
with ThreadPoolExecutor(max_workers=3, initializer=thread_initializer) as executor:
    [executor.submit(thread_task, ids) for ids in unique_task_ids]

# Вывод списка с результатами работы потоков
for res in result_lst:
    print(res)