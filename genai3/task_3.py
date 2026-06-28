gst = lambda price:price+(0.18*price)
print(gst(100))

final_price=lambda price:(price - (0.10*price))+(0.18*(price - (0.10*price)))

print(final_price(100))