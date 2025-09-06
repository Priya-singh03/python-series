#movie tickets are $12 for adults(18 and over), $8 for children.Everyone gets a $2 discount on wednesday.
age = 22
day = "wednesday"

price = 12 if age >= 18 else 8
#print(price)
if day == "wednesday":
    price -= 2
print(price)