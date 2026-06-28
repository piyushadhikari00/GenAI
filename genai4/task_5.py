file = open("products.txt",'w')

n=int(input("enter the number of products needs to stored :"))
for i in range(n):

    product =input("enter the product name:")
    price = float(input("enter the price of the product:"))

    file.write(product + "," + str(price) + "\n")

file.close()

print("\nStored products:\n")

file = open("products.txt",'r')

for line in file:
    print(line.strip())

file.close()