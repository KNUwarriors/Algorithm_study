N = int(input())
lst = []
stck = []
ans = []

for _ in range(N):
    temp = int(input())
    lst.append(temp)

i,j = 0,0
while True:
    if i > N or j >= N :
        break

    if len(stck) >0 and stck[len(stck)-1] == lst[j]:
        ans.append('-')
        j+=1
        stck.pop()
    else:
        i += 1
        stck.append(i)
        ans.append('+')

if len(stck) >0:
    print("NO")
else:
    for item in ans:
        print(item)