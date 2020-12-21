#%%
with open('input.txt', 'r') as f:
    read_data = f.readlines()
    read_data = list(map(lambda s: s.strip(), read_data))
    read_data = list(map(lambda s: int(s), read_data))

# %%
'''
Part 1
'''
for x in read_data:
    for y in read_data:
        if x + y == 2020:
            print(f'{x} + {y} = {x+y}')
            print(f'{x} * {y} = {x*y}')

# %%
'''
Part 2
'''
for x in read_data:
    for y in read_data:
        for z in read_data:
            if x + y + z == 2020:
                print(f'{x} + {y} + {z}= {x+y+z}')
                print(f'{x} * {y} * {z}= {x*y*z}')
# %%
