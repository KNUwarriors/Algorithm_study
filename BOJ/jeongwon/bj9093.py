# 백준 9093 - 단어 뒤집기

T = int(input())
stck= []


def pop_all(ans):
    while(stck):
        ans.append(stck.pop())


for _ in range(T):
    sentence = input()
    ans = []
    for i, item in enumerate(sentence):
        if item == ' ' and len(stck) >0:
            pop_all(ans)
            ans.append(' ')
        elif item != ' ' and i == len(sentence)-1:
            stck.append(item)
            pop_all(ans)
        else:
            stck.append(item)

    ans = ''.join(ans)
    print(ans)
