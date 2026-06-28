high_price = list(filter(lambda x:x>500,[100,2500,400,1200,50,2000,850]))
print("the price of products having price greater than 500 are:",high_price)

price=list(filter(lambda x:x<=500,[100,250,400,1200,50,2000,850]))
print("the price of products having price less than or equal to 500 are:",price)