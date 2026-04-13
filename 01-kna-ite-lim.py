from itertools import combinations as c
n,W,k=map(int,input().split());a=[tuple(map(int,input().split()))for _ in range(n)]
print(max([sum(v for w,v in x)for i in range(1,k+1)for x in c(a,i)if sum(w for w,_ in x)<=W]+[0]))