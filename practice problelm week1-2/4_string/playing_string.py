# using + operator and f string

street = "lalita chokdi"
city = "Surat"
country = "India"
address = street +'\n'+ city +'\n'+ country
address_f = f'{street}\n{city}\n{country}'
print("Using + operator\n",address)
print("Using f-string\n",address_f)

# for calculating veggies and fruit

veggies =10
fruit = 2

total = f"I eat {veggies} veggies and {fruit} fruits daily"
print(total)
