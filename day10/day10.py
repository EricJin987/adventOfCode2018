import os,re

with open(os.path.join(os.path.dirname(__file__), 'day10.in')) as file:
  input = [list(map(int, re.findall(r'-?\d+', line))) for line in file]
  
  bounds = {}

  for sec in range(30000):
    minx = min(x+sec*vx for x,y,vx,vy in input)
    maxx = max(x+sec*vx for x,y,vx,vy in input)
    miny = min(y+sec*vy for x,y,vx,vy in input)
    maxy = max(y+sec*vy for x,y,vx,vy in input)
    
    bounds[sec]=[minx,maxx,miny,maxy]
  
  min_sec = min(bounds.keys(), key=lambda x: bounds[x][1]-bounds[x][0]+bounds[x][3]-bounds[x][2])
  
  max_x = bounds[min_sec][1]+1
  max_y = bounds[min_sec][3]+1

  word = [[' ']*max_x for _ in range(max_y)]
  for x,y,vx,vy in input:
    word[y+min_sec*vy][x+min_sec*vx] = '*'
  
  for w in word:
    print(''.join(w))

  print(min_sec)