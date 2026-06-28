# task_4.py

# List of daily sales
daily = [200, 150, 0, 400, 50, -1, 300]

# Variable to store total sales
total_sales = 0

# Process daily sales
for i in daily:

    # Stop processing if -1 is found
    if i == -1:

        print("Sales entry stopped.")
        break

    # Skip days with zero sales
    elif i == 0:

        print("No sales today.")
        continue

    # Add valid sales
    else:

        total_sales = total_sales + i

        # Display running total after each sale
        print("Running Total Sales:", total_sales)

# Display final total sales
print("Total Sales of the Week:", total_sales)