import os
import time
import zipfile
import wget
from bs4 import BeautifulSoup
from os import path
import requests
from threading import Lock
from concurrent.futures import ThreadPoolExecutor

class Analiz:

    def __init__(self):
        self.__total = 0
        self.lock_total = Lock()
        self.lock_list_files = Lock()
        self.lock_files_txt = Lock()
        self.lock_links_list = Lock()
        self.new_download_files = []
        self.files_txt_list = []
        self.links_list = []
        self.flag = True

    def get_total_words(self)->int:
        "Получить общее количество слов"
        return self.__total


    def download_zip_file(self, url: str) -> str:
        "Скачать zip файл"
        try:
            file_name = wget.download(url)
            with self.lock_list_files:
                self.new_download_files.append(file_name)
            return file_name
        except Exception as err:
            print(err)

    def open_zip(self, file_name: str)->None:
        "Распаковать zip файл в формат txt"
        try:
            if path.exists(file_name):
                with zipfile.ZipFile(file_name, "r") as zf:
                    zf.extractall("extracted_files")
                    with self.lock_files_txt:
                        self.files_txt_list.extend(zf.namelist())
        except Exception as err:
            print(err)

    def read_files(self, file_name: str)->None:
        "Читать txt файл"
        current_dir = os.getcwd()
        file_path = f'{current_dir}/extracted_files/{file_name}'
        if path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                links = file.readlines()
                with self.lock_links_list:
                    self.links_list.extend(links)

    def read_content(self, content: str)->int:
        "Прочитать текстовый фаил. Возвращает количество слов в файле"
        try:
            soup = BeautifulSoup(content, 'html.parser')
            text = soup.get_text()
            count = len(text.split())
            return count
        except AttributeError as err:
            print(err)

    def request_url(self, url):
        "Сделать запрос по url"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                count_words = self.read_content(response.text)
                with self.lock_total:
                    self.__total += count_words
            return None
        except requests.ConnectTimeout as err:
            print(err)

    def worker(self, urls):
        "Запустить выполнение потоков"
        with ThreadPoolExecutor(max_workers=16) as executor:
            futures = []
            if urls:
                futures += [executor.submit(self.download_zip_file, url) for url in urls]
                urls = None
                time.sleep(2)
            while self.flag:
                    if self.new_download_files:
                        with self.lock_list_files:
                            futures += [executor.submit(self.open_zip, file_name) for file_name in self.new_download_files]
                            self.new_download_files = []
                    if self.files_txt_list:
                        with self.lock_files_txt:
                            futures += [executor.submit(self.read_files, file_name) for file_name in self.files_txt_list]
                            self.files_txt_list = []
                    if self.links_list:
                        with self.lock_links_list:
                            futures += [executor.submit(self.request_url, link.strip()) for link in self.links_list]
                            self.links_list = []
                    if not self.links_list and not self.new_download_files and not self.files_txt_list and all(f.done() for f in futures):
                        self.flag = False

        return self.__total


if __name__ == "__main__":
    analize = Analiz()
    res = analize.worker(['https://stepik.org/media/attachments/lesson/1165153/generated_links_6.1.zip',])
    print(res)


