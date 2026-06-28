orders = []

while True:


  print("\n======= MENU =======")
  print("1. Add Order Amount") 
  print("2. Calculate Discounts")
  print("q. Quit")

  action = input("Choose an action: ")

  if action == '1':

      try:
 
          amount = float(input("Enter the order amount: "))

          # Validate positive input
          if amount <= 0:

              print("Order amount must be greater than 0.")
            

          # Add order to list
          orders.append(amount)

          print("Order added successfully!")

      except ValueError:

          print("Invalid input! Please enter a valid number.")

  elif action == '2':

      # Check if orders list is empty
        if len(orders) == 0:

          print("No orders available.")
        

        print("\n======= DISCOUNT DETAILS =======")

        total_final = 0

        # Process each order
        for i in orders:

        # Apply discount rules

          # 15% discount for orders >= 2000
          if i >= 2000:

              discount = 15

          # 10% discount for orders between 1500 and 1999
          elif i >= 1500:

              discount = 10

          # 7% discount for orders between 1000 and 1499
          elif i >= 1000:

              discount = 7

          # No discount below 1000
          else:

              discount = 0

          # Calculate discount amount
          discount_amount = (i * discount) / 100

          # Calculate final amount
          final_amount = i - discount_amount

          # Add to total payable amount
          total_final += final_amount

          # Display details
          print("\nOrder Amount:", i)
          print("Discount Applied:", discount, "%")
          print("Final Amount:", final_amount)

          print("--------------------------------")

      # Display total payable amount
        print("\nTotal Payable Amount:", total_final)

  # Quit program
  elif action == 'q':

      print("Exiting the program. Goodbye!")

  # Invalid menu choice
  else:

      print("Invalid action! Try again.")