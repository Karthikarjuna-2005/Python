def fact(t): #t=5
    f=1
    for i in range(1,t+1,1):
        f=f*i
    return f
n=int(input())
print(fact(n))
    
