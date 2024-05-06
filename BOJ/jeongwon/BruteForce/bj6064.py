#  백준 6064 번 카잉달력

T = int(input())
for _ in range(T):
    m,n,x,y = map(int, input().split())

    i = x
    while True:
        if i > m*n:
            print(-1)
            break
        # i % n == y 가 안되는 이유 -> 초기값 x가 n보다 작으면서 y와 다르ㅁ
        if (i-y) %n == 0:
            print(i)
            break
        i += m