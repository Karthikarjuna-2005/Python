print("*"*50)
print("\tArithmetic Operators")
print("*"*50)
print("\t1.Addition")
print("\t2.subtraction")
print("\t3.multiplication")
print("\t4.division")
print("\t5.floor division")
print("\t6.modulo division")
print("\t7.power")
print("*"*50)
choice=int(input())
match(choice):
     case 1:
         print("enter the two values")
         a,b=map(int,input().split())
         c=a+b
         print(c)
     case 2:
         print("enter the two values")
         a,b=map(int,input().split())
         c=a-b
         print(c)
     case 3:
         print("enter the two values")
         a,b=map(int,input().split())
         c=a*b
         print(c)
     case 4:
         print("enter the two values")
         a,b=map(int,input().split())
         c=a/b
         print(c)
     case 5:
         print("enter the two values")
         a,b=map(int,input().split())
         c=a//b
         print(c)
     case 6:
         print("enter the two values")
         a,b=map(int,input().split())
         c=a%b
         print(c)
     case 7:
         print("enter the two values")
         a,b=map(int,input().split())
         c=a**b
         print(c)
     case _:
         print("enter valid choice")
         
