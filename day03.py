from math import inf


def manhattan_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


wires = []
with open('data.in', 'r') as f:
    for line in [line.strip() for line in f.readlines()]:
        wires.append(line.split(','))

print(wires)
SIZE = 1700
grid = [[0 for _ in range(SIZE)] for _ in range(SIZE)]
central_point = (SIZE // 2, SIZE // 2)
cross = []
start_x = SIZE // 2
start_y = SIZE // 2
print('start')
for index, wire in enumerate(wires, start=1):
    current_x, current_y = start_x, start_y
    print(len(wire))
    for part in wire:
        if part[0] == 'R':

            for y in range(1, int(part[1:]) + 1):
                if grid[current_x][current_y + y] != 0 and grid[current_x][current_y + y] != index:
                    cross.append((current_x, current_y + y))
                else:
                    grid[current_x][current_y + y] = index
            current_y += int(part[1:])
        if part[0] == 'L':
            for y in range(1, int(part[1:]) + 1):
                if grid[current_x][current_y - y] != 0 and grid[current_x][current_y - y] != index:
                    cross.append((current_x, current_y - y))
                else:
                    grid[current_x][current_y - y] = index
            current_y -= int(part[1:])
        if part[0] == 'U':
            for k in range(1, int(part[1:]) + 1):
                if grid[current_x - k][current_y] != 0 and grid[current_x - k][current_y] != index:
                    cross.append((current_x - k, current_y))
                else:
                    grid[current_x - k][current_y] = index
            current_x -= int(part[1:])
        if part[0] == 'D':
            print(int(part[1:]))
            for k in range(1, int(part[1:]) + 1):
                if grid[current_x + k][current_y] != 0 and grid[current_x + k][current_y] != index:
                    cross.append((current_x + k, current_y))
                else:
                    grid[current_x + k][current_y] = index
            current_x += int(part[1:])
print(cross)
min_dist = inf
for c in cross:
    if manhattan_distance(c, central_point) < min_dist:
        min_dist = manhattan_distance(c, central_point)
print(min_dist)
