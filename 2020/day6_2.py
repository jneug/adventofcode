from functools import reduce

input = []
with open('day6_input.txt', 'r') as f:
    group = []
    for line in f.readlines():
        if len(line.strip()) == 0:
            input.append(group)
            group = []
        else:
            group.append(line.strip())
    input.append(group)

def intersec(s, g):
    return s.intersection(set(g))

def counter(group):
    return len(reduce(intersec, group, set(group[0])))

print(sum([counter(g) for g in input]))