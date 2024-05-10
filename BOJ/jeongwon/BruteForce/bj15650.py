# 백준 15650 n과m2

n=m=0

s = []

def dfs(start):
    if len(s) == m:
        print(*s)
        return
    for i in range(start, n):

        s.append(i+1)

        dfs(i+1)
        s.pop()

n, m = map(int, input().split())
dfs(0)