def findStartOfPacketMarker(dataStream):
  for i in range(3, len(dataStream)):
    chars = []
    for j in range(i - 3, i + 1):
      if dataStream[j] not in chars:
        chars.append(dataStream[j])
      else:
        break
    if len(chars) == 4:
      return i + 1

with open('input.txt') as f:
  dataStream = f.readline()
  print(findStartOfPacketMarker(dataStream))