file = open('sales_data.txt','r')

print("===using read()====")
content = file.read()
print(content)

file.close()

file = open('sales_data.txt','r')

print("====using radline()====")
first_line = file.readline().strip()
print(first_line)

file.close()


file = open('sales_data.txt','r')

print('====using readlines()====')
lines = file.readlines()

sales=[]

for line in lines:
    sales.append(int(line.strip()))

print(sales)

file.close()