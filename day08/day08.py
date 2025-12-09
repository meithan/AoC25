# Day 08: 

from functools import reduce
from math import sqrt
import sys

CLR = "\33[2K\r"

# ==============================================================================

# Get filename of input as CLI arg. If not given, default to "input"
if len(sys.argv) == 1:
  input_fname = "input"
else:
  input_fname = sys.argv[1]

# Read and parse input
boxes = []
with open(input_fname) as f:
  for line in f:
    boxes.append([int(x) for x in line.strip().split(',')])

def calc_dist(coords1, coords2):
  x1, y1, z1 = coords1
  x2, y2, z2 = coords2
  return sqrt((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)

distances = []
N = len(boxes)
for i in range(N):
  for j in range(i+1,N):
    distances.append((i, j, calc_dist(boxes[i], boxes[j])))

distances.sort(key=lambda x: x[2])

# ------------------------------------------------------------------------------
# Part 1

# Put every box into its own circuit
assignments = {i: i for i in range(len(boxes))}

# Now do the connections
num_connections = 1000
count = 0
for i, j, _ in distances[:num_connections]:
  c1 = assignments[i]
  c2 = assignments[j]
  for idx in assignments:
    if assignments[idx] == c2:
      assignments[idx] = c1

# Create the circuits from the assignments
circuits = {}
for idx in assignments:
  c = assignments[idx]
  if c not in circuits:
    circuits[c] = []
  circuits[c].append(idx)

# Sort the circuits by size
circuits_list = [(c, circuits[c]) for c in circuits]
circuits_list.sort(key=lambda x: len(x[1]), reverse=True)
sizes = [len(x[1]) for x in circuits_list[:3]]
ans1 = reduce(lambda x, y: x*y, sizes, 1)

print("Part 1:", ans1)

# ------------------------------------------------------------------------------
# Part 2

# Put every box into its own circuit
assignments = {i: i for i in range(len(boxes))}

# Keep connecting until every box is in the same circuit
count = 0
for i, j, _ in distances:
  c1 = assignments[i]
  c2 = assignments[j]
  for idx in assignments:
    if assignments[idx] == c2:
      assignments[idx] = c1
  if list(assignments.values()).count(assignments[0]) == len(boxes):
    ans2 = boxes[i][0] * boxes[j][0]
    break

print("Part 2:", ans2)