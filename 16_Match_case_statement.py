x = int(input("Enter the number:"))

match x:
    case 0:
        print("x is zero")
    case 45:
        print("x is 45")
        
    case _ if(x!=90):
        print("X is not 90")
    case _ :
        print(x)
    