# *****************break***************************

for i in range(12):
    if(i==10):
        break # exit the loop
    print("5x ",i+1,"=",5*(i+1))
    
# ******************continue********************************

for i in range(12):
    if(i==10):
        print("Skip the itreation")
        continue # exit the loop
    print("5x ",i,"=",5*i)
    