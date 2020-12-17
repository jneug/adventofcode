from pprint import pprint

input = []
with open('day9_input.txt', 'r') as f:
    for line in f.readlines():
        input.append(int(line.strip()))


# Solution of problem 1
invalid_idx = 511
invalid_val = input[invalid_idx]

def adder(input, low=0, high=2):
    s = sum(input[low:high])
    if s == invalid_val:
        return min(input[low:high])+max(input[low:high])
    elif s > invalid_val:
        return adder(input, low+1, high)
    else:
        return adder(input, low, high+1)

print(adder(input))