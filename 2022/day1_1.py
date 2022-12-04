max_cal = 0

with open('day1_input.txt', 'r') as f:
    sum = 0
    for line in f.readlines():
        if line.strip():
            sum += int(line)
        else:
            if sum > max_cal:
                max_cal = sum
            sum = 0

print(max_cal)
