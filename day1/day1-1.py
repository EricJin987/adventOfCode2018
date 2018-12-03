import os
with open(os.path.join(os.path.dirname(__file__), 'day1-1.in')) as file:
  result = 0
  for line in file:
    result += int(line)
  print(result)