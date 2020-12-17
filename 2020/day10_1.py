from pprint import pprint

input = []
with open('day9_input.txt', 'r') as f:
    for line in f.readlines():
        input.append(int(line.strip()))


# prepare prefix cache
prefix = 25
cache = []
for i in range(prefix-1):
    cache.append([])
    for j in range(prefix-i-1):
        cache[i].append(input[i]+input[i+j+1])

def check_val(cache, val):
    for c in cache:
        if val in c:
            return True
    return False

# start checking
err = None
for i in range(len(input)-prefix):
    val = input[i+prefix]
    if check_val(cache, val):
        cache = cache[1:]
        for j in range(prefix-2):
            cache[j].append(input[i+j+1]+val)
        cache.append([input[i+prefix-1]+val])
    else:
        err = i+prefix
        break
print(err)
print(input[err-25:err])
print(input[err])