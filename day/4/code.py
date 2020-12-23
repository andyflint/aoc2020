
# %%
import re
def get_data(raw_data):
    data = list()
    tmp_dict = dict()
    raw_data.append('\n')
    for line in raw_data:
        if line == '\n':
            data.append(tmp_dict)
            tmp_dict = {}
        else:
            for tmp_data in line.strip().split(' '):
                tmp_data = tmp_data.split(':')
                tmp_dict.update({tmp_data[0] : tmp_data[1]})
    return data
'''
Part 1
def validate_data(passport):
    patterns = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return set(patterns).issubset(set(passport.keys()))
'''
def validate_byr(byr):
    return int(byr) in range(1902,2003)

def validate_iyr(iyr):
    return int(iyr) in range(2010,2021)

def validate_eyr(eyr):
    return int(eyr) in range(2020,2031)

def validate_hgt(hgt):
    match =  re.match('([0-9]+)(in|cm)', hgt)
    if match:
        if match.group(2) == 'cm':
            return int(match.group(1)) in range(150,194)
        if match.group(2) == 'in':
            return int(match.group(1)) in range(59,77)

def validate_hcl(hcl):
    return bool(re.match('#[0-9a-f]{6}', hcl))

def validate_ecl(ecl):
    return bool(re.search('amb|blu|brn|gry|grn|hzl|oth', ecl))

def validate_pid(pid):
    return bool(re.search('[0-9]{9}', pid))

def validate_data(passport):
    patterns = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    if set(patterns).issubset(set(passport.keys())):
        print(passport)
        print(f"byr:{validate_byr(passport['byr'])}")
        print(f"iyr:{validate_iyr(passport['iyr'])}")
        print(f"eyr:{validate_eyr(passport['eyr'])}")
        print(f"hgt:{validate_hgt(passport['hgt'])}")
        print(f"hcl:{validate_hcl(passport['hcl'])}")
        print(f"ecl:{validate_ecl(passport['ecl'])}")
        print(f"pid:{validate_pid(passport['pid'])}")
        if (    validate_byr(passport['byr']) 
            and validate_iyr(passport['iyr'])
            and validate_eyr(passport['eyr'])
            and validate_hgt(passport['hgt'])
            and validate_hcl(passport['hcl'])
            and validate_ecl(passport['ecl'])
            and validate_pid(passport['pid'])
        ):
            return True
        else: 
            return False
    else: 
        return False


with open('input.txt', 'r') as f:
    read_data = f.readlines()

passports = get_data(read_data)

validated = map(validate_data, passports)
print(sum(list(validated)))
# %%

# %%
