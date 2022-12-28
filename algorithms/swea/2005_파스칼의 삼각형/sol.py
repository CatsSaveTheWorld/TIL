#%%
# 작업디렉토리 위치 확인할 것. (안하면 input파일 안들어쳐먹음)
import os
# os.chdir('현재_디렉토리')
os.getcwd()
#%%
open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    pascal_list = [[0]*n for n in range(1, N+1)]
    
    for idx in range(N):
        if N == 1:
            pascal_list[0][0] = 1
            continue

        for jdx in range(idx+1):
            if jdx == 0 or jdx == idx:
                pascal_list[idx][jdx] = 1
                
            else:
                pascal_list[idx][jdx] = pascal_list[idx-1][jdx-1] + pascal_list[idx-1][jdx]
    
    print(f'#{tc}')
    for list_pas in pascal_list:
        for number_pas in list_pas:
            print(number_pas, end=' ')
        print()
#%%
pascal_list
#%%


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    #파스칼의 삼각형 값을 담을 배열 생성
    arr = [[0] * n for _ in range(n)]
    #양 끝에는 값을 1, 중앙 값은 위의 값의 합을 받는다.
    for i in range(n):
        for j in range(i+1):
            if j ==0 or j==i:
                arr[i][j]=1
            else:
                arr[i][j] = arr[i-1][j] + arr[i-1][j-1]
    #한 줄씩 출력
    print('#{}'.format(tc))
    #0이 아닌 값들만 출력
    for lst in arr:
        result = [x for x in lst if x]
        print(*result)




#%%

cycle = int(input()) # 반복 횟수 입력
numbers = [] # 출력 용 저장 리스트
temp = [] # 계산용 임시 리스트

for i in range(cycle): # 반복문
    numbers.append(1) # 첫부분 1 입력
    temp.append(1) # 계산용도 동일하게 적용
    if i < 2: 
        pass # 2가 넘어갈 될 때까지 무시
    else:
        for j in range(1, len(numbers)-1): # 계산
            temp[j] = numbers[j-1]+numbers[j]
    for j in range(len(numbers)): # 계산 완료된 코드를 다시 저장
        numbers[j]=temp[j]
        print(str(numbers[j]) + " ", end="") # 한줄로 출력
        
    print("") # 줄 띄우기





#%%

for idx in range(1):
    

#%%



