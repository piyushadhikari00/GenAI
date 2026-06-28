from task1_lists_tuples import products
from task2_sets import categories

catalog={}

category_to_products={}
for product ,category in zip(products,categories):
    catalog[product]=category

    if category not in category_to_products:
        category_to_products[category]=[]
    category_to_products[category].append(product)

    
print("catalog:")
print(catalog)

print("\nCategory to products:")
print(category_to_products)

max_category=max(
    category_to_products,
    key=lambda c: len(category_to_products[c])
)

print("\nCategory with most products:",max_category)
print(max_category)
print("products:",category_to_products[max_category])