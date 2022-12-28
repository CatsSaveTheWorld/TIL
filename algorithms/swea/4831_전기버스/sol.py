T = int(input())

for cycle in range(1, T+1):
    K, N, M = list(map(int, input().split()))
    charge_bustop = input()
    charge_bustop = list(map(int, charge_bustop.split()))

    count = curr = 0

    while N > curr + K:
        for step in range(K, 0, -1):
            if curr + step in charge_bustop:
                curr += step
                count += 1
                break
        else:
            count = 0
            break
    print(f'#{cycle} {count}')



    # print(f'#{cycle} {charge_count}')




    # print(f'#{cycle} ')

'''
로직
1. number(현재위치) <=  
2. 
'''


