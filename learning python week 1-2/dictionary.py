d = {"dev":9409462433,"dad":8000426886,"mom":9898330370}
print(d)
print(d["dev"])
print(d["mom"])
print(d["dad"])

# adding a new numbers in dictionary    

d["neel"]=1234567890
print(d)

# delete a numbers for dictionary

del d["neel"]
print(d)


for key in d:
    print("key :",key,"value:",d[key])

for k,v in d.items():
    print("key :", k, "value:",v)

# checking if any key is present in dictonary
"mom " in d

# clear whole dictonary

d.clear()
print(d)


