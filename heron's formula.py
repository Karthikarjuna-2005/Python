import math
a=int(input("enter the value"))
b=int(input("enter the value"))
c=int(input("enter the value"))
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print('Area of {} and {} and {} is::{}'.format(a,b,c,area))      
