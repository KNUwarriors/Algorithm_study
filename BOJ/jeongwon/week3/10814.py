# 백준 10814 나이순 정렬

n = int(input())
list = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    list.append((age, name))

list.sort(key = lambda x : x[0])

for i in list:
    print(i[0], i[1])
