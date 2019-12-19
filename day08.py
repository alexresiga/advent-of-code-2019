from more_itertools.recipes import grouper

W, L = 25, 6
data = list(map(int, open('data.in').read()))
layers = list(grouper(list(grouper(data, W)), L))
fewest = min(layers, key=lambda x: sum(s.count(0) for s in x))
print(sum(s.count(1) for s in fewest) * sum(s.count(2) for s in fewest))
# part 2
image = [[None for _ in range(W)] for _ in range(L)]
for layer in layers:
    for i, row in enumerate(layer):
        for j, column in enumerate(row):
            if column != 2 and image[i][j] is None:
                image[i][j] = '#' if column == 1 else ' '

print('\n'.join([' '.join(row) for row in image]))
