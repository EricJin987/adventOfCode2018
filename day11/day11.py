def power_level(x,y,serial_number):
  rack_id = x+10
  s = rack_id*y
  s1 = s + serial_number
  s2 = s1 * rack_id
  h = s2//100%10
  return h-5

print(power_level(122,79,57))
print(power_level(217,196,39))
print(power_level(101,153,71))

grid=[[power_level(x+1,y+1,7857) for y in range(300)] for x in range(300)]

partial_sum_grid = [[0 for y in range(300)] for x in range(300)]

for x in range(300):
  for y in range(300):
    partial_sum_grid[x][y] = grid[x][y] + partial_sum_grid[x-1][y] + partial_sum_grid[x][y-1] - partial_sum_grid[x-1][y-1]



max_power = (-100000,-1,-1)
for x in range(297):
  for y in range(297):
    g = partial_sum_grid[x+3][y+3]-partial_sum_grid[x][y+3]-partial_sum_grid[x+3][y] + partial_sum_grid[x][y]
    max_power = max(max_power, (g,x+2,y+2))
    

print('part1',max_power)

max_power = (-100000,-1,-1,-1)
for size in range(2,301):
  for x in range(300-size):
    for y in range(300-size):
      g = partial_sum_grid[x+size][y+size]-partial_sum_grid[x][y+size]-partial_sum_grid[x+size][y] + partial_sum_grid[x][y]
      max_power = max(max_power, (g,x+2,y+2,size))
    

print('part2',max_power)