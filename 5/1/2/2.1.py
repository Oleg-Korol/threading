import time
import json
from concurrent.futures import ThreadPoolExecutor, wait, ALL_COMPLETED
from threading import Lock

lock = Lock()

json_object = {}
json_all = []


def get_str(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as file:
        key = file_name.rstrip('.txt')
        lines=[file_name,]
        lines1 =[ item.rstrip('\n') for item in file.readlines()]
        lines.extend(lines1)
        return lines



def create_list_json(results):
    global json_object
    print(results)
    r = zip(*results)
    r = list(r)
    print(r)



    for i in len(results-1):
        for key in r[0]:
            print(i)
            json_object.update({key:results[i+1][r[0].index(key)]})
            json_all.append(json_object)
            json_object ={}
    print(json_all)



def main():
    files = ['first_name.txt', 'last_name.txt', 'age.txt', 'country.txt', 'hobbies.txt', 'salary.txt',
             'job_title.txt', 'email.txt', 'projects.txt', 'education.txt']
    files = ['q','w']
    results = []
    for x in files:
        y = get_str(x)
        results.append(y)

    # with ThreadPoolExecutor(max_workers=10) as executor:
    #     futures = [executor.submit(get_str, file_name) for file_name in files]
    #     wait(futures, return_when=ALL_COMPLETED)
    #     results = [future.result() for future in futures]
    #
    create_list_json(results)


    if json_object:
        with lock:
            json_all.append(json_object)

    json_string = json.dumps(json_all, ensure_ascii=False, indent=4)



main()
