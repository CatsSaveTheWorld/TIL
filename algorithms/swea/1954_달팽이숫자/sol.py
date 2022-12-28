#%%
import os

os.chdir('../1954_달팽이숫자')
os.getcwd()     # 'c:\\Users\\4ser\\Documents\\TIL\\algorithms\\swea\\1954_달팽이숫자'

#%%
import sys

sys.stdin = open('input.txt')

T = int(input())

print(T)

for tc in range(1 + T+1):
    N = int(input())
    print(N)
#%%






