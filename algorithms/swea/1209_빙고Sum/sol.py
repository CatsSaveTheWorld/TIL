#%%
import os
# os.chdir('../1209_빙고Sum')
os.getcwd()

#%%
# 미완성
infile = open('input.txt', 'r', encoding='utf-8')

T = int(input())

for tc in range(1, T+1):
    horizon_puzzle_list = []
    vertical_puzzle_list = []
    flag_list = []
    max_num = 0
    cnt = 0

    # 가로 puzzle list 생성
    for line in infile:
        line_list = line.split(' ')
        line_list.remove(line_list[-1])
        line_list = list(map(int, line_list))
        horizon_puzzle_list.append(line_list)

    # 세로 puzzle list 생성
    for idx, horizon_line in enumerate(horizon_puzzle_list):
        if idx >= 100:
            vertical_puzzle_list.append(flag_list)
            break
        flag_list.append(horizon_line[0])
        cnt += 1

    # 가로, 대각 max값 탐색
    diagonal_line = []
    for idx, hor_val in enumerate(horizon_puzzle_list):
        for jdx, ver_val in hor_val:
            if idx == jdx:
                diagonal_line.append(ver_val)
        if sum(horizon_line) > max_num:
            max_num = sum(horizon_line)
    
    # 세로, 반대각 max값 탐색
    diagonal_line = []
    for idx, ver_val in enumerate(vertical_puzzle_list):
        for jdx, ver_val in ver_val:
            if idx == jdx:
                diagonal_line.append(ver_val)
        max_num = sum(diagonal_line)
        if sum(ver_val) > max_num:
            max_num = sum(ver_val)
        
    
    # 가로 max값 탐색
    # for horizon_line in horizon_puzzle_list:
    #     if sum(horizon_line) > max_num:
    #         max_num = sum(horizon_line)

    # # 세로 max값 탐색
    # for vertical_line in vertical_puzzle_list:
    #     if sum(vertical_line) > max_num:
    #         max_num = sum(vertical_line)
    

        

max_num
    
    


#%%

# infile = open('input.txt', 'r', encoding='utf-8')

# for line in infile:
#     line_list = line.split(' ')
#     line_list.remove(line_list[-1])
#     line_list = list(map(int, line_list))
#     horizon_puzzle_list.append(line_list)

len(horizon_puzzle_list[0])






#%%








