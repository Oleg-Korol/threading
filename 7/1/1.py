import os
import threading
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

    def add_thread(self):
        while True:
            if self.new_download_files:
                with self.lock_list_files:
                    file_name = self.new_download_files.pop()
                    with ThreadPoolExecutor(max_workers=5) as executor:
                        executor.submit(self.new_download_files, args = (file_name,))

    def download_zip_file(self,url:str) ->str:
        "Download zip file"
        try:
            file_name =  wget.download(url)
            print(file_name)
            with self.lock_list_files :
                self.new_download_files.append(file_name)
            return file_name
        except Exception as err:
            print(err)


    def open_zip(self, file_name:str) ->list:
        "Extract zip file to txt format"
        try:
            if path.exists(file_name):
                with zipfile.ZipFile(file_name, "r") as zf:
                    zf.extractall("extracted_files")
                    with self.lock_files_txt:
                        self.files_txt_list.extend(zf.namelist())
        except Exception as err:
                print(err)


    def read_files(self,file_name:str):
        "Read txt file"
        current_dir = os.getcwd()
        file_name = f'{current_dir}/extracted_files/{file_name}'
        if path.exists(file_name):
            with open(file_name, 'r', encoding='utf-8') as file:
                links = file.readlines()
                with self.lock_links_list:
                    self.links_list.extend(links)


    def read_content(self,content:str):
        "Read content"
        try:
            soup = BeautifulSoup(content, 'html.parser')
            text = soup.find('body').text
            count = len(text.split())
            with self.lock_total:
                self.__total += count
            return 1
        except AttributeError:
            return 0

    def request_url(self, url):
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                count_words = self.read_content(response.text)
                return count_words
            return None
        except requests.ConnectTimeout:
            return 0


    def worker(self, urls):

        while self.flag :
            with ThreadPoolExecutor(max_workers=15) as executor:
                if urls:
                    print('0')
                    [executor.submit(self.download_zip_file, args = (url,)) for url in urls]
                    urls = None
                if self.new_download_files:
                    with self.lock_list_files:
                            print('1')
                            [executor.submit(self.open_zip, args = (file_name,)) for file_name in self.new_download_files]
                            self.new_download_files =[]
                if self.files_txt_list:
                    with self.lock_files_txt:
                            print('2')
                            [executor.submit(self.read_files, args = (file_name,)) for file_name in self.lock_files_txt]
                            self.lock_files_txt = []
                if self.links_list:
                    with self.lock_links_list:
                            [executor.submit(self.request_url, args =(link, )) for link in self.self.links_list]
                            self.links_list = []
                if not self.links_list and self.lock_links_list and self.links_list:
                    self.flag = False




analiz = Analiz()
x= analiz.worker(['https://stepik.org/media/attachments/lesson/1165153/generated_links_6.1.zip',])
print('end')