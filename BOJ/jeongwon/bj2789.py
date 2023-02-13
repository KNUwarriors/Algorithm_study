#문제: 백준 2798번 블랙잭, https://www.acmicpc.net/problem/2798

N,M = map(int, input().split())
arr1 = list(map(int, input().split()))
result = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if arr1[i] + arr1[j] + arr1[k] > M:
                continue
            else:
                result = max(result, arr1[i]+arr1[j]+arr1[k])

print(result)



