process_price=[100,200,300,400,850,1200,6509,2500]

discounted_price=list(map(lambda x:x-(0.10*x),process_price))
print("the discounted price of products are:",discounted_price)

print(list(filter(lambda x:x>300,discounted_price)))
