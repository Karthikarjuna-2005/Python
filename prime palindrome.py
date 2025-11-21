def palindrome(t=n):
    rev=0
    while n>0:
        r=n%10
        r=rev*10+r
        n=n//10
    if rev==t:
        return 1
    else:
        return 0
def prime(n):
    if n==1:
        return 0
    for i in range(2,n,1):
        if n%i==0:
            return 0
    else:
        return 1
n=int(input())
if(prime(n) and palindrome(n)):
    print(" prime palindrome")
else:
    print("not a prime palindrome")
