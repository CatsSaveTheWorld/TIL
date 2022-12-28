#%%
import os
# os.chdir('../1209_빙고Sum')
os.getcwd()

#%%
infile = open('input.txt', 'r', encoding='utf-8')

T = int(input())

for tc in range(1, T+1):
    puzzle_list = []
    for line in infile:
        line_list = line.split(' ')
        line_list.remove(line_list[-1])
        line_list = list(map(int, line_list))
        puzzle_list.append(line_list)
    
    max_num = 0




#%%
for horizon_line in puzzle_list:
    if sum(horizon_line) > max_num:
        max_num = sum(horizon_line)
    print(max_num)



#%%





