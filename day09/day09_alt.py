# Day 09: Movie Theater

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

# Determines if the point lies inside the axis-aligned polygon 
# Works regardless of the concacivity of the polygon
# Returns True if the point is inside, False if it's outside; if the point
# lies exactly on one side, it's considered inside.
# point: an (x,y) tuple
# polygon: the vertices of the polygon (a list of tuples), in order)
def point_inside_aa_polygon(point, polygon):
  xp, yp = point
  # First check whether the point lines on an edge
  # This could be changed to return a different value if it's important
  # to distinguish points on the boundary
  num_sides = len(polygon)
  for i in range(num_sides):
    x1, y1 = polygon[i]
    x2, y2 = polygon[(i+1) % num_sides]
    if min(x1,x2) <= xp <= max(x1,x2) and min(y1, y2) <= yp <= max(y1, y2):
      return True
  # Apply the ray algorithm: consider a ray launched from the point towards
  # any (axis-aligned) direction, here we choose it towards +x, and check
  # whether it intersects each side of the polygon that is perpendicular to
  # the ray (parallel sides are ignored). If the total number of intersections
  # is odd, the point is inside is the polygon; if it's even, it's outside.
  # Care must be taken when the ray exactly intersects one endpoint of a side
  # (a vertex of the polygon) instead of crossing the side between its end-
  # points. A simple rule, if applied consistently, solves this issue: only
  # count a vertex hit as an intersection when the ray crosses the bottom-most
  # endpoint of the side (or top-most, or left/right-most if the ray was 
  # chosen vertically; the only thing that matters is consistency).
  intersections = 0
  for i in range(num_sides):
    x1, y1 = polygon[i]
    x2, y2 = polygon[(i+1) % num_sides]
    # Only consider vertical sides
    if x1 == x2:
      if x1 >= xp and min(y1, y2) <= yp < max(y1, y2):
        intersections += 1
  return intersections % 2 == 1

# For test input: show tiles
# rows = []
# for y in range(9):
#   row = ""
#   for x in range(14):
#     if (x,y) in tiles:
#       row += "o"
#     elif point_inside_aa_polygon((x,y), tiles):
#       row += "X"
#     else:
#       row += "."
#   rows.append(row)
# for row in rows:
#   print(row)

# import matplotlib.pyplot as plt
# def draw_tiles():
#   xs = [t[0] for t in tiles]
#   ys = [t[1] for t in tiles]
#   plt.plot(xs+[xs[0]], ys+[ys[0]], color="blue")
#   plt.gca().invert_yaxis()
# def draw_rect(verts, color):
#   xs = []; ys = []
#   for x,y in verts + [verts[0]]:
#     xs.append(x)
#     ys.append(y)
#   plt.plot(xs, ys, color=color)

# We go over all pairs of red tiles, which are the opposite corners of a
# rectangle, and for each rectangle (which by definition touches the polygon)
# we check whether its corners are insid the polygin and whether its sides
# intersect any side of the polygon. We compute and compare the area of
# rectangles that do not cross any side.
max_area2 = None
max_tiles2 = None
for i in range(num_tiles):
  for j in range(i+1, num_tiles):
    
    x1, y1 = tiles[i]
    x2, y2 = tiles[i][0], tiles[j][1]
    x3, y3 = tiles[j]
    x4, y4 = tiles[j][0], tiles[i][1]
    corners = [(x1,y1), (x2,y2), (x3,y3), (x4,y4)]

    good = True

    # Check that all corners are inside
    if not all(point_inside_aa_polygon(p, tiles) for p in corners):
      good = False

    # Check that no sides of the rectangle strictly intersect with the polygon
    for s in range(num_tiles):
      xs1, ys1 = tiles[s]
      xs2, ys2 = tiles[(s+1) % num_tiles]
      for k in range(4):
        xc1, yc1 = corners[k]
        xc2, yc2 = corners[(k+1) % 4]
        if xc1 == xc2 and ys1 == ys2:
          if (min(xs1,xs2) < xc1 < max(xs1,xs2) and min(yc1,yc2) < ys1 < max(yc1,yc2)) or (min(xc1,xc2) < xs1 < max(xc1,xc2) and min(ys1,ys2) < yc1 < max(ys1,ys2)):
            good = False
            break
      if not good:
        break

    # if good:
    #   plt.figure(figsize=(8,7))
    #   draw_tiles()
    #   draw_rect(corners, color="green" if good else "red")
    #   plt.gca().set_aspect("equal")
    #   plt.tight_layout()
    #   plt.show()

    # Conditions passed: compute area and record largest
    if good:
      dx = abs(tiles[i][0] - tiles[j][0]) + 1
      dy = abs(tiles[i][1] - tiles[j][1]) + 1
      area = dx * dy
      if max_area2 is None or area > max_area2:
        max_area2 = area
        max_tiles2 = (tiles[i], tiles[j])

print("Part 2:", max_area2)

