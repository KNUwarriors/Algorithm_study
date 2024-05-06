# 백준 3085번 사탕게임

def check(a):
    ans =cnt =  1
    #행 마다 최댓값 구하기
    for i in range(len(a)):
        cnt = 1
        for j in range(1, len(a)):
            if a[j][i] == a[j-1][i]:
                cnt+= 1
                ans = max(ans, cnt)
            else:
                cnt = 1
    cnt = 1
    #열 마다 최댓값 구하기
    for i in range(len(a)):
        cnt = 1
        for j in range(1,len(a)):
            if a[i][j] == a[i][j-1]:
                cnt+=1
                ans = max(ans, cnt)
            else:
                cnt = 1
    return ans

n = int(input())
a = []
ans = -1
for i in range(n):
    a.append(list(input()))
#오른쪽과 비교, 아래와 비교
for i in range(n):
    for j in range(n):
        if i < (n-1):
            a[i+1][j], a[i][j] = a[i][j], a[i+1][j]
            ans = max(ans, check(a))
            a[i + 1][j], a[i][j] = a[i][j], a[i + 1][j]
        if j < (n-1):
            a[i][j], a[i][j+1] = a[i][j+1], a[i][j]
            ans = max(ans, check(a))
            a[i][j], a[i][j + 1] = a[i][j + 1], a[i][j]

print(ans)

