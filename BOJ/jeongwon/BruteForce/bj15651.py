#백주 15651 n과m3

s = []
n = m = 0

def dfs():
    if len(s) == m:
        print(*s)
        return
    for i in range(n):
        s.append(i+1)
        dfs()
        s.pop()

n,m = map(int, input().split())
dfs()