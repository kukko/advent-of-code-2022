with open('input.txt') as f:
    lines = list(map(lambda b: [b[:int(len(b)/2)], b[int(len(b)/2):]],
                 map(lambda a: a.replace('\n', ''), f.readlines())))
    sum = 0
    for line in lines:
        alreadyFound = []
        for item in line[0]:
            if item not in alreadyFound and item in line[1]:
                alreadyFound.append(item)
                if ord(item) > 90:
                    sum = sum + ord(item) - 96
                else:
                    sum = sum + ord(item) - 38
    print(sum)
    badgeSum = 0
    for i in range(0, len(lines), 3):
        found = False
        for j in lines[i][0] + lines[i][1]:
            for k in range(1, 3):
                contains = False
                for l in lines[i + k][0] + lines[i + k][1]:
                    if j == l:
                        contains = True
                        break
                if contains == False:
                    break
                elif k == 2:
                    found = True
                    if ord(j) > 90:
                        badgeSum = badgeSum + ord(j) - 96
                    else:
                        badgeSum = badgeSum + ord(j) - 38
            if found == True:
                break
    print(badgeSum)