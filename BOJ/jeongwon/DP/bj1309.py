# 백준 1309번 동물원

d = [[0 for _ in range(3)] for _ in range(100000)]

n= int(input())
d[0][0], d[0][1], d[0][2] = 1, 1, 1
for i in range(1,n):
    d[i][0] = (d[i - 1][0] + d[i - 1][1] + d[i - 1][2]) % 9901
    d[i][1] = (d[i - 1][0] + d[i - 1][2]) % 9901
    d[i][2] = (d[i - 1][0] + d[i - 1][1]) % 9901

print(sum(d[n-1])%9901)
