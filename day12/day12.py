# Day 12: Christmas Tree Farm

import re
import sys

CLR = "\33[2K\r"

# ==============================================================================

# Get filename of input as CLI arg. If not given, default to "input"
if len(sys.argv) == 1:
  input_fname = "input"
else:
  input_fname = sys.argv[1]

# Read and parse input
presents = []
regions = []
with open(input_fname) as f:
  while True:
    line = f.readline()
    if line == "": break
    if re.match("[0-9]+:", line):
      present = []
      while True:
        line = f.readline()
        if line == "\n":
          break
        present.append(line.strip())
      presents.append(present)
    elif "x" in line:
      size, nums = line.strip().split(":")
      size = tuple(int(x) for x in size.split("x"))
      nums = tuple(int(x) for x in nums.split())
      regions.append((size, nums))

# ------------------------------------------------------------------------------
# Part 1

# Areas of each present
areas = [sum(row.count("#") for row in present) for present in presents]

# Count how many test cases are impossible because the total
# area of the presents is larger than the region's
impossible_count = 0
for size, numbers in regions:
  region_area = size[0] * size[1]
  presents_area = sum([numbers[i]*areas[i] for i in range(len(numbers))])
  if presents_area > region_area:
    impossible_count += 1

# Maybe?
print("Part 1:", len(regions)-impossible_count)

# ------------------------------------------------------------------------------
# Part 2

print("Part 2:", "No part 2 in last day!")
