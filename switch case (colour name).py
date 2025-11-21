print("*"*50)
print("colour name")
print("\tV ->violet")
print("\tI ->indigo")
print("\tB ->blue")
print("\tG ->green")
print("\tY ->yellow")
print("\tO ->orange")
print("\tR ->red")
print("*"*50)
choice=int(input())
match(choice):
    case 'V':
        print("V->violet")
    case 'I':
        print("I->indigo")
    case 'B':
        print("B->blue")
    case 'G':
        print("G->green")
    case 'Y':
        print("Y->yellow")
    case 'O':
        print("O->orange")
    case 'R':
        print("R->red")
    case _:
        print("invalid colour")
