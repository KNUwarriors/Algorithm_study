# 백준 9251 LCS
# 해설 https://velog.io/@piopiop/%EB%B0%B1%EC%A4%80-9251-LCS-%ED%8C%8C%EC%9D%B4%EC%8D%AC

s1 = ' '+input()
s2 = ' '+input()
d = [[0 for _ in range(len(s2))] for _ in range(len(s1))]

for i in range(1, len(s1)):
    for j in range(1, len(s2)):
        if s1[i] == s2[j]:
            d[i][j] = d[i-1][j-1]+1
        else:
            d[i][j] = max(d[i-1][j], d[i][j-1])


print(d[-1][-1])