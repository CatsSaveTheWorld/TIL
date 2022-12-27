T = int(input())

def make_combinations(target_list:list, r:int):
    from itertools import combinations

    com_list = []
    for i in combinations(target_list, r):
        com_list.append(i)
    
    return com_list

for tc in range(1, T+1):
    A = [x for x in range(1, 13)]
    N, K = tuple(map(int, input().split()))
    combi_list_a_n = make_combinations(A, N)
    count_K = 0
    
    for tuple_combi in combi_list_a_n:
        if sum(tuple_combi) == K:
            count_K += 1
    
    print(f'#{tc} {count_K}')