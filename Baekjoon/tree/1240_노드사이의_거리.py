from collections import deque
n, m = map(int, input().split())
tree = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(n - 1):
    x, y, d = map(int, input().split())
    tree[x][y] = d
    tree[y][x] = d

def bfs(start, end):
    q = deque([[start, 0]])
    check = [0] * (n + 1)
    while q:
        s, d = q.popleft()
        if s == end:
            return d
        for i in range(1, n + 1):
            if tree[s][i] != 0 and check[i] == 0:
                check[i] = 1
                q.append([i, d + tree[s][i]])

for _ in range(m):
    s, e = map(int, input().split())
    print(bfs(s, e))