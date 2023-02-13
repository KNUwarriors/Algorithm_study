# 백준 2331번 분해합


N= int(input())
test = 0

for i in range(1, N+1):
    a = list(map(int, str(i)))
    test = i + sum(a)
    if test == N:
        print(i)
        break

    elif i == N:
        print(0)
