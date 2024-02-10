# 백준 9613 gcd의 합

def gcd(a, b):
    if b == 0:
        return a
    r = a % b
    return gcd(b,r)


T = int(input())
ans = []
for _ in range(T):
    lst = list(map(int, input().split()))
    cnt=0
    n = lst[0]
    for i in range(1, n):
        for j in range(i+1, n+1):
            cnt+= gcd(lst[i], lst[j])
    ans.append(cnt)

for item in ans:
    print(item)