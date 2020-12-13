input = []
with open('day8_input.txt', 'r') as f:
    for line in f.readlines():
        cmd,param = line.strip().split()
        input.append((cmd, int(param)))


def terminates( prg ):
    idx = 0
    acc = 0
    visited = []
    running = True
    while running:
        if idx >= len(prg):
            return (True, acc)
        elif idx in visited:
            return (False, acc)

        cmd,param = prg[idx]
        visited.append(idx)
        if cmd == 'acc':
            acc += param
            idx += 1
        elif cmd == 'jmp':
            idx += param
        else: # nop
            idx += 1

def mutate_code( prg ):
    for idx,cmd in enumerate(prg):
        if cmd[0] == 'nop':
            prg[idx] = ('jmp', prg[idx][1])
            term,acc = terminates(prg)
            if term:
                return (idx, acc)
            prg[idx] = ('nop', prg[idx][1])
        elif cmd[0] == 'jmp':
            prg[idx] = ('nop', prg[idx][1])
            term,acc = terminates(prg)
            if term:
                return (idx, acc)
            prg[idx] = ('jmp', prg[idx][1])

print(mutate_code(input))