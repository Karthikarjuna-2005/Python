name=input()
s1=int(input("enter subject 1 marks\n"))
s2=int(input("enter subject 2 marks\n"))
s3=int(input("enter subject 3 marks\n"))
per=(s1+s2+s3)/3
if per>=40:
  if s1>40 and s2>40 and s3>40:
      print("pass")
  else:
     print("fail")
else:
 print("fail")
