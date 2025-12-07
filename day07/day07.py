# Day 07: Laboratories

import copy
import sys
import time

CLR = "\33[2K\r"

# ==============================================================================

# Get filename of input as CLI arg. If not given, default to "input"
if len(sys.argv) == 1:
  input_fname = "input"
else:
  input_fname = sys.argv[1]

# Read and parse input
grid0 = []
with open(input_fname) as f:
  for line in f:
    grid0.append([c for c in line.strip()])

nrows = len(grid0)
ncols = len(grid0[0])

def print_grid(grid1):
  for line in grid1:
    s = ""
    for c in line:
      if c == 0: s += "."
      elif type(c) is int: s += str(c)
      else:
        s += c
    print(s)

# ------------------------------------------------------------------------------
# Part 1

grid1 = copy.deepcopy(grid0)
num_splits = 0

# Start beam
for j in range(ncols):
  if grid1[0][j] == "S":
    grid1[0][j] = "|"
    break

# Propagate from each row to the next (except the last)
for i in range(nrows-1):
  for j in range(ncols):
    if grid1[i][j] == "|":
      if grid1[i+1][j] == ".":
        grid1[i+1][j] = "|"
      elif grid1[i+1][j] == "^":
        grid1[i+1][j+1] = "|"
        grid1[i+1][j-1] = "|"
        num_splits += 1

print("Part 1:", num_splits)

# ------------------------------------------------------------------------------
# Part 2

grid1 = copy.deepcopy(grid0)

# Convert grid to numeric values (# timelines passing through each cell)
for i in range(nrows):
  for j in range(ncols):
    if grid1[i][j] == ".":
      grid1[i][j] = 0
    elif grid1[i][j] == "S":
      grid1[i][j] = 1

# Propagate from each row to the next (except the last)
# But count multiplicities this time
for i in range(nrows-1):
  for j in range(ncols):
    if type(grid1[i][j]) is int and grid1[i][j] > 0:
      if grid1[i+1][j] == "^":
        grid1[i+1][j+1] += grid1[i][j]
        grid1[i+1][j-1] += grid1[i][j]
      else:
        grid1[i+1][j] += grid1[i][j]
  # print_grid(grid1); input()

num_timelines = sum(grid1[-1])

print("Part 2:", num_timelines)
