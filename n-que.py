from itertools import permutations
n = int(input())
ok = 0
for p in permutations(range(n)):
    if all(abs(p[i]-p[j]) != abs(i-j) for i in range(n) for j in range(i)):
        print(*p)
        ok = 1
if not ok:
    print(-1)