from concurrent.futures import ThreadPoolExecutor, as_completed

fifty = ['OF95RK', 'VH61DX','JF39XW', 'RO06QB', 'RW48XW' ]
one_hundred = ['JF39XW', 'RO06QB', 'RW48XW']
two_hundred = ['FP99WI', 'IJ21HS', 'SV16JN', 'EP11JG']

# Функция для вывода сообщения
def process_element(elem, pool_size):
    print(f"Элемент {elem} списка из пула размером {pool_size}", flush=True)


# Функция для создания и использования пула потоков
def process_with_threadpool(elements, pool_size):
    with ThreadPoolExecutor(max_workers=pool_size) as executor:
            for el in elements:
                executor.submit(process_element,el,pool_size)
            executor.shutdown(wait=True)

# Обработка списков с разными размерами пулов
process_with_threadpool(fifty, 2)
process_with_threadpool(one_hundred, 3)
process_with_threadpool(two_hundred, 1)