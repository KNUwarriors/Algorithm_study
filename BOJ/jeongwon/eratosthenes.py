#에라토스테네스의 체: (1~N) 사이의 소수 개수?
N = 130
cnt = 0

#0이면 소수 1이면 소수아님
check = [0] * (N+1)

prime = []

for i in range(1, N+1):
    if i<2:
        check[i] = 1
        continue
    if check[i] == 0:
        cnt+=1
        prime.append(i)

        j = i*i
        while j <= N:
            check[j] = 1
            j+=i

print(prime)
print(len(prime))
print(cnt)