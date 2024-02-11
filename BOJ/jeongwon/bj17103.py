# 백준 17103번 골드바흐 파티션
check = [0] * 1000001
check[1] = 1
prime = []

for i in range(2, 1000001):
    if check[i] == 0:
        prime.append(i)
        j = i * i
        while j <1000001:
            check[j]= 1
            j+=i

N = int(input())
for _ in range(N):
    num = int(input())
    bound = 1000001
    ans=0

    for item in prime:
        if item >= num or item >= bound:
            break
        if check[num - item] == 0:
            bound = num-item
            ans+=1

    print(ans)