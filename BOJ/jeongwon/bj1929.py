# 백준 1929번 소수 구하기
import sys

M, N = map(int, sys.stdin.readline().split())

check = [0] * (N+1)
prime = []

for i in range(2, N+1):
    if check[i] == 0:
        if  i >= M:
            prime.append(i)

        j = i*i
        while(j <=N):
            check[j] = 1
            j+=i

for item in prime:
    print(item)