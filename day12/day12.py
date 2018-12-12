import os,re
from collections import deque

with open(os.path.join(os.path.dirname(__file__), 'day12.in')) as file:
  input = file.readlines()
  inital_state = input[0].split(':')[1].strip()
  cur_gen = inital_state
  init_len = len(inital_state)
  note = {}
  for line in input[2:]:
    (a,b) = line.split('=>')
    note[a.strip()] = b.strip()

 
def sum_gen(gen):
  delta = (len(gen)-init_len)//2
  return sum([i-delta for i,c in enumerate(gen) if c == '#'])

for i in range(20):
  cur_gen = '....' + cur_gen + '....'
  next_gen = ''
  for j in range(2,len(cur_gen)-2):
    next_gen += note[cur_gen[j-2:j+3]]
  cur_gen = next_gen
  if i==19:
    print(sum_gen(cur_gen))

cur_gen = inital_state

for i in range(1000):
  cur_gen = '....' + cur_gen + '....'
  cur_sum = sum_gen(cur_gen)
  next_gen = ''
  for j in range(2,len(cur_gen)-2):
    next_gen += note[cur_gen[j-2:j+3]]
  next_sum = sum_gen(next_gen)
  print(next_sum-cur_sum,i)
  cur_gen = next_gen

print((50000000000-i)*38+cur_sum)


      
