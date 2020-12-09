input = []
with open('day1_input.txt', 'r') as f:
    for line in f.readlines():
        input.append(int(line))

def brute_force( nums, idx ):
    for i in range(len(nums)-idx-1):
        if nums[idx]+nums[i+idx+1] == 2020:
            return (nums[idx], nums[i+idx+1], nums[idx]*nums[i+idx+1])
    return None

res = None
for i in range(len(input)):
    res = brute_force(input, i)
    if res:
        break
print(res)