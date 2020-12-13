input = []
with open('day8_input.txt', 'r') as f:
    for line in f.readlines():
        cmd,param = line.strip().split()
        input.append((cmd, int(param)))


idx = 0
acc = 0
visited = []
running = True
while running:
    if idx >= len(input):
        break
    elif idx in visited:
        break

    cmd,param = input[idx]
    visited.append(idx)
    if cmd == 'acc':
        acc += param
        idx += 1
    elif cmd == 'jmp':
        idx += param
    else: # nop
        idx += 1

print(acc)