# def average(a = 5, b = 7):
#     print("The aveerage is ", (a+b)/2)

# average()
# average(5,5)
# average(7)

# keyword arguments****************************************
# average(b = 10, a = 12) # dont have issue of oder

# As Tuple*************************************************
def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum + i
    return sum/ len(numbers)



c = average(1,2,3,4,5,6,7,8,9,10)
print(c)
# average(1)

# As Dict******************************************************

def name(**name):
    print(type(name))
    print("Hello",name["fname"],name["lname"],name["mname"])

# name(mname = "Tejash",lname = "Pavthawala",fname = "Dev")