import sys
input=sys.stdin.readline
n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
temp=[1 for _ in range(n)]

for i in range(n):
    if i==0:
        temp[i]=1
        continue
    for j in range(i):
        if arr[i]>arr[j]:
            if temp[j]+1>temp[i]:
                temp[i]=temp[j]+1

    
print(n-max(temp))
