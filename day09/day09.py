# Day 09: Movie Theater

import sys

CLR = "\33[2K\r"

# ==============================================================================

# Get filename of input as CLI arg. If not given, default to "input"
if len(sys.argv) == 1:
  input_fname = "input"
else:
  input_fname = sys.argv[1]

# Read and parse input
tiles = []
with open(input_fname) as f:
  for line in f:
    tokens = line.strip().split(',')
    tiles.append((int(tokens[0]), int(tokens[1])))
num_tiles = len(tiles)

# ------------------------------------------------------------------------------
# Part 1

# Go over all pairs of red tiles, compute the area of the rectangle,
# determine maximum area
max_area = None
max_tiles = None
for i in range(num_tiles):
  for j in range(i+1, num_tiles):
    dx = abs(tiles[i][0] - tiles[j][0]) + 1
    dy = abs(tiles[i][1] - tiles[j][1]) + 1
    area = dx * dy
    if max_area is None or area > max_area:
      max_area = area
      max_tiles = (tiles[i], tiles[j])

print("Part 1:", max_area)

# ------------------------------------------------------------------------------
# Part 2

# For test input: show tiles
# for y in range(9):
#   row = ""
#   for x in range(14):
#     if (x,y) in tiles:
#       row += "#"
#     elif is_inside(x,y):
#       row += "X"
#     else:
#       row += "."
#   print(row)

# We go over all pairs of red tiles, which are the opposite corners of a
# rectangle, and for each rectangle we check whether all red tiles are
# outside or on the edge of the rectangle; if any red tile is strictly inside
# we reject that rectangle.
# This only works by adding the condition that the rectangle is either on the
# lower or upper "half" of the "elipsoid" defined by the red tiles
max_area2 = None
max_tiles2 = None
for i in range(num_tiles):
  for j in range(i+1, num_tiles):
    
    x1, y1 = tiles[i]
    x2, y2 = tiles[i][0], tiles[j][1]
    x3, y3 = tiles[j]
    x4, y4 = tiles[j][0], tiles[i][1]
    
    # Specific for my input: check that all corners are on the same
    # vertical "half" of the ellipsoid
    lower_y = 48484
    upper_y = 50269
    if not (y1 <= lower_y and y3 <= lower_y) and not (y1 >= upper_y and y3 >= upper_y):
      continue
    
    # Check that no red tile is (strictly) inside the rectangle
    passed = True
    for xt, yt in tiles:
      if (min(x1,x3) < xt < max(x1,x3) and min(y1,y3) < yt < max(y1,y3)):
        passed = False
        break
    if not passed:
      continue
    
    # All conditions passed: compute area and record largest
    dx =  abs(tiles[i][0] - tiles[j][0]) + 1
    dy = abs(tiles[i][1] - tiles[j][1]) + 1
    area = dx * dy
    if max_area2 is None or area > max_area2:
      max_area2 = area
      max_tiles2 = (tiles[i], tiles[j])

print("Part 2:", max_area2)

# import matplotlib.pyplot as plt
# plt.plot(xs+[xs[0]], ys+[ys[0]], color="red")
# max_tile1, max_tile2 = max_tiles2
# x1, y1 = max_tile1
# x2, y2 = max_tile1[0], max_tile2[1]
# x3, y3 = max_tile2
# x4, y4 = max_tile2[0], max_tile1[1]
# plt.plot([x1,x2,x3,x4,x1], [y1,y2,y3,y4,y1], color="blue")
# plt.gca().invert_yaxis()
# plt.show()