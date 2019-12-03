lines = list(map(int, open('data.in').readlines()))
# with open('data.in') as f:
#     for line in [line.strip() for line in f.readlines()]:

# first
# print(sum([x // 3 - 2 for x in lines]))

# second
_sum = 0
for x in lines:
    while (x := x // 3 - 2) > 0:
        _sum += x
print(_sum)
