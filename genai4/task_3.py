new_sales=[5000,2500,1700]
with open('sales_data.txt','a') as file:
    for amount in new_sales:
        file.write(str(amount) + '\n')
        print(f"the sales amount {amount} has been appended to the file.")

with open('sales_data.txt','r') as file:
    print("=====updated sales data======")
    print(file.read())
    
file =open("sales_data.txt",'r')

items = file.readlines()

file.close()

print(items)
print("number of lines:",len(items))