N = int(input())
A = list(map(int, input().split()))

D = [1] * N
ans = 1

for i in range(1,N):
    for j in range(0, i):
        if A[i] > A[j] and D[i] < D[j] + 1:
            D[i] = D[j] + 1

print(max(D))