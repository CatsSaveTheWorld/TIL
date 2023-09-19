#%%
def solution(name, yearning, photo):
    answer = []
    miss_dict = dict(zip(name, yearning))
    
    for case in photo:
        miss_sum = 0
        # print('==================================')
        # print(f'case : {case}')
        for human in name:
            # print('==================================')
            # print(f'human : {human}')
            if human in case:
                # print(f'miss_sum : {miss_sum}')
                miss_sum += miss_dict[human]
                # print(f'miss_sum : {miss_sum}')
        answer.append(miss_sum)
    return answer