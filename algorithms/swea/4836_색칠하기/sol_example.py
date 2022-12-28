#%%
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [[0 for _ in range(10)] for _ in range(10)]
    counter = 0

    # 색칠 시작
    for _ in range(N):
        # 시작r, 시작c, 끝r, 끝c, 색깔
        r1, c1, r2, c2, color = map(int, input().split())

        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                matrix[r][c] += color
    
    # 색칠 끝나고 보라색(3)검사.
    for r in range(10):
        for c in range(10):
            if matrix[r][c] == 3:
                counter += 1

    print(f'#{tc} {counter}')