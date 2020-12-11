import re

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


def test_hgt(x):
    if x[-2:] == 'cm':
        hgt = int(x[:-2])
        return hgt >= 150 and hgt <= 193
    elif x[-2:] == 'in':
        hgt = int(x[:-2])
        return hgt >= 59 and hgt <= 76
    else:
        return False

valid = 0
keys = {
    'byr': lambda x: re.fullmatch(r'\d{4}', x) and int(x) >= 1920 and int(x) <= 2002,
    'iyr': lambda x: re.fullmatch(r'\d{4}', x) and int(x) >= 2010 and int(x) <= 2020,
    'eyr': lambda x: re.fullmatch(r'\d{4}', x) and int(x) >= 2010 and int(x) <= 2030,
    'hgt': test_hgt,
    'hcl': lambda x: re.fullmatch(r'#[0-9a-f]{6}', x),
    'ecl': lambda x: re.fullmatch(r'(amb|blu|brn|gry|grn|hzl|oth)', x),
    'pid': lambda x: re.fullmatch(r'\d{9}', x)
}
for passport in passports:
    if passport.keys() == keys.keys():
        val = True
        for k,v in keys.items():
            val = val and v(passport[k])
        if val:
            valid += 1
print(valid)