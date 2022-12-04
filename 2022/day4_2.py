
## Read input file
input = []
with open('day4_input.txt', 'r') as f:
    for line in f.readlines():
        input.append(line)


# Solve problem
def run():
    count = 0

    for line in input:
        first, second = line.split(',')
        first = make_range(first)
        second = make_range(second)

        if overlaps(first, second) or overlaps(second, first):
            count += 1

    print(count)

def make_range( a ):
    return tuple(int(i) for i in a.split('-'))

def overlaps( r1, r2 ):
    return not (r2[1] < r1[0] or r2[0] > r1[1])

if __name__ == '__main__':
    run()
