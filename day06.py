from collections import defaultdict, Counter

orbits = defaultdict(list)
indirect = defaultdict(int)
total = 0
with open('data.in', 'r') as f:
    for line in [line.strip() for line in f.readlines()]:
        key, value = line.split(')')
        orbits[key].append(value)
        indirect[value] = 1 + indirect[key]

for key, values in orbits.items():
    parent = [item for sublist in orbits.values() for item in sublist].count(key)
    for value in values:
        pass

print(sum(indirect.values()))
