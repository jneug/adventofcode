
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

        if is_in(first, second) or is_in(second, first):
            count += 1

    print(count)

def make_range( a ):
    return tuple(int(i) for i in a.split('-'))

def is_in( r1, r2 ):
    return r1[0] <= r2[0] and r1[1] >= r2[1]

if __name__ == '__main__':
    run()
