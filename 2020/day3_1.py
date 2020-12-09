input = []
with open('day3_input.txt', 'r') as f:
    for line in f.readlines():
        input.append(line.strip())

start = (0, 0)
slope = (3, 1)

def slide(forest, pos, slope):
    if pos[1]+slope[1] >= len(forest):
        return 0
    else:
        pos[0] += slope[0]
        pos[1] += slope[1]
        row = forest[pos[1]]
        if row[pos[0]%len(row)] == '#':
            return 1 + slide(forest, pos, slope)
        else:
            return slide(forest, pos, slope)

print(slide(input, list(start), slope))