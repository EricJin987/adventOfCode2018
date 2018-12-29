import os,math

def addr(before, instruction):
    a,b,_ = list(map(int, instruction[1:]))
    return before[a]+before[b]

def addi(before, instruction):
    a,b,_ = list(map(int, instruction[1:]))
    return before[a] + b

def mulr(before, instruction):
    a,b,_ = list(map(int, instruction[1:]))
    return before[a]*before[b]

def muli(before, instruction):
    a,b,_ = list(map(int, instruction[1:]))
    return before[a]*b

def banr(before, instruction):
    a,b,_ = list(map(int, instruction[1:]))
    return before[a]&before[b]

def bani(before, instruction):
    a,b,_ = list(map(int, instruction[1:]))
    return before[a]&b

def borr(before, instruction):
    a,b,_ = list(map(int, instruction[1:]))
    return before[a]|before[b]

def bori(before, instruction):
    a,b,_ = list(map(int, instruction[1:]))
    return before[a]|b

def setr(before, instruction):
    a,b,_ = list(map(int, instruction[1:]))
    return before[a]

def seti(before, instruction):
    a,b,_ = list(map(int, instruction[1:]))
    return a

def gtir(before, instruction):
    a,b,_ = list(map(int, instruction[1:]))
    return 1 if a > before[b] else 0

def gtri(before, instruction):
    a,b,_ = list(map(int, instruction[1:]))
    return 1 if before[a] > b else 0

def gtrr(before, instruction):
    a,b,_ = list(map(int, instruction[1:]))
    return 1 if before[a] > before[b] else 0

def eqir(before, instruction):
    a,b,_ = list(map(int, instruction[1:]))
    return 1 if a == before[b] else 0

def eqri(before, instruction):
    a,b,_ = list(map(int, instruction[1:]))
    return 1 if before[a] == b else 0

def eqrr(before, instruction):
    a,b,_ = list(map(int, instruction[1:]))
    return 1 if before[a] == before[b] else 0

ops = {
    'gtrr': gtrr,
    'borr': borr,
    'gtir': gtir,
    'eqri': eqri,
    'addr': addr,
    'seti': seti,
    'eqrr': eqrr,
    'gtri': gtri,
    'banr': banr,
    'addi': addi,
    'setr': setr,
    'mulr': mulr,
    'bori': bori,
    'muli': muli,
    'eqir': eqir,
    'bani': bani
}

with open(os.path.join(os.path.dirname(__file__), 'day19.in')) as file:
    bound = int(file.readline().strip()[-1])
    instructions = [line.strip().split(' ') for line in file]

def run(register, instructions):
    ip = 0
    register = register
    k = 0
    while True:
        if ip < 0 or ip >= len(instructions):
            break
        ins = instructions[ip]
        k+=1
        op = ins[0]
        c = int(ins[3])
        register[bound] = ip
        register[c] = ops[op](register, ins)
        ip = register[bound]
        ip += 1
        print(register)
    print(register[0])

print('part1')
run([0,0,0,0,0,0], instructions)


def sx(n):
    result = 0
    for i in range(1, int(math.sqrt(n))+1):
        if n%i == 0:
            result += i + n/i
    return result

print('part2', sx(10551377))

