import os, collections
with open(os.path.join(os.path.dirname(__file__), 'day2-1.in')) as file:
  twos, threes = 0, 0
  for line in file:
    has_two = False
    has_three = False
    counter = collections.Counter(line)
    for c in line:
      if has_two and has_three:
        break
      if counter[c] == 2:
        if has_two != True:
          has_two = True
          twos += 1
        continue
      if counter[c] == 3:
        if has_three != True:
          has_three = True
          threes +=1

        continue
  print(twos*threes)
      

