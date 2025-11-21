import math
n=int(input())
dc=0
t=n
while t:
    r=n%10
    dc=dc+1
    t=t//10
#print(dc)
    sum=0
    t=n
while n>0:
    r=n%10
    sum=sum+int(math.pow(r,dc))
    n=n//10
if t==sum:
    print("arm")
else:
    print("not arm")
      
