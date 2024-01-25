T = int(input())

for _ in range(T):
    lst = list(input())
    stck =[]
    flag = 1
    for item in (lst):
        if item == '(':
            stck.append(item)
        else:
            if len(stck) > 0:
                stck.pop()
            else:
                flag = 0
                break
    if len(stck) > 0 or flag == 0:
        print("NO")
    else:
        print("YES")