# 백준 2309번 일곱난쟁이

lst = []
sum = 0
for _ in range(9):
    lst.append(int(input()))
lst.sort()

for item in lst:
    sum+=item

for i in range(8):
    for j in range(i, 9):
        if sum - (lst[i]+lst[j]) == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                print(lst[k])
            exit()