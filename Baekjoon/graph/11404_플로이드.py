import sys
input = sys.stdin.readline

n, m = int(input()), int(input())
graph = [[100001] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i != j:
                graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

for g in graph[1:]:
    print(' '.join(list(map(str, g[1:]))).replace('100001', '0'))