# 백준 15654 n과m 4

visited = [False] * 10001
n = m = 0
s = []

def dfs(cnt, lst):
    if cnt == m:
        print(*s)
        return

    for item in lst:
        if visited[item]:
            continue
        s.append(item)
        visited[item] = True
        dfs(cnt+1, lst)

        s.pop()
        visited[item] = False


n,m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
dfs(0, lst)