result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]

count1 = 0
count2 = 0
for  item in result:
    if item == "heads":
        count1 += 1
    elif item == "tails":
        count2 += 1

print("head count",count1)
print("tails count",count2)