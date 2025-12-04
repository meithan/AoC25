# Day 03: Printing Department

import sys
CLR = "\33[2K\r"

# ==============================================================================

# Get filename of input as CLI arg. If not given, default to "input"
if len(sys.argv) == 1:
  input_fname = "input"
else:
  input_fname = sys.argv[1]

# Read and parse input
grid = []
with open(input_fname) as f:
  for line in f:
    grid.append([_ for _ in line.strip()])

NX = len(grid)
NY = len(grid[0])

neihgs_deltas = [(1,0), (-1,0), (-1,-1), (0,-1), (1,-1), (-1,1), (0,1), (1,1)]

def is_accesible(i, j):
  adj_rolls = 0
  for di, dj in neihgs_deltas:
    ni = i + di; nj = j + dj
    if 0 <= ni < NX and 0 <= nj < NY and grid[ni][nj] == "@":
      adj_rolls += 1
  return adj_rolls < 4

# ------------------------------------------------------------------------------
# Part 1

accesible_count = 0
for i in range(NX):
  for j in range(NY):
    if grid[i][j] == "@" and is_accesible(i, j):
      accesible_count += 1

print("Part 1:", accesible_count)

# ------------------------------------------------------------------------------
# Part 2

ans2 = None

removed_count = 0
while True:
  accesible_rolls = []
  for i in range(NX):
    for j in range(NY):
      if grid[i][j] == "@" and is_accesible(i, j):
        accesible_rolls.append((i, j))
  if len(accesible_rolls) == 0:
    break
  else:
    for ii, jj in accesible_rolls:
      grid[ii][jj] = "."
      removed_count += 1

print("Part 2:", removed_count)
