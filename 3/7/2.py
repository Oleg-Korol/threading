from concurrent.futures import ThreadPoolExecutor

orders = [{'name': 'Ivan', 'balance': 500, 'order': 'борщ', 'Стоимость блюда': 200},
     {'name': 'User5f4a', 'balance': 117, 'order': 'суп', 'Стоимость блюда': 161},
     {'name': 'User71e3', 'balance': 749, 'order': 'борщ', 'Стоимость блюда': 213},
     {'name': 'Userecf7', 'balance': 1509, 'order': 'салат', 'Стоимость блюда': 103},
     {'name': 'Usera299', 'balance': 45, 'order': 'шашлык', 'Стоимость блюда': 106},
     {'name': 'Userf4f8', 'balance': 172, 'order': 'шашлык', 'Стоимость блюда': 121},
     {'name': 'Userc6fd', 'balance': 71, 'order': 'борщ', 'Стоимость блюда': 51}]


def process_order(order):
    if order.get('balance') < order.get('Стоимость блюда'):
        raise ValueError(f"Недостаточно средств для заказа {order['order']} пользователя {order['name']}")
    else:
        return f"Заказ {order['order']} пользователя {order['name']} успешно обработан"

with ThreadPoolExecutor(max_workers=len(orders)) as executor:
    futures = [executor.submit(process_order, order) for order in orders]
    for future in futures:
        try:
            res = future.result()
            print(res)
        except ValueError as err:
            print(err)



