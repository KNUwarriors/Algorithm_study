# 백준 17299번 오등큰수

cnt = [0]* 1000001
stck = []

N = int(input())
s = list(map(int, input().split()))
ans = [-1] * N

for item in s:
    cnt[item]+=1

for i in range(N):
    while stck and cnt[s[stck[-1]]]<cnt[s[i]]:
        ans[stck.pop()] = s[i]
    stck.append(i)


print(str(ans).replace('[', '').replace(']', '').replace(',', ''))