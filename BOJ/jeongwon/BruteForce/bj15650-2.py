# # 백준 15650 2**n 복잡도로 하는 법
#
# n = m = 0
# s = [0]*10
#
# def dfs(selected, idx):
#     if selected == m:
#         for item in s:
#             if item >0:
#                 print(item, end=' ')
#         print()
#         return
#
#     if idx > n:
#         return
#
#     s[selected] = idx
#     dfs(selected+1, idx+1)
#     s[selected] = 0
#     dfs(selected, idx+1)
# n,m = map(int, input().split())
# dfs(0,1)

n = m = 0
s = []

def dfs(cnt, idx):
    if cnt == m:
        print(*s)
        return
    if idx > n:
        return

    s.append(idx)
    dfs(cnt+1, idx+1)
    s.pop()
    dfs(cnt, idx+1)

n,m = map(int, input().split())
dfs(0,1)