from collections import defaultdict
n=int(input())
arr=[[0 for i in range(n)] for i in range(n)]
dic=defaultdict(int)
for i in range(n):
    arr[i]=list(map(int,input().split()))
def func(sr,sc,size):
    ans=arr[sr][sc]
    flag=0
    for i in range(sr,sr+size):
        for j in range(sc,sc+size):
            if arr[i][j]!=ans:
                flag=1
                break
    if flag==1:
        func(sr,sc,size//3)
        func(sr,sc+(size//3),size//3)
        func(sr,sc+(size//3)*2,size//3)
        func(sr+(size//3),sc,size//3)
        func(sr+(size//3),sc+(size//3),size//3)
        func(sr+(size//3),sc+(size//3)*2,size//3)
        func(sr+(size//3)*2,sc,size//3)
        func(sr+(size//3)*2,sc+(size//3),size//3)
        func(sr+(size//3)*2,sc+(size//3)*2,size//3)
    if flag==0:
        dic[ans]+=1

func(0,0,n)
print(dic[-1])
print(dic[0])
print(dic[1])
