india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city1 = input("Enter the 1st City Name :")
city2 = input("Enter the 2nd City Name :")

if city1 in india  and city2 in india:
    print(f"{city1} and {city2} is in India")
elif city1 in pakistan and city2 in pakistan:
    print(f"{city1} and {city2} in Pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print(f"{city1} and {city2} is in Bangladesh")
else:
    print(f"{city1} and {city2} not preset in the dataset or both city is not in the same country")