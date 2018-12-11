import os


def react(polymer):
    t = []
    for c in polymer:
        if t and c.swapcase() == t[-1]:
            t.pop()
        else:
            t.append(c)
    return t


with open(os.path.join(os.path.dirname(__file__), 'day5.in')) as file:
    for line in file:
        polymer = line.strip()
        print('part1', len(react(polymer)))
        types = set([c.lower() for c in polymer])
        print('part2', min(
            [len(react(polymer.replace(t, '').replace(t.upper(), ''))) for t in types]))
