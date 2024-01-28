# 백준 17413 단어뒤집기2

lst = list(input())
flag = 0
stck =[]
for item in lst:
    if item == "<":
        while (stck):
            print(stck.pop(), end="")
        flag = 1
        print("<", end = "")
    elif item == ">":
        flag = 0
        print(">", end = "")
    elif flag == 1:
        print(item, end = "")
    elif item == " ":
        while(stck):
            print(stck.pop(), end="")
        print(" ", end="")
    else:
        stck.append(item)
    #
while (stck):
    print(stck.pop(), end="")