# %%
''' 
Part 1
def check_pw(rule_count, rule_char, password):
    return password.count(rule_char) in rule_count
'''

'''
Part2
'''
def check_pw(rule_count, rule_char, password):
    print(f'{rule_char} == {password[rule_count[0] - 1]} or {rule_char} == {password[rule_count[1] - 1]}')
    return (rule_char == password[rule_count[0] - 1]) ^ (rule_char == password[rule_count[1] - 1])

def get_rule_pw(rule_pw):
    split_string = rule_pw.replace(':', '').strip().split(' ')
    #print(split_string)
    rule_count = split_string[0].split('-')
    #Part 1
    #rule_count = range(int(rule_count[0]), int(rule_count[1]) + 1)
    #Part 2
    rule_count = int(rule_count[0]), int(rule_count[1])
    rule_char = split_string[1]
    password = split_string[2]
    if check_pw(rule_count, rule_char, password):
        print(rule_pw)
        return password

with open('input.txt', 'r') as f:
    read_data = f.readlines()

#print(read_data)
counter = 0
for line in read_data:
    if get_rule_pw(line):
        counter += 1
print(counter)        
# %%

# %%
