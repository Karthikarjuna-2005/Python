price=int(input("enter price:\n"))#100
quantity=int(input("enter quantity:\n"))#90
cost=price*quantity#90*100=900
if quantity>=100:
    cost=cost-(price*quantity*(10/100))
    print(cost)   
