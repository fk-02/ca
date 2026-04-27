n = int(input())
e = int(input())
graph = [[] for _ in range(n)]
for _ in range(e):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
color = [-1] * n
for i in range(n):
    used = {color[j] for j in graph[i] if color[j] != -1}
    color[i] = next(x for x in range(n) if x not in used)
print(max(color) + 1)