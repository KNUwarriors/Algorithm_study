# 백준 15652 n과m4

m = n = 0
s = []
def dfs(cnt, idx):
    if cnt == m:
        print(*s)
        return

    for i in range(idx, n+1):
        s.append(i)
        dfs(cnt+1, i)
        s.pop()

n,m = map(int, input().split())
dfs(0, 1)

