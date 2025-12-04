# Day 03: Lobby

import sys
CLR = "\33[2K\r"

# ==============================================================================

# Get filename of input as CLI arg. If not given, default to "input.txt"
if len(sys.argv) == 1:
  input_fname = "input.txt"
else:
  input_fname = sys.argv[1]

# Read and parse input
battery_banks = []
with open(input_fname) as f:
  for line in f:
    battery_banks.append(line.strip())

# ------------------------------------------------------------------------------
# Part 1

ans1 = 0
digits = [str(d) for d in range(9, 0, -1)]
for bank in battery_banks:
  for d1 in digits:
    idx1 = bank.find(str(d1), 0, -1)
    if idx1 != -1:
      break
  for d2 in digits:
    idx2 = bank.find(str(d2), idx1+1)
    if idx2 != -1:
      break  
  n = int(d1 + d2)
  ans1 += n

print("Part 1:", ans1)

# ------------------------------------------------------------------------------
# Part 2

ans2 = 0
num_to_select = 12
for bank in battery_banks:
  selected = []
  start = 0
  for i in range(num_to_select):
    for d in digits:
      end = len(bank)-num_to_select+i+1
      idx = bank.find(str(d), start, end)
      if idx != -1:
        selected.append(d)
        start = idx+1
        break
  n = int("".join(selected))
  ans2 += n

print("Part 2:", ans2)
