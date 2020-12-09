input = []
with open('day1_input.txt', 'r') as f:
    for line in f.readlines():
        input.append(int(line))

def find_sum(nums, s, idx):
    for i in range(len(nums)-idx-1):
        for j in range(len(nums)-i-2):
            if nums[i+idx+1]+nums[j+i+2] == s:
                return (i+idx+1,j+i+2)
    return None

res = None
for i in range(len(input)):
    res = find_sum(input, 2020-input[i], i)
    if res:
        res = (input[i], input[res[0]], input[res[1]])
        break
print(res)
print(sum(res))
print(res[0]*res[1]*res[2])