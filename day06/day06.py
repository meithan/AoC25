# Day 06: Trash Compactor

import re
import sys
from functools import reduce
from operator import add, mul

CLR = "\33[2K\r"

# ==============================================================================

# Get filename of input as CLI arg. If not given, default to "input"
if len(sys.argv) == 1:
  input_fname = "input"
else:
  input_fname = sys.argv[1]

# Read and parse input
with open(input_fname) as f:
  lines = f.readlines()
problems = list(zip(*[[int(x) for x in line.strip().split()] for line in lines[:-1]]))
operators = lines[-1].strip().split()

# ------------------------------------------------------------------------------
# Part 1

grand_total = 0
for numbers, op in zip(problems, operators):
  if op == "+":
    tot = reduce(add, numbers, 0)
  elif op == '*':
    tot = reduce(mul, numbers, 1)
  grand_total += tot

print("Part 1:", grand_total)

# ------------------------------------------------------------------------------
# Part 2

num_rows = len(lines)-1

# Determine number of columns that each problem spans
parts = re.findall("[+*] +", lines[-1])
prob_cols = []
for i, part in enumerate(parts):
  prob_cols.append(len(part)-1 if i < len(parts)-1 else len(part))

problems2 = []
idx = 0
for ncols in prob_cols:
  nums = []
  for j in range(ncols):
    num = int("".join([lines[i][idx+j] for i in range(num_rows)]))
    nums.append(num)
  problems2.append(nums)
  idx += ncols + 1

grand_total2 = 0
for numbers, op in zip(problems2, operators):
  if op == "+":
    tot = reduce(add, numbers, 0)
  elif op == '*':
    tot = reduce(mul, numbers, 1)
  grand_total2 += tot

print("Part 2:", grand_total2)
