def calaculate_total(exp):
    total = 0
    for iteam in exp:
        total = total+iteam
    return total

tom_expense_list=[2100,200,2500]
jhon_expense_list=[5400,52,250]

tom_total = calaculate_total(tom_expense_list)
jhon_total = calaculate_total(jhon_expense_list)

print("tom total is ",tom_total)
print("jhon total is ",jhon_total)