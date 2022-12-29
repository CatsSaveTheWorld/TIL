#%%
import os

os.chdir('../1954_달팽이숫자')
os.getcwd()     # 'c:\\Users\\4ser\\Documents\\TIL\\algorithms\\swea\\1954_달팽이숫자'

#%%
N = list(open('input.txt', 'r'))

# \n 제거
for idx, line in enumerate(N):
    if '\n' in line:
        line = line.replace('\n', '')
        N[idx] = line

# T = int(input())

# 일괄 int화 및 N에서 10제거
N = list(map(int, N))
T = N.pop(0)

for tc in range(1, T+1):
    # N = int(input())
    new_list = []
    add_num = 1

    # 빈 2차원 리스트 생성
    for _ in range(N[tc-1]):
        extend_list = []
        for __ in range(N[tc-1]):
            extend_list.append(0)
        new_list.append(extend_list)
    
    # 그리기 시작
    # N = int(input())
    for idx, row in enumerate(new_list):
        for jdx, value in enumerate(row):
            if idx == 0:                # 첫줄 채우기
                new_list[idx][jdx] = add_num
                add_num += 1
                continue

            if value == row[-1]:
                if new_list[idx][-1] == 0:
                    new_list[idx][-1] = add_num
                    add_num += 1
                    continue
            

    print(f'#{tc} {new_list}')

#%%





