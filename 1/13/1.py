# Допишите функцию увеличения ставки
import threading

initial_bid =  10    # Начальная ставка аукциона. С этой суммы начинается аукцион.
bid_increment = 1   # Сумма, на которую увеличивается текущая ставка на каждом шаге аукциона.
max_bid = 20   # Максимальная ставка, при достижении которой аукцион завершается.
interval = 2

current_bid = 0

def add():
    global current_bid
    current_bid += bid_increment
    if current_bid >= max_bid:
        print(f"Текущая ставка: {current_bid} у.е.")
        print('Ставок нет, аукцион завершен!')
    else:
        print(f"Текущая ставка: {current_bid} у.е.")


def increase_bid():
    global current_bid
    current_bid = initial_bid
    while current_bid < max_bid:
        timer = threading.Timer(interval=interval, function=add)
        timer.start()
        timer.join()


# Вызовите эту функцию
increase_bid()