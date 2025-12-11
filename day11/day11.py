# Day 11: Reactor

import sys

CLR = "\33[2K\r"

# ==============================================================================

# Get filename of input as CLI arg. If not given, default to "input"
if len(sys.argv) == 1:
  input_fname = "input"
else:
  input_fname = sys.argv[1]

# Read and parse input
nodes = {}
with open(input_fname) as f:
  for line in f:
    tokens = line.strip().split(":")
    name = tokens[0]
    children = tokens[1].split()
    nodes[name] = children
nodes["out"] = []

# ------------------------------------------------------------------------------
# Part 1

def count_paths(start, end):
  if (start,end) in memo:
    return memo[(start,end)]
  if start == end:
    memo[(start,end)] = 1
    return 1
  count = 0
  for child in nodes[start]:
    n = count_paths(child, end)
    memo[(child,end)] = n
    count += n
  return count

memo = {}
count = count_paths("you", "out")

print("Part 1:", count)

# ------------------------------------------------------------------------------
# Part 2

memo = {}

count1 = 1
seq = ["svr", "fft", "dac", "out"]
for i in range(len(seq)-1):
  c = count_paths(seq[i], seq[i+1])
  # print(seq[i], seq[i+1], c)
  count1 *= c

count2 = 1
seq = ["svr", "dac", "fft", "out"]
for i in range(len(seq)-1):
  c = count_paths(seq[i], seq[i+1])
  if c == 0:
    # print(f"No path from {seq[i]} to {seq[i+1]}")
    count2 = 0
    break
  # print(seq[i], seq[i+1], c)
  count2 *= c

ans2 = count1 + count2

print("Part 2:", ans2)
