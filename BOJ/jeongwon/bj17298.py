# 백준 17298번 오큰수
N = int(input())
s = list(map(int, input().split()))
ans = [-1] * N
stck = []

for i in range(N):
    while stck and s[stck[-1]] < s[i]:
        ans[stck.pop()] = s[i]
    stck.append(i)

print(ans)