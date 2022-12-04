
## Read input file
input = []
with open('day3_input.txt', 'r') as f:
    for line in f.readlines():
        input.append(line.strip())


# Solve problem
def run():
    total = 0

    group = []
    for line in input:
        if len(group) < 3:
            group.append(set(line))
        if len(group) == 3:
            isect = group[0].intersection(group[1], group[2])
            if len(isect) > 1:
                print(isect)

            for i in isect:
                common = i
            if common.islower():
                total += ord(common) - 96
            else:
                total += ord(common) - 38
            group = []

    print(total)



if __name__ == '__main__':
    run()
