from itertools import product

i_lines = list(map(int, open('data.in').readline().split(',')))
for a, b in product(range(100), range(100)):
    lines = i_lines[:]
    lines[1], lines[2] = a, b
    i = 0
    while i < len(lines):
        if lines[i] == 1:
            lines[lines[i + 3]] = lines[lines[i + 1]] + lines[lines[i + 2]]
        elif lines[i] == 2:
            lines[lines[i + 3]] = lines[lines[i + 1]] * lines[lines[i + 2]]
        elif lines[i] == 99:
            break
        i += 4
    if lines[0] == 19690720:
        print(lines[1] * 100 + lines[2])
        break
