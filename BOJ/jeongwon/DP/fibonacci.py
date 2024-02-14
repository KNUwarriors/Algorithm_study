# 피보나치 수열 top-down과 bottom up 방식 으로 각각 구현, py는 bottom up 방식이 좀 더 좋다..왜? top-down하면 스택을 쓰기때문에 재귀함수에서 스택 오버플로우가 가끔 난다.

top_memo = [0]* 101
btm_memo = [0] * 101

# Top-Down 방식 (재귀)
def fib1(n):
    if n <=1:
        return n
    if top_memo[n] > 0:
        return top_memo[n]

    top_memo[n]= fib1(n-1) + fib1(n-2)
    return top_memo[n]

#Bottom-Up 방식 (반복문)
def fib2(n):
    if n <=1:
        return n

    btm_memo[0] = 0
    btm_memo[1] = 1

    for i in range(2, n+1):
        btm_memo[i] = btm_memo[i-1] + btm_memo[i-2]

    return btm_memo[n]

print(fib1(7))
print(fib2(7))