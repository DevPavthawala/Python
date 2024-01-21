user = int(input("Enter your sugar leval :"))

if user>=80 and user<=100:
    print(f"the sugar leval {user} is normal")
elif user>=101:
    print(f"the sugar leval {user} is more than normal")
elif user<=79:
    print(f"the sugar leval {user} is less than normal")