n=int(input())
g=[list(map(int,input().split())) for _ in range(n)]
ans=[]
def f(i,j,v,p):
    if i==j==n-1: ans.append(p); return
    v.add((i,j))
    for di,dj,c in [(1,0,'D'),(0,-1,'L'),(0,1,'R'),(-1,0,'U')]:
        ni,nj=i+di,j+dj
        if 0<=ni<n and 0<=nj<n and g[ni][nj] and (ni,nj) not in v:
            f(ni,nj,v,p+c)
    v.remove((i,j))
if g[0][0]:
    f(0,0,set(),"")
    print(-1 if not ans else " ".join(sorted(ans)))
else:
    print(-1)