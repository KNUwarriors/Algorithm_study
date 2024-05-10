# 백준 15656 N과 M (7)

n = m = 0
s = []

def dfs(cnt, lst):
    if cnt == m:
        print(*s)
        return

    for item in lst:
        s.append(item)
        dfs(cnt+1, lst)
        s.pop()

n,m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
dfs(0, lst)

