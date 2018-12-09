import os, re
from collections import defaultdict
with open(os.path.join(os.path.dirname(__file__), 'day3-1.in')) as file:
  metric = defaultdict(list)
  overlaps = set()
  claims = []
  numbers = map(lambda line: map(int, re.findall(r'\d+',line)), file)
  for claim,x,y,a,b in numbers:
    claims.append(claim)
    for i in range(x, x+a):
      for j in range(y, y+b):
        metric[(i,j)].append(claim)
        if (len(metric[(i,j)]) > 1):
          for c in metric[(i,j)]:
            overlaps.add(c)  
  print([claim for claim in claims if claim not in overlaps])