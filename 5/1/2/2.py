import time
import json
from concurrent.futures import ThreadPoolExecutor, wait,ALL_COMPLETED
from threading import Lock

lock =Lock()

json_object = {}
json_all = []
def get_str(file_name:str):
    global json_object
    flag = 1
    with open(file_name, 'r', encoding='utf-8') as file:
        key = file_name.rstrip('.txt')
        lines = iter(file.readlines())
        while flag:
            try:
                value = next(lines).rstrip('\n')
            except StopIteration:
                flag = False
            else:
                if len(json_object)<=9:
                    with lock:
                        json_object.update({key:value})

                else:
                    with lock:
                        json_object.update({key: value})
                        append_list_json()



def append_list_json():
    global json_object
    json_all.append(json_object)
    print(json_object)
    json_object = {}

def main():
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        files = ['first_name.txt','last_name.txt','age.txt','country.txt','hobbies.txt','salary.txt',
'job_title.txt','email.txt','projects.txt','education.txt']
        for file_name in ['first_name.txt','last_name.txt','age.txt','country.txt','hobbies.txt','salary.txt',
'job_title.txt','email.txt','projects.txt','education.txt']:
            futures = executor.map(get_str, files)
            futures = list(futures)
        if json_object:
            with lock:
                json_all.append(json_object)
        json_string = json.dumps(json_all, ensure_ascii=False, indent=4)
        print(json_string)

main()