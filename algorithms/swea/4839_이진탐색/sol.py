#%%
# from math import floor

T = int(input())

def search_bisect_number(P:int, target_num:int):
    cnt = 1
    left = 0
    right = P
    center = (right - left) / 2
    while center != target_num:
        if center > target_num:
            right = center
            center = ((right + left) // 2)
            cnt += 1
        else:
            left = center
            center = ((right + left) // 2)
            cnt += 1
    return cnt

for tc in range(1, T+1):
    P, Pa, Pb = list(map(int, input().split()))
    count_a = search_bisect_number(P, Pa)
    count_b = search_bisect_number(P, Pb)
    
    if count_a < count_b:
        result = f'#{tc} A'
    elif count_a > count_b:
        result = f'#{tc} B'
    else:
        result = f'#{tc} {0}'     
    print(result)

#%%

    
    



#%%




#%%




#%%




#%%



