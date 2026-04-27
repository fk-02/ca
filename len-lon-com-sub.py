a,b=input(),input()
print(max((len(x) for i in range(len(a)) for j in range(i+1,len(a)+1) if (x:=a[i:j]) in b),default=0))