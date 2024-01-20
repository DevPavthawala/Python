a=input("enter a number")
b=input("enter a number")

try:
    z = a/int(b)
except ZeroDivisionError as e:
    print("zero division error occured")
    z = None

except TypeError as e:
    print("Type Error occured")
    z = None

print("divison is ",z)
