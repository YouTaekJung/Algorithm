import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
li = [int(input()) for _ in range(n)]
tree = [0] * 4 * n

def init(start, end, index):
    if start == end:
        tree[index] = li[start]
        return tree[index]
    mid = (start + end) // 2
    tree[index] = (init(start, mid, index * 2) * init(mid + 1, end, index * 2 + 1)) % 1000000007
    return tree[index]

def interval_prod(start, end, index, left, right):
    if left > end or right < start:
        return 1
    if left <= start and right >= end:
        return tree[index]
    mid = (start + end) // 2
    return interval_prod(start, mid, index * 2, left, right) * interval_prod(mid + 1, end, index * 2 + 1, left, right) % 1000000007

def update(start, end, index, what, value):
    if what < start or what > end:
        return
    if start == end:
        tree[index] = value
        return
    mid = (start + end) // 2
    update(start, mid, index * 2, what, value)
    update(mid + 1, end, index * 2 + 1, what, value)
    tree[index] = tree[index * 2] * tree[index * 2 + 1] % 1000000007

init(0, n - 1, 1)
for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        update(0, n - 1, 1, b - 1, c)
        li[b - 1] = c
    else:
        print(int(interval_prod(0, n - 1, 1, b - 1, c - 1)))
