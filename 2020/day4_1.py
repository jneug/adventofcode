input = []
with open('day4_input.txt', 'r') as f:
    passport = []
    for line in f.readlines():
        if len(line.strip()) == 0:
            input.append(passport)
            passport = []
        else:
            passport += line.strip().split()
    input.append(passport)


passports = list()
p = dict()
for passport in input:
    for kv in passport:
        k,v = kv.split(':')
        if k != 'cid':
            p[k] = v
    passports.append(p)
    p = dict()


valid = 0
keys = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
for passport in passports:
    if passport.keys() == keys:
        valid += 1
print(valid)
print(passports[-1])
print(passports[-2])