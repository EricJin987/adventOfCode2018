import os,re
from collections import defaultdict

with open(os.path.join(os.path.dirname(__file__), 'day7.in')) as file:
  WORKERS = 5
  pres = defaultdict(list)
  nodes = set()

  steptimes = {}
  for line in file:
      x = line[5]
      y = line.rstrip()[-12]
      pres[y].append(x)
      nodes.add(x)
      nodes.add(y)

  for s in sorted(nodes):
      steptimes[s] = ord(s) - ord('A') + 61
      if s not in pres:
          pres[s] = []

  part1 = []
  part2 = 0

  while (len(pres) > 0):
      cando = []
      for s in pres.items():
          if all(d in part1 for d in s[1]):
              cando.append(s[0])

      
      cando = sorted(cando)
      for i in range(min(WORKERS, len(cando))):
          steptimes[cando[i]] -= 1

      for cd in cando:
          if steptimes[cd] < 1:
              part1 += cd
              del pres[cd]

      part2 += 1



  print("".join(part1)) 

  print(part2)
