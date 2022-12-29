def solution(text, anagram, sw):
    new_list = [None] * len(anagram)
    if sw == True:
        for true_idx in range(len(text)):
            new_list[anagram[true_idx]] = text[true_idx]
    elif sw == False:
        for false_idx in range(len(text)):
            new_list[false_idx] = text[anagram[false_idx]]
    new_str = ''.join(new_list)
    return new_str

print(solution('Hello', [4, 2, 0, 1, 3], True))  # 'lleoH'
print(solution('lleoH', [4, 2, 0, 1, 3], False))  # 'Hello'