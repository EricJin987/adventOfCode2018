import os, re
from collections import defaultdict
with open(os.path.join(os.path.dirname(__file__), 'day4-1.in')) as file:
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
      id_dict[id].append((wakes_up_time,falls_asleep_time))
  
  t = []
  for id, intervals in id_dict.items():
    s = defaultdict(int)
    for wakes_up_time,falls_asleep_time in intervals:
      for minute in range(60):
        if falls_asleep_time<=minute<wakes_up_time:
          s[minute] += 1
    (m, f) = max(s.items(), key=lambda i: i[1])
    t.append((id,m,f))
  (i, mm, ff) = max(t, key=lambda i: i[2])
  print(i*mm)