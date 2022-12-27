from collections import Counter

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input()))
    new_numbers = Counter(numbers)
    max_value = max(new_numbers.values())
    value_list = sorted(new_numbers.values())
    max_key = [key for key, value in new_numbers.items() if value_list[-1] == value]
    print(f'#{tc} {max_key[0]} {max_value}')









