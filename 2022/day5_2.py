
## Read input file
input = []
with open('day5_input.txt', 'r') as f:
    for line in f.readlines():
        input.append(line.rstrip())


# Solve problem
def run():
    layout = {(i+1): list() for i in range(9)}

    move = False
    for line in input:
        if len(line) == 0:
            move = True
            for i in range(9):
                layout[i+1].reverse()
            print(layout)
        elif not move and line.lstrip()[0] == '[':
            for i in range(9):
                crate = line[i*4 + 1:i*4 + 2]
                if crate != ' 'and crate != '':
                    layout[i+1].append(crate)
        elif move:
            line = line.split(' ')
            amount, stack1, stack2 = int(line[1]), int(line[3]), int(line[5])

            layout[stack2].extend(layout[stack1][-amount:])
            layout[stack1] = layout[stack1][:-amount]
    print(''.join(s[-1] for s in layout.values()))


if __name__ == '__main__':
    run()
