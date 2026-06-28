from task1_lists_tuples import products


## a dictionary stores data in:
#  1.real dictionary
#  2.hashmap
#  3.unordered_map in c++
#  4.key-value pairs


price_dict = {"mobile phone":20000,"bedsheet":400,"mouse":1500,"study table":1000,"stickers":100}
print(price_dict)

price_dict["mobile phone"] = 25000

print(price_dict)

## using try and except to handle key errors
## safe deletion

product_name="stickers"

if product_name in price_dict:
    del price_dict[product_name]
    print(f"{product_name} deleted successfully.")
else:
    print(f"{product_name} not found.")



sum=0
num=0

for i in price_dict:
    sum +=price_dict[i]
    num +=1
   


max(price_dict.values())
min(price_dict.values())

print("average price:",sum/num)
print("max price:",max(price_dict.values()))

print(price_dict)
