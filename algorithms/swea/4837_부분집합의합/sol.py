#%%
from itertools import combinations

T = int(input())

for tc in range(1, T+1):
    A = [x for x in range(1, 13)]
    N, K = tuple(map(int, input().split()))
    combi_list_a_n = combinations(A, N)
    count_K = 0
    
    for tuple_combi in combi_list_a_n:
        if sum(tuple_combi) == K:
            count_K += 1
    
    print(f'#{tc} {count_K}')
    

#%%

print('1 4 7 8 0')
print(1 4 7 8 0)


#%%




#%%
