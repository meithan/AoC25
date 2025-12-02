# Day 02: Gift Shop

import sys
CLR = "\33[2K\r"

# ==============================================================================

# Get filename of input as CLI arg. If not given, default to "input.txt"
if len(sys.argv) == 1:
  input_fname = "input.txt"
else:
  input_fname = sys.argv[1]

# Read and parse input
id_ranges = []
with open(input_fname) as f:
  line = f.readline().strip()
  for foo in line.split(','):
    start, end = foo.split("-")
    id_ranges.append((int(start), int(end)))

# ------------------------------------------------------------------------------
# Part 1

def is_invalid_part1(num):
  snum = str(num)
  l = len(snum)
  return l % 2 == 0 and snum[:l//2] == snum[l//2:]

# Brute force: just check every number in range
def find_invalid_ids(ranges, invalid_fun):
  invalid_ids = []
  for start, end in id_ranges:
    num = start
    for num in range(start, end+1):
      if invalid_fun(num):
        invalid_ids.append(num)
  return invalid_ids

invalid_ids1 = find_invalid_ids(id_ranges, is_invalid_part1)
ans1 = sum(invalid_ids1)

print("Part 1:", ans1)

# ------------------------------------------------------------------------------
# Part 2

def is_invalid_part2(num):
  snum = str(num)
  l = len(snum)
  for l1 in range(1, l//2+1):
    # print(l1)
    if l % l1 != 0: continue
    reps = l // l1
    # print(snum[:l1]*reps)
    if snum == snum[:l1] * reps:
      return True
  return False

invalid_ids2 = find_invalid_ids(id_ranges, is_invalid_part2)
ans2 = sum(invalid_ids2)

print("Part 2:", ans2)
