# 백준 17404 rgb2
import sys
INF = 1000*1000+1
n = int(sys.stdin.readline().rstrip())
rgb = []
for _ in range(n):
    rgb.append(list(map(int, sys.stdin.readline().rstrip().split())))

ans = INF

for i in range(3):
    d = [[-1]*3 for _ in range(n)]
    d[0][0] = d[0][1] = d[0][2] = INF
    d[0][i] = rgb[0][i]

    for j in range(1, n):
        d[j][0] =min(d[j-1][1], d[j-1][2]) + rgb[j][0]
        d[j][1] = min(d[j-1][0], d[j-1][2])+ rgb[j][1]
        d[j][2] = min(d[j-1][0], d[j-1][1])+ rgb[j][2]

    d[n-1][i] = INF
    ans = min(ans, min(d[n-1]))


print(ans)