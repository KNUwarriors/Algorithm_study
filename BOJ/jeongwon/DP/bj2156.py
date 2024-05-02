# 백준 2156 포도주 시식
import sys

n = int(input())
d = [0] * (n+1)
wine = [0]*(n+1)
for i in range(1,n+1):
    wine[i] = int(input())

d[1] = wine[1]
d[2] = wine[1]+wine[2]

for i in range(3, n+1):
    d[i] = d[i-1]
    if (d[i] < d[i-2] + wine[i]):
        d[i] = d[i-2] + wine[i]
    if (d[i] < d[i-3] + wine[i] + wine[i-1]):
        d[i] = d[i-3] + wine[i] + wine[i-1]
print(d[n])
