'''
[문제]
M개의 합이 가장 큰 경우와 가장 작은 경우의 차이를 출력하는 프로그램을 작성하시오.
T = 테스트 개수 (테스트 예제가 총 3번)
N = 정수의 개수
M = 더할 이웃 정수의 개수

[입력]
1. 첫 줄에 테스트 케이스 개수 T가 주어진다.  ( 1 ≤ T ≤ 50 )
2. 다음 줄부터 테스트케이스의 첫 줄에 정수의 개수 N과 구간의 개수 M 주어진다. ( 10 ≤ N ≤ 100,  2 ≤ M ＜ N )
3. 다음 줄에 N개의 정수 ai가 주어진다. ( 1 ≤ a ≤ 10000 )

[출력]
각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

#1 21
#2 11088
#3 1090
'''

T = int(input())        # 3

for tag_num in range(1, T+1):
    N, M = input().split()
    N, M = int(N), int(M)
    numbers = input()
    numbers = list(map(int, numbers.split()))
    print(numbers)

    for idx, num in enumerate(numbers):
        flag_num = sum(numbers[idx:idx+M])
        print(f'{idx} +: {idx+M} = {flag_num}')

        if idx == 0:
            min_num = sum(numbers[:M])
            max_num = sum(numbers[:M])
        if flag_num < min_num:
            min_num = flag_num
        if flag_num > max_num:
            max_num = flag_num
        dif_max = max_num - min_num

        if N - M <= idx:
            break

    print(f'#{tag_num} {dif_max}')

'''
3

10 3
1 2 3 4 5 6 7 8 9 10

10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821

20 19
3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 19
'''