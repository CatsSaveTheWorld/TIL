T = int(input())

for tc in range(1, T+1):
    N = int(input())
    target_list = list(map(int, (input().split())))
    target_list.sort()
    target_list = list(map(str, target_list))
    target_str = ' '.join(target_list)
    
    print(f'#{tc} {target_str}')
    




