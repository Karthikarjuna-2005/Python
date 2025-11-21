def prime(n):
    if n==1:
     return 0
    for i in range(2,n,1):
        if n%i==0:
            return 0
    else:
        return 1
a,b=map(int,input().split())
c=0  #count
for i in range(a,b+1,1):
    if(prime(i)):
        c=c+1
        print(i,end=" ")
print()
print(c)
