file = open('sales_data.txt','r')

sales = []

for line in file.readlines():
    sales.append(float(line.strip()))

file.close()

total_sales = sum(sales)
highest_sale = max(sales)
lowest_sale = min(sales)
average_sales = total_sales / len(sales)

print("Total Sales:",total_sales)
print("Highest Sales:",highest_sale)
print("Lowest Sales:",lowest_sale)
print("Average Sales:",average_sales)