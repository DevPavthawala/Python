import time

time_strap = time.strftime("%H:%M:%S")
print(time_strap)

time_Hour = int(time.strftime("%H"))
time_min = int(time.strftime("%M"))
time_sec = int(time.strftime("%S"))

# print(time_Hour,time_min,time_sec)
if(time_Hour<9 and time_Hour>5):
    print("Guten Morgan")
elif(time_Hour>9 and time_Hour<16):
    print("Guten Tag")
else:
    print("Gute Nacht")
