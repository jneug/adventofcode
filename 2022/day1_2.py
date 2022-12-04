calories = list()

with open('day1_input.txt', 'r') as f:
    _sum = 0
    for line in f.readlines():
        if line.strip():
            _sum += int(line)
        else:
            calories.append(_sum)
            _sum = 0

calories.sort(reverse=True)
print(calories[0:3])
print(sum(calories[0:3]))
