# 백준 15649 n과m 1

s = []
def dfs(n,m, visited):
    if len(s) == m:
        print(*s)
    for i in range(n):
        if visited[i]:
            continue
        s.append(i+1)
        visited[i] = True
        dfs(n,m, visited)
        s.pop()
        visited[i] = False




n,m = map(int,input().split())
visited = [False] * (n)
dfs(n,m,visited)

