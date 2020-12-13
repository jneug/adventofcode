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

def walk_bags(name, bags):
    count = 1
    if name in bags:
        for child in bags[name]:
            count += child[0] * walk_bags(child[1], bags)
    return count


search = 'shiny gold bag'
print(walk_bags(search, input)-1)