lines = list(map(int, open('data.in', 'r').readlines()))
# with open('data.in', 'r') as f:
#     for line in [line.strip() for line in f.readlines()]:

# first
# print(sum([x // 3 - 2 for x in lines]))

# second
_sum = 0
for x in lines:
    while x // 3 - 2 > 0:
        x = x // 3 - 2
        _sum += x
print(_sum)
