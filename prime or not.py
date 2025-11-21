def prime(n):
    fc=0
    for i in range(1,n+1,1):
        if n%i==0:
            fc=fc+1
    if fc==2:
        return 1
    else:
        return 0
n=int(input())
res=prime(n)#function call
if res==1:
    print("prime")
else:
    print("not a prime")
            
