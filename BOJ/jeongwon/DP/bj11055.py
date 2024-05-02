# 백준 11055 가장 큰 증가하는 부분 수열

n = int(input())
a = list(map(int, input().split()))
d = [0] * n
d[0] = a[0]

# max 값이라고 0, -1 이딴걸로 초기화 해두면 틀림! a[0] 포문에 안넣었으니까 max값에 넣어주자 제발
max_sum = a[0]

for i in range(1, n):
    d[i] = a[i]
    for j in range(0, i):
        if a[j] < a[i] and d[j]+a[i] > d[i]:
            d[i] = d[j] + a[i]

    max_sum = max(max_sum, d[i])
print(max_sum)