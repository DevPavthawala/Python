expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ["january","febuary","march","april","may"]

expense = int(input("Enter your expense form jan to may"))
month = -1

for i in range(len(expense_list)):
    if expense == expense_list[i]:
        month = i
        break

if month != -1:
    print(f"the {expense} is an expense of {month_list[month]}")
else:
    print(f"you did't spend {expense} in any month")
