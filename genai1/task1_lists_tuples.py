# -> Ordered 
# -> Mutable(Changeable)
# -> Allows Duplicates

products = ["mobile phone","keyboard","study table","table","bedsheet","mouse"]

# -> Python stores lists as Dynamic arrays:
#    1. contiguous memory
#    2. automatic resizing



# USES 
# . Store products
# . store users
# . AI datasets
# . DSA arrays

# ------------------------------------------------------------

# tuple is :
#   1. ordered
#   2. immutaable
#   3. allows duplicates
#   4. data should not be changed or altered

sample_product = ('mouse',2000,'accessory')

print(products[1])
print(products[-1])
products.extend(['chair','shoes'])
print(products)

sample_products = list(sample_product)
sample_products[1]=2500
sample_product=tuple(sample_products)
print(sample_products)





# real uses
# 1. database rows
# 2. coordinates
# 3. immutable configurations