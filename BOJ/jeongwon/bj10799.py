#백준 10799번 쇠막대기

s = list(input())
stck = []
ans = 0
flag = 0

for i in range(len(s)-1):
    if s[i] == "(":
        if s[i+1] != ")":
            stck.append(1)
            ans += 1
        else:
            flag =1
    else:
        if flag == 1:
            flag = 0
            ans+= len(stck)
        else:
            stck.pop()

print(ans)