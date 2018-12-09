import os
from itertools import combinations
with open(os.path.join(os.path.dirname(__file__), 'day2-1.in')) as file:
    ids = [x.strip() for x in file]
    for a,b in combinations(ids,2):
        diff = 0
        for index, value in enumerate(a):
            if b[index] != value:
                diff += 1
        if diff == 1:
            print(''.join([value for index, value in enumerate(a) if b[index]==value]))
