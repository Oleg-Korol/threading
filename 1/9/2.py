import threading
import time

students_info = {'Варлаам Бирюкова': {'Возраст': 25, 'Специальность': None, 'Город': None, 'Страна': 'Россия',
                                      'Университет': 'ЗАО «Миронова-Прохоров»', 'Курс': 3, 'Группа': 'CK008',
                                      'Электронная почта': 'ostaplitkin@example.com', 'Телефон': None,
                                      'Дата рождения': '2005-08-22', 'Пол': 'Женский',
                                      'Хобби': ['Физика', 'Астрономия'], 'Время обработки': 6},
                 'Никандр Мамонтов': {'Возраст': 20, 'Специальность': 'Компьютерные науки',
                                      'Город': 'к. Октябрьский (Башк.)', 'Страна': 'Россия', 'Университет': None,
                                      'Курс': 3, 'Группа': 'LE057', 'Электронная почта': 'jakub_2001@example.org',
                                      'Телефон': '+7 919 424 9512', 'Дата рождения': '2002-01-13', 'Пол': None,
                                      'Хобби': None, 'Время обработки': 5},}
local_storage = threading.local()
list_threads = []
res = []


def thread_function(name, data):
    if delay := data.get('Время обработки'):
        time.sleep(delay)
    else:
        time.sleep(3)
    for key, value in data.items():
        if not value == None:
            local_storage.__dict__[key] = value
            res.append(f"Имя потока - {threading.current_thread().name}, локальные данные потока - {key}: {value}")


def main():
    for name in students_info:
        data = students_info[name]
        thread = threading.Thread(target=thread_function, name=name, args=(name, data))
        list_threads.append(thread)
        thread.start()

    for thrd in list_threads:
        thrd.join()
    for result in res:
        print(result)


main()