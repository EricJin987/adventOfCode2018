import os, re
from collections import defaultdict
with open(os.path.join(os.path.dirname(__file__), 'day4-1.in')) as file:
  time_dict = defaultdict(int)
  id_dict = defaultdict(list)
  for line in sorted(file):
    shift = re.match(r'\[1518-(\d+-\d+) \d+:(\d+)\].*#(\d+).*', line)
    wakes_up = re.match(r'\[1518-(\d+-\d+) \d+:(\d+)\] wakes up', line)
    falls_asleep = re.match(r'\[1518-(\d+-\d+) \d+:(\d+)\] falls asleep', line)
    if shift:
      date = shift.group(1)
      shift_time = shift.group(2)
      id = int(shift.group(3))
    elif falls_asleep:
      date = falls_asleep.group(1)
      falls_asleep_time = int(falls_asleep.group(2))
    elif wakes_up:
      date = wakes_up.group(1)
      wakes_up_time = int(wakes_up.group(2))
      time_dict[id] += wakes_up_time - falls_asleep_time
      id_dict[id].append((wakes_up_time,falls_asleep_time))
  
  (id, minutes) = max(time_dict.items(), key=lambda i:i[1])
  s = defaultdict(int)
  for wakes_up_time,falls_asleep_time in id_dict[id]:
    for minute in range(60):
      if falls_asleep_time<=minute<wakes_up_time:
        s[minute] += 1
  print(max(s.items(), key=lambda i: i[1])[0]*id)
