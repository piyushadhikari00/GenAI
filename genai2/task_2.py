# task_2.py
orders = [1200, 2500, 800, 1750, 3000]

total_revenue = 0
for i in orders:

  if i >= 2000:

    discount = 15
 
  elif i >= 1500:

    discount = 10


  elif i >= 1000:

    discount = 7


  else:

    discount = 0


discount_amount = (i * discount) / 100


final_amount = i - discount_amount


total_revenue += final_amount


print("Order Amount:", i)
print("Discount Applied:", discount, "%")
print("Final Amount:", final_amount)

print("--------------------------------")



print("Total Revenue:", total_revenue)


     