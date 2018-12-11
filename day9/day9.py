import os
from collections import deque, defaultdict
with open(os.path.join(os.path.dirname(__file__), 'day9.in')) as file:
  line = file.read().strip().split(' ')

def game(players, last_marble):
  circle = deque([0])
  score = defaultdict(int)
  for i in range(1,last_marble+1):
    if i%23 == 0:
      circle.rotate(-7)
      score[i%players] += i+circle.pop()

    else:
      circle.rotate(2)
      circle.append(i)
  return max(score.values())

print('part1', game(int(line[0]), int(line[6])))
print('part2', game(int(line[0]), int(line[6])*100))
