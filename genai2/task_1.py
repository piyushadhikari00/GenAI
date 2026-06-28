try:
    order_amount=int(input("enter the orders:"))

except ValueError:
     print("invalid input! please enter a number. ")
     exit()


   
if order_amount>=2000:
       
       discount=0.15

       order_amount=order_amount-order_amount*discount

       print("the amount after discount is:",order_amount)

elif order_amount>=1500:
       
       discount=0.10

       order_amount=order_amount-order_amount*discount

       print("the amount after discount is:",order_amount)


elif order_amount>=1000:
       
       discount=0.05

       order_amount=order_amount-order_amount*discount

       print("the amount after discount is:",order_amount)

else:
       
       discount=0

       order_amount=order_amount*1

       print("no discount applied!")

       print("the amount is:",order_amount)

