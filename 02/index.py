from functools import reduce
print(reduce(lambda e, f: e + (6 if f[2] == 1 or f[2] == -2 else 3 if f[2] == 0 else 0) + (f[1] + 1), map(lambda d: d + [d[1] - d[0]], list(map(lambda a: list(map(lambda c: c - 88 if c > 67 else c - 65, map(lambda b: ord(b), a.replace('\n', '').split(
    ' ')))), open('input.txt').readlines()))), 0))