sales_amount =[1200,450,980,1500,3000]

with open('sales_data.txt','w') as file:
    for amount in sales_amount:
        file.write(str(amount) + '\n')
        print(f"the sales amount {amount} has been written to the file.")

with open('sales_data.txt','r') as file:
    for line in file:
        print(line)