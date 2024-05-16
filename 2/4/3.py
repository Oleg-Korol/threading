from concurrent.futures import ThreadPoolExecutor
students = {
    1: {'name': 'Alice', 'age': 20, 'grades': [4, 5, 5, 4, 2, 3, 5, 2]},
    2: {'name': 'Bob', 'age': 21, 'grades': [3, 4, 3, 4, 4, 5, 3, 4, 3, 2, 4]},
    3: {'name': 'Charlie', 'age': 19, 'grades': [5, 5, 5, 5, 5, 5, 4, 5, 4, 5, 4]},
    20: {'name': 'Hannah Thompson', 'age': 20, 'grades': [2, 4, 3, 5, 3, 3, 2, 4, 4, 3, 2, 2, 2, 2, 5, 3, 4, 5]}
    }
new_dict = {}

def average_score( student:dict)->dict:
    name = student.get('name')
    average = sum(student.get('grades'))/len(student.get('grades'))
    data = {name:round(average,2)}
    return data

def main():
    with ThreadPoolExecutor(max_workers=len(students)) as execute:
        results = execute.map(lambda x: average_score(students.get(x)),students)
        [new_dict.update(student) for student in results]
        print({new_dict})

main()