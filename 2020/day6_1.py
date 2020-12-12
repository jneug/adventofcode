input = []
with open('day6_input.txt', 'r') as f:
    group = ''
    for line in f.readlines():
        if len(line.strip()) == 0:
            input.append(group)
            group = ''
        else:
            group += line.strip()
    input.append(group)

def counter(group):
    return len(set(group))
print(sum(map(counter, input)))

print(input[0])
print(set(input[0]))