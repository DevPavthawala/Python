# Srings are immutable means i dont change the varibale
a = 'Dev!!! pavthawala'
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip('!'))
print(a.replace("Dev", "Pavthawala"))
print(a.split(" "))

Heading = "intro tO code" # convert 1st to upper and other to lower case
print(Heading.capitalize())

str = "Welcome to the console!!!"
print(len(str))
print(len(str.center(30)))
print(str.endswith("!")) # output in boolean

print(str.endswith("to", 4,10)) # used string sclicing

name = "He's is Dev. He is an honest man."
print(name.find("is"))
print(name.isspace())

name = "Heisdev"
print(name.isalnum())

name = "Heisdev00 " 
print(name.isalnum())

name = "qwertyuiop " 
print(name.islower())
print(name.isprintable())

name = "qwertyuiop\n" 
print(name.isprintable())
