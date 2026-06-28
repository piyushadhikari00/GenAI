def add_prices(prices,price):
    prices.append(price)

def get_average_price(prices):

    if len(prices) == 0:
        return 0
    return sum(prices)/len(prices)


def get_max_price(prices_list):
    if len(prices_list) == 0:
        return 0
    return max(prices_list)


prices=[]

while True:
    print("\n =======MENU=========")
    print("1 -> Add price")
    print("2 -> show average price")
    print("3 -> show maximum price")
    print("q -> quit")

    choice =input("enter the choice:")

    if choice == '1':

        try:
            price= float(input("enter price:"))
            add_prices(prices,price)
            print("price added successfully!")

        except ValueError:
            print("invailed input!")

    elif choice == '2':
        print("average price is:",get_average_price(prices))

    elif choice == '3':
        print("maximum price is:",get_max_price(prices))

    elif choice.lower() == 'q':
        print("exiting the program .....")
        break
    else:
        print("invailed choice!")