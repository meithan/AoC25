# Day 10: Factory

import re
import sys
import queue
import numpy as np
import scipy

CLR = "\33[2K\r"

# ==============================================================================

# Get filename of input as CLI arg. If not given, default to "input"
if len(sys.argv) == 1:
  input_fname = "input"
else:
  input_fname = sys.argv[1]

# Read and parse input
machines1 = []
machines2 = []
with open(input_fname) as f:
  for line in f:
    m = re.match(r"\[([#.]+)\]", line)
    target_state = ["1" if c == "#" else "0" for c in m.group(1)]
    target_size = len(target_state)
    target_state = int("".join(target_state), 2)
    m = re.findall(r"(\([0-9,]+\))", line)
    buttons = []
    buttons2 = []
    for g in m:
      positions = eval(g)
      if type(positions) is not tuple:
        positions = tuple([positions])
      buttons2.append(positions)
      button = 0
      for pos in positions:
        button += 2**(target_size-pos-1)
      buttons.append(button)
    m = re.findall(r"\{(.+)\}", line)
    joltage_levels = tuple(eval(m[0]))
    machines1.append((target_state, buttons))
    machines2.append((joltage_levels, buttons2))

# ------------------------------------------------------------------------------
# Part 1

def solve(machine):
  target_state, buttons = machine
  start = 0
  Q = queue.Queue()
  explored = set()
  explored.add(start)
  Q.put([start, []])
  while not Q.empty():
    state, hist = Q.get()
    if state == target_state:
      return hist
    for button in buttons:
      next_state = state ^ button
      if next_state not in explored:
        explored.add(next_state)
        next_hist = hist + [button]
        Q.put([next_state, next_hist])

ans1 = 0
for machine in machines1:
  # print(machine)
  hist = solve(machine)
  ans1 += len(hist)

print("Part 1:", ans1)

# ------------------------------------------------------------------------------
# Part 2

# Too slow
# def solve2(machine):
#   target_joltage, buttons = machine
#   start = [0]*len(target_joltage)
#   Q = queue.Queue()
#   explored = set()
#   explored.add(tuple(start))
#   Q.put([start, []])
#   while not Q.empty():
#     state, hist = Q.get()
#     if tuple(state) == target_joltage:
#       return hist
#     for button in buttons:
#       next_state = state.copy()
#       for pos in button:
#         next_state[pos] += 1
#       # Check if next_state exceeds target_state
#       exceeds = False
#       for i in range(len(target_joltage)):
#         if next_state[i] > target_joltage[i]:
#           exceeds = True
#           break
#       if exceeds: continue
#       if tuple(next_state) not in explored:
#         explored.add(tuple(next_state))
#         next_hist = hist + [button]
#         Q.put([next_state, next_hist])

def solve2(machine):
  
  joltage, buttons = machine
  
  # Formulate into integer linear programming problem
  A = []
  for i in range(len(joltage)):
    row = []
    for button in buttons:
      if i in button:
        row.append(1)
      else:
        row.append(0)
    A.append(row)
  A = np.array(A)
  b = np.array(joltage)
  c = np.array([1]*len(buttons))
  
  # Solve ILP using scipy
  result = scipy.optimize.linprog(c=c, A_eq=A, b_eq=b, integrality=1)
  return np.round(result.x).astype(np.int32)

ans2 = 0
for machine in machines2:
  solution = solve2(machine)
  ans2 += np.sum(solution)

print("Part 2:", ans2)
