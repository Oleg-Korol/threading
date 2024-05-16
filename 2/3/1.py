# Напишите свой код
from concurrent.futures import ThreadPoolExecutor


def aim_func( n_start: int, n_end: int) -> None:
    for i in range(n_start,n_end + 1):
        print(i)

def letters(letters: str) -> None:
    for letter in letters:
        print(letter)

def main():
    with ThreadPoolExecutor(max_workers=2) as executor:
        future1 = executor.submit(aim_func,1,50)
        future2 = executor.submit(letters,'abcde')

    return True

print('Готово!') if main() else None

