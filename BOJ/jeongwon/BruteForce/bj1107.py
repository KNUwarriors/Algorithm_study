# 백준 1107 리모컨

c = int(input())
n = int(input())
broken=[]
#고장난 버튼이 있을 때만 입력받아야함
if n != 0:
    broken = list(map(str, input().split()))

ans = abs(c-100)

for i in range(1000001):
    num = str(i)
    for item in num:
        if item in broken:
            break
    else:
        ans = min(ans, len(num) + abs(i-int(c)))
print(ans)