def apply_discount(price,discout_percent=5):
    if discount_percent>60:
        discount_percent=60

    final_price=price-(price*discount_percent/100)
    return final_price

print("the amount after discount is:",apply_discount(1000,10))
print("the amount after discount is :",apply_discount(500))