# Plot day 7 solution

import copy
import sys
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np

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

# Replace splitters with 0
for i in range(nrows):
  for j in range(ncols):
    if grid1[i][j] == "^": grid1[i][j] = 0

# ---------------

plt.figure(figsize=(9,8))

data = np.array(grid1, dtype=np.float32)
data[data == 0] = np.nan

cmap = plt.cm.rainbow
cmap.set_bad('black')

im = plt.imshow(data, norm=mcolors.LogNorm(), cmap=cmap)

ax = plt.gca()
divider = make_axes_locatable(ax)
cax = divider.append_axes("right", size="5%", pad=0.1)
plt.colorbar(im, cax=cax)

ax.set_xticks([])
ax.set_yticks([])

plt.tight_layout()

if "--save" in sys.argv:
  plt.savefig("plot.png")
else:
  plt.show()




