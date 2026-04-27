n,m=map(int,input().split())
a=[list(map(int,input().split()))for _ in range(n)]
d=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
for i in range(n):
    for j in range(m):
        c=0
        for dx,dy in d:
            x,y=i+dx,j+dy
            while 0<=x<n and 0<=y<m:
                if a[x][y]:c+=1;break
                x+=dx;y+=dy
        print(c,end=" ")
    print()