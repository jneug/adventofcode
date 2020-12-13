input = dict()
with open('day7_input.txt', 'r') as f:
    for line in f.readlines():
        if len(line.strip()) > 0:
            btype, content = line.strip()[:-1].split(' contain ')
            btype= btype[:-1]
            input[btype] = content.split(', ')
            for i,b in enumerate(input[btype]):
                if b == 'no other bags':
                    input[btype] = []
                else:
                    num,name = b.split(' ',1)
                    if int(num) > 1:
                        name = name[0:-1]
                    input[btype][i] = (int(num), name)

def walk_bags(name, cur, bags):
    if cur == name:
        return True
    elif cur in bags:
        for child in bags[cur]:
            if walk_bags(name, child[1], bags):
                return True
        return False
    else:
        return False


search = 'shiny gold bag'
count = 0
for bag in input.keys():
    if bag != search and walk_bags(search, bag, input):
        count += 1
print(count)