from concurrent.futures import ThreadPoolExecutor

list1 = ['kw63vdxI', 'YmSsWblC', '5OJ3Mto9']
list2 = ['7GBrUY6t', 'bfQjS3gj', 'MhTsKf0X']
list3 = ['mt05f80F', 'haHHiXoX', 'v2cYPhRO']


def worker(texts,thread_num):
    for text in texts:
        print(f"Поток {thread_num} извлёк текст из списка: {text}")

def main():
    with ThreadPoolExecutor(max_workers=3) as executor:
        for i, texts in enumerate([list1, list2, list3], start=1):
            executor.submit(worker, texts, i)

main()