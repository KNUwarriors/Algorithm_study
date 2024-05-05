# 백준 9252 LCS2

import sys
input = sys.stdin.readline

s1 = [""] + list(input().rstrip())
s2 = [""] + list(input().rstrip())
d = [[""]*len(s2) for _ in range(len(s1))]

for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            d[i][j] = d[i-1][j-1] + s1[i]
        else:
            if len(d[i-1][j]) >= len(d[i][j-1]):
                d[i][j] = d[i-1][j]
            else:
                d[i][j] = d[i][j-1]

# print문 두개 쓰면 시간 초과됨 ;
result = d[-1][-1]
print(len(result), result, sep="\n")