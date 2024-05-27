import re
from data import messages
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

special_characters_pattern = re.compile(r'[!"#$%&\'()*+,-./:;<=>?@[\\\]^_`{|}~ ]')
letter_values = {'а': 1, 'б': 2, 'в': 3, 'г': 4, 'д': 5,
                 'е': 6, 'ё': 7, 'ж': 8, 'з': 9, 'и': 10,
                 'й': 11, 'к': 12, 'л': 13, 'м': 14, 'н': 15,
                 'о': 16, 'п': 17, 'р': 18, 'с': 19, 'т': 20,
                 'у': 21, 'ф': 22, 'х': 23, 'ц': 24, 'ч': 25,
                 'ш': 26, 'щ': 27, 'ъ': 28, 'ы': 29, 'ь': 30,
                 'э': 31, 'ю': 32, 'я': 33}
best_total = (0,'')

def sum_letters(sentence):
    global best_total
    total = 0
    for letter, count in (Counter(special_characters_pattern.sub('', sentence.lower()))).items():
        total+= letter_values.get(letter) * count
    if best_total[0]<total:
        best_total = (total,sentence)


with ThreadPoolExecutor(max_workers=16) as executor:
    results = executor.map(sum_letters, messages)

print(best_total[1])