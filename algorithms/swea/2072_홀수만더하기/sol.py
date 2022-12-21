#%%
# import sys
# sys.stdin = open('input.txt')

# 여기부터 고정
T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input().split()))

    total = 0
    
    for num in numbers:
        if num % 2 == 1:
            total += num
# 여기까지 고정

#%%
for tc in range(1, T+1):
    numbers = list(map(int, input().split()))
    print(f'#{tc} {total}')




