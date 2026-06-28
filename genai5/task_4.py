# ---------- Task 1 ----------
import task_1
from task_1 import square

print("Task 1")
print("Add:", task_1.add(10, 5))
print("Subtract:", task_1.subtract(10, 5))
print("Square:", square(6))


# ---------- Task 2 ----------
import task_2

text = "python modules and packages"

print("\nTask 2")
print("Capitalized:", task_2.capitalize_words(text))
print("Reversed:", task_2.reverse_string(text))
print("Word Count:", task_2.word_count(text))


# ---------- Task 4 ----------
import task3_1 as disc
from task3_2 import calculate_total

print("\nTask 4")

print("10% Discount on 1000 =", disc.apply_discount(1000, 10))
print("Flat Discount on 1000 =", disc.flat_discount(1000))

prices = [100, 200, 300]
print("Total Bill =", calculate_total(prices))