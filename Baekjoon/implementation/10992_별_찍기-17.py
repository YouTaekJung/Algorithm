n = int(input())

print(' ' * (n - 1) + '*')
for i in range(2, n + 1):
    if i == n:
        print(' ' * (n - i) + '*' * (2 * i - 1))
    else:
        print(' ' * (n - i) + '*' + ' ' * (2 * i - 3) + '*')