#%%
# import os
# os.getcwd()



#%%
import sys
sys.stdin = open('sample_input.txt')

T = int(input())

for tc in range(1, T+1):
    sticks = input()
    sticks = sticks.replace('()', '*')
    
    total = bar = 0

    for char in sticks:
        if char == '(':
            bar += 1
        elif char == ')':
            bar -= 1
            total += 1
        else:
            total += bar

    print(f'#{tc} {total}')



#%%

infile = list(open('sample_input.txt', 'r'))

infile = list(map(lambda x: x.replace('\n', ''), infile))
# 혹은
# for idx, line in enumerate(infile):
#     line = line.replace('\n', '')
#     infile[idx] = line

T = int(infile[0])

for tc in range(1, T+1):
    sticks = infile[tc]
    sticks = sticks.replace('()', '*')
    print(sticks)

    total = bar = 0

    for char in sticks:
        if char == '(':
            bar += 1
        elif char == ')':
            bar -= 1
            total += 1
        else:
            total += bar

    print(f'#{tc} {total}')







