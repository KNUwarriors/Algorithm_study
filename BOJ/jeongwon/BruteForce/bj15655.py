# 백준 15655  N과 M6

n = m = 0
s = []

def dfs(cnt, idx, lst):
    if cnt == m:
        print(*s)
        return

    if idx >=n:
        return

    s.append(lst[idx])
    dfs(cnt+1, idx+1, lst)
    s.pop()
    dfs(cnt, idx+1,lst)

n,m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
dfs(0,0,lst)