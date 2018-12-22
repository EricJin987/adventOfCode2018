import os
from collections import defaultdict

with open(os.path.join(os.path.dirname(__file__), 'day16.in')) as file:
    ins = []
    outs = []
    instructions = []
    for index, line in enumerate(file):
        if 'Before' in line:
            ins.append(tuple(map(lambda x: int(x.strip()),line[9:-2].split(','))))
        elif 'After' in line:
            outs.append(tuple(map(lambda x: int(x.strip()),line[9:-2].split(','))))
        elif len(line)>1:
            instructions.append(tuple(map(int,line.strip().split(' '))))

def addr(before, after, instruction):
    a,b,c = instruction[1:]
    return before[a]+before[b]

def addi(before, after, instruction):
    a,b,c = instruction[1:]
    return before[a] + b

def mulr(before, after, instruction):
    a,b,c = instruction[1:]
    return before[a]*before[b]

def muli(before, after, instruction):
    a,b,c = instruction[1:]
    return before[a]*b

def banr(before, after, instruction):
    a,b,c = instruction[1:]
    return before[a]&before[b]

def bani(before, after, instruction):
    a,b,c = instruction[1:]
    return before[a]&b

def borr(before, after, instruction):
    a,b,c = instruction[1:]
    return before[a]|before[b]

def bori(before, after, instruction):
    a,b,c = instruction[1:]
    return before[a]|b

def setr(before, after, instruction):
    a,b,c = instruction[1:]
    return before[a]

def seti(before, after, instruction):
    a,b,c = instruction[1:]
    return a

def gtir(before, after, instruction):
    a,b,c = instruction[1:]
    return 1 if a > before[b] else 0

def gtri(before, after, instruction):
    a,b,c = instruction[1:]
    return 1 if before[a] > b else 0

def gtrr(before, after, instruction):
    a,b,c = instruction[1:]
    return 1 if before[a] > before[b] else 0

def eqir(before, after, instruction):
    a,b,c = instruction[1:]
    return 1 if a == before[b] else 0

def eqri(before, after, instruction):
    a,b,c = instruction[1:]
    return 1 if before[a] == b else 0

def eqrr(before, after, instruction):
    a,b,c = instruction[1:]
    return 1 if before[a] == before[b] else 0

number = len(ins)
ops = defaultdict(set)


def part1():
    part1_result = 0
    for i in range(number):
        before = ins[i]
        after = outs[i]
        instruction = instructions[i]
        opcodes = 0

        if after[instruction[3]] == addr(before, after, instruction):
            opcodes += 1
            ops[instruction[0]].add(addr)
        if after[instruction[3]] == addi(before, after, instruction):
            opcodes += 1
            ops[instruction[0]].add(addi)
        if after[instruction[3]] == mulr(before, after, instruction): 
            opcodes += 1 
            ops[instruction[0]].add(mulr)
        if after[instruction[3]] == muli(before, after, instruction):
            opcodes += 1 
            ops[instruction[0]].add(muli)
        if after[instruction[3]] == banr(before, after, instruction):
            opcodes += 1
            ops[instruction[0]].add(banr)
        if after[instruction[3]] == bani(before, after, instruction):
            opcodes += 1
            ops[instruction[0]].add(bani)
        if after[instruction[3]] == borr(before, after, instruction):
            opcodes += 1
            ops[instruction[0]].add(borr)
        if after[instruction[3]] == bori(before, after, instruction):
            opcodes += 1
            ops[instruction[0]].add(bori)
        if after[instruction[3]] == setr(before, after, instruction):
            opcodes += 1
            ops[instruction[0]].add(setr)
        if after[instruction[3]] == seti(before, after, instruction):
            opcodes += 1
            ops[instruction[0]].add(seti)
        if after[instruction[3]] == gtir(before, after, instruction):
            opcodes += 1
            ops[instruction[0]].add(gtir)
        if after[instruction[3]] == gtri(before, after, instruction):
            opcodes += 1
            ops[instruction[0]].add(gtri)
        if after[instruction[3]] == gtrr(before, after, instruction):
            opcodes += 1
            ops[instruction[0]].add(gtrr)
        if after[instruction[3]] == eqir(before, after, instruction):
            opcodes += 1
            ops[instruction[0]].add(eqir)
        if after[instruction[3]] == eqri(before, after, instruction):
            opcodes += 1
            ops[instruction[0]].add(eqri)
        if after[instruction[3]] == eqrr(before, after, instruction):
            opcodes += 1
            ops[instruction[0]].add(eqrr)
        part1_result += 1 if opcodes >=3 else 0
    print(part1_result)
part1()
while True:
    confirmed = [(num, ins) for num, ins in ops.items() if len(ins) == 1]
    if len(confirmed) == 16:
        break
    for c in confirmed:
        for num, ins in ops.items():
            if num != c[0] and list(c[1])[0] in ins:
                ops[num].remove(list(c[1])[0])


with open(os.path.join(os.path.dirname(__file__), 'day16-2.in')) as file:
    new_ins = [list(map(int, line.strip().split(' '))) for line in file]

registers = [0,0,0,0]
for ins in new_ins:
    op = ins[0]
    c = ins[3]
    result = list(ops[op])[0](registers, [], ins)
    registers[c] = result

print('part2', registers[0])
    