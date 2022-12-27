#%%
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    red_color_area_1 = [[False for col in range(10)] for row in range(10)]
    blue_color_area_1 = [[False for col in range(10)] for row in range(10)]
    # purple_idx_list = [[False for column in range(10)] for row in range(10)]
    purple_count = 0

    for _ in range(N):
        info_list = list(input())
        info_list = list(map(int, info_list))

        if info_list[-1] == 1:                      # ex) 22441
            for row in range(info_list[0], info_list[2]+1):
                for column in range(info_list[1], info_list[3]+1):
                    red_color_area_1[row][column] = True
        elif info_list[-1] == 2:                      # ex) 33662
            for row in range(info_list[0], info_list[2]+1):
                for column in range(info_list[1], info_list[3]+1):
                    blue_color_area_1[row][column] = True
        
        for idx_row, row in enumerate(red_color_area_1):
            for idx_column, column in enumerate(blue_color_area_1):
                if red_color_area_1[idx_row][idx_column] == True and blue_color_area_1[idx_row][idx_column] == True:
                    # purple_idx_list[idx_row][idx_column] = True
                    purple_count += 1
    print(f'#{tc} {purple_count}')

#%%
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    red_color_area_1 = [[False for col in range(10)] for row in range(10)]
    blue_color_area_1 = [[False for col in range(10)] for row in range(10)]
    purple_count = 0

    for _ in range(N):
        info_list = list(input())
        info_list = list(map(int, info_list))

        if info_list[-1] == 1:                      # ex) 22441
            for row in range(info_list[0], info_list[2]+1):
                for column in range(info_list[1], info_list[3]+1):
                    if red_color_area_1[row][column] == False:
                        red_color_area_1[row][column] = True
        elif info_list[-1] == 2:                      # ex) 33662
            for row in range(info_list[0], info_list[2]+1):
                for column in range(info_list[1], info_list[3]+1):
                    if blue_color_area_1[row][column] == False:
                        blue_color_area_1[row][column] = True
        
        for idx_row, row in enumerate(red_color_area_1):
            for idx_column, column in enumerate(row):
                if red_color_area_1[idx_row][idx_column] == True and blue_color_area_1[idx_row][idx_column] == True:
                    purple_count += 1
    print(f'#{tc} {purple_count}')
#%%
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    red_color_area_1 = [[False for col in range(10)] for row in range(10)]
    blue_color_area_1 = [[False for col in range(10)] for row in range(10)]
    purple_idx_list = [[False for column in range(10)] for row in range(10)]
    purple_count = 0

    for _ in range(N):
        info_list = list(input())
        info_list = list(map(int, info_list))

        if info_list[-1] == 1:  # info_list의 마지막이 1일경우 red_color_area_1를 색칠
            for row in range(info_list[0], info_list[2]+1):
                for column in range(info_list[1], info_list[3]+1):
                    if red_color_area_1[row][column] == False:
                        red_color_area_1[row][column] = True
        elif info_list[-1] == 2:# info_list의 마지막이 1일경우 blue_color_area_1를 색칠
            for row in range(info_list[0], info_list[2]+1):
                for column in range(info_list[1], info_list[3]+1):
                    if blue_color_area_1[row][column] == False:
                        blue_color_area_1[row][column] = True
        
        # red_color_area_1와 blue_color_area_1의 True가 일치하는 원소의 갯수를 카운팅.
        for idx_row, row in enumerate(red_color_area_1):
            for idx_column, column in enumerate(row):
                if red_color_area_1[idx_row][idx_column] == True and blue_color_area_1[idx_row][idx_column] == True:
                    purple_idx_list[idx_row][idx_column] = True
                    purple_count += 1
    print(f'#{tc} {purple_count}')


#%%





#%%





#%%





#%%




