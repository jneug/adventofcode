input = []
with open('day2_input.txt', 'r') as f:
    for line in f.readlines():
        line = line.split(' ');
        a,b = line[0].split('-');
        input.append(((int(a),int(b)), line[1][0], line[2].strip()))

def check_pwd(p):
    rule, char, pwd = p[0], p[1], p[2]
    if (pwd[rule[0]-1] == char or pwd[rule[1]-1] == char) and (pwd[rule[0]-1] != pwd[rule[1]-1]):
        return 1
    else:
        return 0

print(sum(map(check_pwd, input)))