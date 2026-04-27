from itertools import permutations
n=int(input());g=[list(map(int,input().split()))for _ in range(n)]
m=10**9;p=[]
for x in permutations(range(1,n)):
    c=g[0][x[0]]+sum(g[x[i]][x[i+1]] for i in range(n-2))+g[x[-1]][0]
    if c<m:m,p=c,[0]+list(x)+[0]
print(m);print(*p,end=" ")