from  concurrent.futures import ThreadPoolExecutor
from  sklad import inventory

def answer(future):
    item_id, remaining, flag = future.result()
    if not flag:
        print(f"Товара {item_id} нет в наличии, обработка невозможна.")
    else:
        print(f"Товар отправлен получателю {item_id}. Осталось {remaining}")

def task(item_id):
    print(f"Поиск товара {item_id}. Количество на складе: {inventory[item_id]} шт")
    if inventory[item_id]:
        inventory[item_id] = inventory[item_id] - 1
        return  item_id, inventory[item_id], True
    return item_id, inventory[item_id], False

with ThreadPoolExecutor(max_workers=len(inventory)) as executor:
    futures = []
    for k, count_items in inventory.items():
            future = executor.submit(task, k)
            future.add_done_callback(answer)
            futures.append(future)