import os

area = {}

with open(os.path.join(os.path.dirname(__file__), 'day18.in')) as file:
    for i, line in enumerate(file):
        for j, c in enumerate(line.strip()):
            area[(i,j)] = c


def change(pt, old_area, new_area):
    if old_area[pt] == '.':
        new_area[pt] = change_open(pt, old_area)
    if old_area[pt] == '|':
        new_area[pt] = change_tree(pt, old_area)
    if old_area[pt] == '#':
        new_area[pt] = change_lumberyard(pt, old_area)

def get_adjacents(pt):
    return [
        (pt[0], pt[1]-1),
        (pt[0]+1, pt[1]-1),
        (pt[0]+1, pt[1]),
        (pt[0]+1, pt[1]+1),
        (pt[0], pt[1]+1),
        (pt[0]-1, pt[1]+1),
        (pt[0]-1, pt[1]),
        (pt[0]-1, pt[1]-1),
    ]

def change_open(pt, old_area):
    nbs = get_adjacents(pt)
    if len([nb for nb in nbs if nb in old_area.keys() and old_area[nb] == '|']) >= 3:
        return '|'
    else:
        return '.'

def change_tree(pt, old_area):
    nbs = get_adjacents(pt)
    if len([nb for nb in nbs if nb in old_area.keys() and old_area[nb] == '#']) >= 3:
        return '#'
    else:
        return '|'

def change_lumberyard(pt, old_area):
    nbs = get_adjacents(pt)
    adjacent_trees = len([nb for nb in nbs if nb in old_area.keys() and old_area[nb] == '|'])
    adjacent_lumberyard = len([nb for nb in nbs if nb in old_area.keys() and old_area[nb] == '#'])
    if adjacent_trees >=1 and adjacent_lumberyard >=1:
        return '#'
    else:
        return '.'

def start(area):
    old_area = area
    
    for _ in range(10):
        new_area = {}
        for pt, _ in old_area.items():
            change(pt, old_area, new_area)
        old_area = new_area

    trees = len([c for _,c in old_area.items() if c == '|'])
    lumberyards = len([c for _,c in old_area.items() if c == '#'])

    print('part1', trees*lumberyards)

    old_area = area
    ans = set()
    for _ in range(1000):
        new_area = {}
        for pt, _ in old_area.items():
            change(pt, old_area, new_area)
        old_area = new_area
        trees = len([c for _,c in old_area.items() if c == '|'])
        lumberyards = len([c for _,c in old_area.items() if c == '#'])

        ans.add(trees*lumberyards)
    off = (1000000000 - 1000) % 28
    print('part2', off)

start(area)