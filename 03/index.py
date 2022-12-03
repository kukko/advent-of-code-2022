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
