# 백준 1748번 수 이어쓰기 1

n = int(input())

i = j =1
ans =0
while i <= n:
    end = i*10 -1
    end = min(end, n)
    ans+= (end-i+1)*j
    i*=10
    j+=1

print(ans)