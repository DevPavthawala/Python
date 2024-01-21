india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

user = input("Enter the City Name from 'india' 'pakistan' and 'bangladesh' :")

if user in india:
    print("this city is in India")
elif user in pakistan:
    print("this city is in Pakistan")
elif user in bangladesh:
    print("this city is in Bangladesh")
else:
    print("your city is not preset in the dataset")