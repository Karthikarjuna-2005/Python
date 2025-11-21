def prime(n):
    if n==1:
        return 0
    for i in range(2,n,1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
t=n
n=n-1
while True:
    if(prime(n)):
        beforeprime=n
        break
    n=n-1
n=t
n=n+1
while True:
    if(prime(n)):
        nextprime=n
        break
    n=n+1
n=t
if nextprime-n==n-beforeprime:
    print(beforeprime,nextprime)
elif nextprime-n>n-beforeprime:
    print(beforeprime)
else:
    print(nextprime)


    
