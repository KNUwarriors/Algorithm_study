# 백준 6588번 골드바흐의 추측
import sys

check = [0] * 1000001
check[1]=1
prime = []

for i in range(2, 1000001):
    if check[i] == 0:
        prime.append(i)
        j = i*i
        while j <= 1000000:
            check[j] = 1
            j+=i

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    else:
        for item in prime:
            if check[n-item] == 0:
                print(f'{n} = {item} + {n-item}')
                break

            elif item >= n:
                print("Goldbach's conjecture is wrong.")
                break
