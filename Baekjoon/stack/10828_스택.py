import sys
n = int(sys.stdin.readline())

stack = []
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0] == 'push':
        stack.append(command[1])
    elif command[0] == 'pop':
        print(-1 if len(stack) == 0 else stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        print(1 if len(stack) == 0 else 0)
    else:
        print(-1 if len(stack) == 0 else stack[-1])