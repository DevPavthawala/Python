for i in range(1,6):
    print(f"you have complete the race{i}KM ")
    tired = input('Are you tired : "yes" or "no"')
    if tired == "yes":
        break

if i == 5:
    print("congrats you finise the race")
else:
    print(f"congrats you finise the {i}km race ,you win if you ran {5-i}km")
