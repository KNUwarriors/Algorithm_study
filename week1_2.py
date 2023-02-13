n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int,input())))

def compress(x,y,size):
    val=arr[x][y]
    flag=0
    for i in range(x,x+size):
        for j in range(y,y+size):
            if arr[i][j]!=val:
                flag=1
    if flag==1:
        print("(",end="")
        compress(x,y,size//2)
        compress(x,y+(size//2),size//2)
        compress(x+(size//2),y,size//2)
        compress(x+(size//2),y+(size//2),size//2)
        print(")",end="")
    else:
        print(val,end="")

compress(0,0,n)
