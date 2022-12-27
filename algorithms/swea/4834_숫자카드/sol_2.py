T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input()))
    counts = [0] * 10

    for card in cards:
        counts[card] += 1

    max_count = 0
    max_card = 0

    for card in range(10):
        if counts[card] >= max_count:
            max_count = counts[card]
            max_card = card


    print(f'#{tc} {max_card} {max_count}')









