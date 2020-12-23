# %%
with open('input.txt', 'r') as f:
    read_data = f.readlines()

def count_trees(slope_left,slope_down):
    counter,counter_tree,y,x = 0,0,0,0
    print(f'\n{slope_left}, {slope_down}\n')
    while counter < len(read_data) - 1:
        counter += slope_down
        y += slope_down
        x += slope_left
        read_data[y] = read_data[y].strip()
        if x >= len(read_data[y]) - 1:
            x -= len(read_data[y])
        print(f'{y},{x}\t{read_data[y]}\t{read_data[y][x]}')
        if read_data[y][x] == '#':
            counter_tree += 1
    return(counter_tree)
'''
Part 1

print(count_trees(3,1))
'''
'''
Part 2
'''
counter_trees = list()
slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
for slope in slopes:
    counter_trees.append(count_trees(slope[0],slope[1]))

prod_all = False
for counter in counter_trees:
    if not prod_all:
        prod_all = counter
    else:
        prod_all *= counter
print(prod_all)
# %%
