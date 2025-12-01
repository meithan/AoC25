# Day 01: 

import sys
CLR = "\33[2K\r"

# ==============================================================================

# Get filename of input as CLI arg. If not given, default to "input.txt"
if len(sys.argv) == 1:
  input_fname = "input.txt"
else:
  input_fname = sys.argv[1]

# Read and parse input
instructions = []
with open(input_fname) as f:
  for line in f:
    direc = line[0]
    amount = int(line[1:])
    instructions.append((direc, amount))

# ------------------------------------------------------------------------------
# Part 1

pos = 50
ans1 = 0
for direc, amount in instructions:
  rotation = -amount if direc == "L" else amount
  pos = (pos + rotation) % 100
  if pos == 0:
    ans1 += 1

print("Part 1:", ans1)

# ------------------------------------------------------------------------------
# Part 2

pos = 50
ans2 = 0
for direc, amount in instructions:
  full_turns = amount // 100
  ans2 += full_turns
  remain = amount % 100
  rotation = -remain if direc == "L" else remain
  end_pos = (pos + rotation) % 100
  # print(pos, f"{direc}{amount}", end_pos)
  if direc == "R":
    if (pos != 0 and end_pos < pos) or end_pos == 0:
      ans2 += 1
  elif direc == "L":
    if (pos != 0 and end_pos > pos) or end_pos == 0:
      ans2 += 1
  pos = end_pos

print("Part 2:", ans2)
