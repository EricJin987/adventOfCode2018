import os
from collections import defaultdict
with open(os.path.join(os.path.dirname(__file__), 'day6.in')) as file:
  coords = []
  for line in file:
    coords.append(list(map(int,line.strip().split(','))))
  
  min_x = min(coord[0] for coord in coords)
  max_x = max(coord[0] for coord in coords)
  min_y = min(coord[1] for coord in coords)
  max_y = max(coord[1] for coord in coords)

  
  coord_counter = defaultdict(int)
  regions = 0
  coords_infinite = []
  for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
      distances = [((abs(x-coord[0])+abs(y-coord[1])), (coord[0],coord[1])) for coord in coords]
      if sum([d for d, c in distances]) <= 10000:
        regions += 1
      t = sorted(distances)
      if len(t)==1 or t[0][0] < t[1][0]:
        coord_counter[t[0][1]] += 1
        if x == min_x or x == max_x or y == min_y or y == max_y:
          coords_infinite.append(t[0][1])
  
  print('part1',max([v for k,v in coord_counter.items() if k not in coords_infinite]))
  print('part2',regions)
