# 백준 14002 가장 긴 증가하는 부분 수열4

N = int(input())
A = list(map(int, input().split()))
D = [1] * N

ans = []

for i in range(1,N):
    for j in range(i):
        if A[i] > A[j] and D[i] < D[j] + 1:
            D[i] = D[j] + 1

num = max(D)
print(num)

for i in range(N-1, -1, -1):
    if D[i] == num:
        ans.append(A[i])
        num-=1

ans.reverse()
print(*ans)
