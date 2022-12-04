# A = Rock     = 1
# B = Paper    = 2
# C = Scissors = 3

# X = lose = 0
# Y = draw = 3
# Z = win  = 6

score_map = {
    'A X': 3 + 0,
    'A Y': 1 + 3,
    'A Z': 2 + 6,
    'B X': 1 + 0,
    'B Y': 2 + 3,
    'B Z': 3 + 6,
    'C X': 2 + 0,
    'C Y': 3 + 3,
    'C Z': 1 + 6
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
