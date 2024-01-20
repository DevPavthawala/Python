# using with function we don't need to close the function


with open("E://Python//custion_for_datascience//funny.txt","r") as f:
    print(f.read())

print(f.closed)