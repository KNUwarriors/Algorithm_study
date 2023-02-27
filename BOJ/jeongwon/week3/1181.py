# 백준 1181번 단어 정렬

n = int(input())
list = []

for i in range(n):
    list.append(input())

list.sort()
list.sort(key = len)

for i in list:
    print(i)
