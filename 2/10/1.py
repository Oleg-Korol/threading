import re
from functools import reduce
from data import messages
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

special_characters_pattern = re.compile(r'[!"#$%&\'()*+,-./:;<=>?@[\\\]^_`{|}~ ]')

def count_letters(sentence:str):
    return Counter(special_characters_pattern.sub('', sentence.lower()))

with ThreadPoolExecutor(max_workers=16) as executor:
    results = executor.map(count_letters, messages)
    count = dict(reduce(lambda x,y:x+y,results))
    print(dict(sorted(count.items())))

