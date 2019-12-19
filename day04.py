start, end = list(map(int, open('data.in').readline().split('-')))


def check(inp):
    return any([inp[i] == inp[i + 1] for i in range(len(inp) - 1)]) and all(
        [inp[i] <= inp[i + 1] for i in range(len(inp) - 1)])


def part_2(inp):
    for i in range(len(inp) - 1):
        var = True
        if inp[i] != inp[i + 1]:
            var = False
        if i > 0:
            if inp[i - 1] == inp[i]:
                var = False
        if i < len(inp) - 2:
            if inp[i + 1] == inp[i + 2]:
                var = False
        if var:
            return True
    return False


def check_part2(inp):
    return part_2(inp) and all([inp[i] <= inp[i + 1] for i in range(len(inp) - 1)])


print(len(list(filter(lambda x: check_part2(str(x)), [x for x in range(start, end)]))))
