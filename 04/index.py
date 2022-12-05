with open('input.txt') as f:
  lines = list(map(lambda a: list(map(lambda b: list(map(lambda c: int(c), b.split('-'))), a.replace('\n', '').split(','))), f.readlines()))
  count = 0
  for line in lines:
    if (line[0][0] <= line[1][0] and line[0][1] >= line[1][1]) or (line[0][0] >= line[1][0] and line[0][1] <= line[1][1]):
      count += 1
  print(count)