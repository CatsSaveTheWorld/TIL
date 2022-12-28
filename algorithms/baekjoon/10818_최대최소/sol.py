#%%
num = list(map(int, input('값을 입력하시오 : ').split()))
num



#%%
def arithmetic_sequence(target_num:int):
    import numpy as np
    
    for num in range(1, target_num+1):
        num_list = np.arange(1, num)
        list_sum = sum(num_list[:])

        if list_sum == target_num:
            return True
        if list_sum < target_num:
            continue
        else:
            return False

print(arithmetic_sequence())






#%%



