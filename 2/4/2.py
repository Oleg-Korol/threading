from concurrent.futures import ThreadPoolExecutor

messages = [
    "Привет, давайте обсудим многопоточность в Python!",
    "Да, GIL - это большая проблема для многопоточности в Python.",
]

def len_letters(stroka):
    return len(stroka)

def main():
    with ThreadPoolExecutor(max_workers=len(messages)) as execute:
        results = execute.map(len_letters,messages)
        print(f"Общее количество символов в каждой строке: {list(results)}")

main()