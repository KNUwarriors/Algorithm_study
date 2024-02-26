# 백준 1699번 제곱수의 합

N = int(input())
D = [0] * (N+1)
D[1] = 1

for i in range(2, N+1):
    D[i] = i
    j = 1
    while i >= j*j:
        if D[i] > D[i - (j*j)] + 1:
            D[i] = D[i - (j*j)] +1
        j+=1

print(D[N])