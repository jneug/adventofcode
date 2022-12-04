
## Read input file
input = []
with open('day3_input.txt', 'r') as f:
    for line in f.readlines():
        input.append(line.strip())


# Solve problem
def run():
    total = 0

    for line in input:
        l = int(len(line) / 2)
        left, right = set(line[:l]), set(line[l:])
        isect = left.intersection(right)
        for i in isect:
            common = i
        if common.islower():
            total += ord(common) - 96
        else:
            total += ord(common) - 38

    print(total)



if __name__ == '__main__':
    run()
