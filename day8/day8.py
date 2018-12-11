import os


with open(os.path.join(os.path.dirname(__file__), 'day8.in')) as file:
  numbers = list(map(int, file.read().strip().split(' ')))
  
part1 = []

def child_length(s):
  num_of_children = s[0]
  num_of_metadata = s[1]
  if num_of_children == 0:
    for i in s[2:2+num_of_metadata]:
      part1.append(i)
    return 2+num_of_metadata
  else:
    children_len = 0
    for i in range(num_of_children):
      children_len += child_length(s[2+children_len:])
    for i in s[2+children_len:2+children_len+num_of_metadata]:
      part1.append(i)
    return 2+children_len+num_of_metadata



def child_value(s):
  num_of_children = s[0]
  num_of_metadata = s[1]
  if num_of_children == 0:
    return sum(s[2:2+num_of_metadata])
  else:
    children_len = 0
    children_values = []
    value = 0
    for i in range(num_of_children):
      children_values.append(child_value(s[2+children_len:]))
      children_len += child_length(s[2+children_len:])
    for i in s[2+children_len:2+children_len+num_of_metadata]:
      if i-1 in range(num_of_children):
        value += children_values[i-1]
    return value

child_length(numbers)
print(len(part1))

part2 = child_value(numbers)
print(part2)
