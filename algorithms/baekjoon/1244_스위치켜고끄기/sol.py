'''
input.txt
첫줄 : 스위치 갯수
두번째줄 : 현재 스위치 상태
세번째줄 : 학생수 (100이하의 양의 정수)
넷째줄 ~ : 성별, 학생이 받은 수 (남자는 1, 여자는 2, 스위치 개수 이하의 양수)

남학생은 스위치 번호가 자기가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다.
즉, 스위치가 켜져 있으면 끄고, 꺼져 있으면 켠다.

여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서
가장 많은 스위치를 포함하는 구간을 찾아서, 그 구간에 속한 스위치의 상태를 모두 바꾼다.
'''

import sys

sys.stdin = open('input.txt')

N = int(input())

switches = list(map(int, input().split()))
student_cnt = int(input())

for _ in range(student_cnt):
    gender, num = map(int, input().split())

    # 남자 => num의 배수 스위치를 다 바꿈.
    if gender == 1:
        i = 1
        idx = num - 1
        while idx < N:
            switches[idx] = 0 if switches[idx] else 1
            # 혹은
            # switches[idx] ^= 1
            i += 1
            idx = (num * i) - 1
    # 여자 => num은 바꾸고, 좌우대칭이면 바꿈.
    else:
        switches[idx] ^= 1
        side = 1

        while 0 <= (idx - side) and (idx + side) < N:
            left = switches[idx - side]
            right = switches[idx + side]

        if left != right:
            break
        else:
            switches[idx - side] ^= 1
            switches[idx + side] ^= 1
            side += 1
for part_no in range(N // 20 + 1):
    start = 20 * part_no

'''
^ : XOR 연산
다르면 1, 같으면 0 반환

예시)
3 ^ 4 >> 7
3 = 011(2)
4 = 100(2)

011(2) + 100(2) = 111(2) => 7
'''



'''
infile = open("input.txt", 'r', encoding='utf-8')
infile_list = list(map(str, infile))

# ['8', '0 1 0 1 0 0 0 1', '2', '1 3', '2 3']
for idx, line in enumerate(infile_list):
    if '\n' in line:
        line = line.replace('\n', '')
        infile_list[idx] = line


infile_list     # ['1 3', '2 3', '1 1', '2 6', '1 5', '2 7', '2 5', '1 6']
count_switch = infile_list.pop(0)   # '8'
curr_switch_list = infile_list.pop(0).split() # ['0', '1', '0', '1', '0', '0', '0', '1']
count_student = infile_list.pop(0)  # '2'
sym_idx = 0     # 나누어지는 수
drainage = 1    # 나누는 수

# 스위치 변환 시작
for idx, line in enumerate(infile_list):
    value = int(line[-1])

    if line[0] == '1':  #스위치가 남자일때
        while drainage < len(curr_switch_list):
            if drainage % value == 0:  # drainage가 males_switch[male_cnt]의 배수이면,
                if curr_switch_list[drainage-1] == '0':  # 0을 1로, 1을 0으로
                    curr_switch_list[drainage-1] = '1'
                    drainage += 1
                else:
                    curr_switch_list[drainage-1] = '0'
                    drainage += 1
            drainage += 1
    else:
        # 여기부터 여자 스위치 대칭 변환
        while value-sym_idx > 0 and value+sym_idx < len(curr_switch_list):
            # 여기부터 if조건 변경필요
            if curr_switch_list[value-sym_idx-1] == '1' and curr_switch_list[value+sym_idx-1] == '1':
                curr_switch_list[value-sym_idx-1] = '0'
                curr_switch_list[value+sym_idx-1] = '0'
                sym_idx += 1
            elif curr_switch_list[value-sym_idx-1] == '0' and curr_switch_list[value+sym_idx-1] == '0':
                curr_switch_list[value-sym_idx-1] = '1'
                curr_switch_list[value+sym_idx-1] = '1'
                sym_idx += 1
            else:
                sym_idx += 1
                break
print(curr_switch_list)


count_switch = int(input())                 # 8
curr_switch_list = list(input().split(' ')) # ['0', '1', '0', '1', '0', '0', '0', '1']
count_student = int(input())                # 2
infile_list = []                            # ['1 3', '2 3', '1 1', '2 6', '1 5', '2 7', '2 5', '1 6']
sym_idx = 0
drainage = 1

for i in range(count_student):
    infile_list.append(input())

# 스위치 변환 시작
for idx, line in enumerate(infile_list):
    value = int(line[-1])

    if line[0] == '1':  #스위치가 남자일때
        while drainage < len(curr_switch_list):
            if drainage % value == 0:  # drainage가 males_switch[male_cnt]의 배수이면,
                if curr_switch_list[drainage-1] == '0':  # 0을 1로, 1을 0으로
                    curr_switch_list[drainage-1] = '1'
                    drainage += 1
                else:
                    curr_switch_list[drainage-1] = '0'
                    drainage += 1
            drainage += 1
    else:
        # 여기부터 여자 스위치 대칭 변환
        while value-sym_idx > 0 and value+sym_idx < len(curr_switch_list):
            # 여기부터 if조건 변경필요
            if curr_switch_list[value-sym_idx-1] == '1' and curr_switch_list[value+sym_idx-1] == '1':
                curr_switch_list[value-sym_idx-1] = '0'
                curr_switch_list[value+sym_idx-1] = '0'
                sym_idx += 1
            elif curr_switch_list[value-sym_idx-1] == '0' and curr_switch_list[value+sym_idx-1] == '0':
                curr_switch_list[value-sym_idx-1] = '1'
                curr_switch_list[value+sym_idx-1] = '1'
                sym_idx += 1
            else:
                sym_idx += 1
                break
print(curr_switch_list)
'''



