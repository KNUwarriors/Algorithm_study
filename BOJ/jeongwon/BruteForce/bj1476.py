#백준 1476 날짜계산

E,S, M =map(int, input().split())
ans = 1

e=s=m = 1

while True:
    if E ==e and S == s and M ==m:
        break
    ans+=1
    e+=1
    s+=1
    m+=1
    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1

print(ans)