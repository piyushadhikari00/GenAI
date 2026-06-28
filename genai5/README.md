# Python Modules & Packages Assignment

## 📌 Overview

This project demonstrates the fundamentals of **Python Modules** and **Packages**. It includes creating custom modules, importing them in different ways, and organizing related functions into a package.

The project is designed for beginners to understand how Python code can be modularized and reused efficiently.

---

##  Project Structure

```text
Project/
│
├── main1.py
|── main2.py
├── task_1.py
├── task_2.py
├── README.md
│
└── shop_package/
    ├── __init__.py
    ├── task3_1.py
    └── task3_2.py
```

---

## 📖 Features

### 1. Math Utilities (`task_1.py`)

Provides basic mathematical operations.

**Functions:**

* `add(a, b)` → Returns the sum of two numbers.
* `subtract(a, b)` → Returns the difference between two numbers.
* `square(n)` → Returns the square of a number.

---

### 2. String Utilities (`task_2.py`)

Provides useful string manipulation functions.

**Functions:**

* `capitalize_words(text)` → Capitalizes the first letter of each word.
* `reverse_string(text)` → Reverses the given string.
* `word_count(text)` → Counts the number of words in the string.

---

### 3. Shop Package (`shop_package`)

Demonstrates how Python packages are created and imported.

#### `task3_1.py`

* `apply_discount(price, percent)` → Applies a percentage discount.
* `flat_discount(price)` → Applies a flat discount of ₹50.

#### `task3_2.py`

* `calculate_total(prices)` → Calculates the total bill.
* `apply_tax(amount)` → Adds 5% tax to the amount.

#### `__init__.py`

Exports commonly used functions for easier package imports.

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<repository-name>.git
```

### 2. Navigate to the project folder

```bash
cd <repository-name>
```

### 3. Run the program

```bash
python main.py
```

---

## 💻 Sample Output

```text
Task 1
Add: 15
Subtract: 5
Square: 36

Task 2
Capitalized: Python Modules And Packages
Reversed: segakcap dna seludom nohtyp
Word Count: 4

Task 4
10% Discount on 1000 = 900.0
Flat Discount on 1000 = 950
Total Bill = 600
```

---

## 🛠️ Technologies Used

* Python 3
* VS Code
* Git
* GitHub

---

## 📚 Concepts Covered

* Python Modules
* Python Packages
* Function Definitions
* Relative Imports
* Package Initialization (`__init__.py`)
* Import Statements
* Code Reusability

---

## 🎯 Learning Objectives

After completing this project, you will understand how to:

* Create custom Python modules.
* Import modules using different methods.
* Organize code into packages.
* Use relative imports.
* Improve code readability and maintainability.

---



Piyush Adhikari