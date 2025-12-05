# Day 05: Cafeteria

import sys
CLR = "\33[2K\r"

# ==============================================================================

# Get filename of input as CLI arg. If not given, default to "input"
if len(sys.argv) == 1:
  input_fname = "input"
else:
  input_fname = sys.argv[1]

# Read and parse input
fresh_ranges = []
ingredients = []
with open(input_fname) as f:
  while True:
    line = f.readline().strip()
    if line == "": break
    a, b = line.split("-")
    fresh_ranges.append((int(a), int(b)))
  while True:
    line = f.readline().strip()
    if line == "": break
    ingredients.append(int(line))

# ------------------------------------------------------------------------------
# Part 1

fresh_count = 0
for ing in ingredients:
  for a, b in fresh_ranges:
    if a <= ing <= b:
      fresh_count += 1
      break

print("Part 1:", fresh_count)

# ------------------------------------------------------------------------------
# Part 2

def combine_ranges(ranges):
  while True:
    changed = False
    N = len(ranges)
    for i in range(N):
      for j in range(i+1,N):
        a1, b1 = ranges[i]
        a2, b2 = ranges[j]
        if a2 <= b1 and b2 >= a1:
          an = min(a1, a2)
          bn = max(b1, b2)
          ranges.remove((a1,b1))
          ranges.remove((a2,b2))
          ranges.append((an,bn))
          changed = True
          break
      if changed:
        break
    if not changed:
      return ranges

fresh_ranges_combined = combine_ranges(fresh_ranges)

tot_fresh_count = 0
for a, b in fresh_ranges_combined:
  tot_fresh_count += (b - a + 1)

print("Part 2:", tot_fresh_count)
