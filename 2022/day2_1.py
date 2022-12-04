# A = Rock = 1 = X
# B = Paper = 2 = Y
# C = Scissors = 3 = Z

score_map = {
    'A X': 3 + 1,
    'A Y': 6 + 2,
    'A Z': 0 + 3,
    'B X': 0 + 1,
    'B Y': 3 + 2,
    'B Z': 6 + 3,
    'C X': 6 + 1,
    'C Y': 0 + 2,
    'C Z': 3 + 3
}

## Read input file
input = []
with open('day2_input.txt', 'r') as f:
    for line in f.readlines():
        input.append(line.strip())


# Solve problem
def run():
    total = 0
    for line in input:
        total += score_map[line]
    print(total)



if __name__ == '__main__':
    run()
