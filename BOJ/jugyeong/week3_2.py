import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
temp=[1 for _ in range(n)]
get=[[] for _ in range(n)]
for i in range(n):
    flag=0
    if i==0:
        temp[i]=1
        get[i].append(arr[i])
        continue
    for j in range(i):
        if arr[i]>arr[j]:
            if temp[j]+1>temp[i]:
                temp[i]=temp[j]+1
                get[i]=get[j]+[arr[i]]
            flag=1
    if flag==0:
        get[i].append(arr[i])
val,idx=-1,-1
for i in range(n):
    if val<temp[i]:
        val=temp[i]
        idx=i
print(val)
print(*get[idx])
