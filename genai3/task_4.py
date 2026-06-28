original_price_list=list(map(lambda x:x,[100,250,400,1200,50,2000,850]))
print("the original prices are:",original_price_list)

discounted_price_list=list(map(lambda x:x+(0.18*x,original_price_list)))
print("the discounted prices are:",discounted_price_list)