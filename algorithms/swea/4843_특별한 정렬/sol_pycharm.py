T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers_list = list(map(int, input().split()))
    numbers_list.sort()

    # numbers_list를 큰 리스트, 작은 리스트로 나눔
    for idx, number in enumerate(numbers_list):
        lower_list = numbers_list[:int(len(numbers_list)/2)]
        upper_list = numbers_list[int(len(numbers_list)/2):]
        upper_list.reverse()
        if len(lower_list) + len(upper_list) >= 10:
            break
            
    new_sorted_list = []
    new_idx = 0

    # 
    for idx in range(len(numbers_list)):
        if len(new_sorted_list) >= 10:
            break
        if idx % 2 == 0:
            new_sorted_list.append(upper_list[new_idx])
        else:
            new_sorted_list.append(lower_list[new_idx])
            new_idx += 1
    new_sorted_list = list(map(str, new_sorted_list))
    new_sorted_str = ' '.join(new_sorted_list)
    print(f'#{tc} {new_sorted_str}')