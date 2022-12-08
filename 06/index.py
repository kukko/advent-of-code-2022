def findStartOfPacketMarker(dataStream, lengthOfMarker):
  for i in range(lengthOfMarker - 1, len(dataStream)):
    chars = []
    for j in range(i - (lengthOfMarker - 1), i + 1):
      if dataStream[j] not in chars:
        chars.append(dataStream[j])
      else:
        break
    if len(chars) == lengthOfMarker:
      return i + 1

with open('input.txt') as f:
  dataStream = f.readline()
  print(findStartOfPacketMarker(dataStream, 4))
  print(findStartOfPacketMarker(dataStream, 14))