import sys
input = sys.stdin.readline
n = int(input())
li = list(map(int, input().split()))
sorted_li = sorted(list(set(li)))
dic = {sorted_li[i] : i for i in range(len(sorted_li))}
for i in li:
    print(dic[i], end = ' ')