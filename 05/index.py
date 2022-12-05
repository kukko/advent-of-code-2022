from pprint import pprint
with open('input.txt') as f:
  text = f.read()
  [stack, movements] = list(map(lambda a: a.split('\n'), text.split('\n\n')))
  movements = list(map(lambda a: list(map(lambda b: int(b), a.replace('move ', '').replace(' from ', ',').replace(' to ', ',').split(','))), movements))
  stacks = {}
  for i in range(len(stack) - 1):
    for j in range(0, len(stack[i]), 4):
      box = stack[i][j:j+3]
      if len(box.strip()) > 0:
        stackIndex = int(stack[-1][j:j+3].strip())
        if stackIndex not in stacks.keys():
          stacks[stackIndex] = []
        stacks[stackIndex] = [box.strip('[]')] + stacks[stackIndex]
  for movement in movements:
    stacks[movement[2]] = stacks[movement[2]] + stacks[movement[1]][:movement[0]*-1-1:-1]
    stacks[movement[1]] = stacks[movement[1]][0:movement[0]*-1]
  result = ''
  for i in sorted(stacks.keys()):
    result += stacks[i][-1]
  print(result)