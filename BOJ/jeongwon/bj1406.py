import sys

left = list(input())
right = []

N = int(input())

for _ in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'L' and len(left) >0:
        right.append(left.pop())
    elif cmd[0] == 'D' and len(right) >0:
        left.append(right.pop())
    elif cmd[0] == 'B' and len(left) >0:
        left.pop()
    elif cmd[0] == 'P':
        # CMD = P $
        left.append(cmd[1])

right.reverse()
ans = ''.join(left+right)
# ans = ans.join(right)
print(ans)