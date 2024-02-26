# 백준 1912번 연속합

N = int(input())
A = list(map(int, input().split()))
D = [0] * N
D[0] = A[0]

for i in range(1, N):
    if A[i] >= D[i-1] + A[i]:
        D[i] = A[i]
    else:
        D[i] = D[i-1] + A[i]

print(max(D))