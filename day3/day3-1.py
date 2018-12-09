import os, re
from collections import defaultdict
with open(os.path.join(os.path.dirname(__file__), 'day3-1.in')) as file:
  metric = defaultdict(int)
  numbers = map(lambda line: map(int, re.findall(r'\d+',line)), file)
  for claim,x,y,a,b in numbers:
    for i in range(x, x+a):
      for j in range(y, y+b):
        metric[(i,j)] += 1
  
  print(len([overlap for overlap in metric if metric[overlap] > 1]))
