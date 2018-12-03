import os
change_list = []
with open(os.path.join(os.path.dirname(__file__), 'day1-2.in')) as file:
  for line in file:
    change_list.append(int(line))

result = 0
f_list = []
f_list.append(result)
outter_loop = True
while True:
  if not outter_loop:
    break
  for change in change_list:
    result += change
    if result in f_list:
      print(result)
      outter_loop = False
      break
    f_list.append(result)
    