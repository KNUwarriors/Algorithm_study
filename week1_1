import sys


n = int(input())

paper = []
for i in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

min = 0
zer = 0
plu = 0


def func(row, col, num):
    global min
    global zer
    global plu
    k = paper[row][col]
    for i in range(row, row+num):
        for j in range(col, col+num):
            if paper[i][j] != k:
                func(row, col, num//3)
                func(row, col+num//3, num//3)
                func(row, col+num//3+num//3, num//3)

                func(row+num//3, col, num//3)
                func(row+num//3, col+num//3, num//3)
                func(row+num//3, col+num//3+num//3, num//3)

                func(row+num//3+num//3, col, num//3)
                func(row+num//3+num//3, col+num//3, num//3)
                func(row+num//3+num//3, col+num//3+num//3, num//3)
                return
    if k == -1:
        min+=1
    elif k == 0:
        zer+=1
    elif k == 1:
        plu+=1


min = 0
zer = 0
plu = 0
func(0, 0, n)
print(min)
print(zer)
print(plu)
