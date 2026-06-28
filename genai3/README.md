# Python Functions, Lambda, Map, Filter and Menu-Based Programs

## Overview

This project contains solutions for Tasks 1–7 covering:

* Functions
* Default Parameters
* Lambda Functions
* map()
* filter()
* Menu-Driven Programs
* List Processing

Each task is implemented in a separate Python file.

---

## Task 1 – Basic Function: Price After Discount

### Description

Creates a function `apply_discount(price, discount_percent=5)` that:

* Returns the final price after discount.
* Uses a default discount of 5% if no discount is provided.
* Optionally limits discount values to a maximum of 60%.

### Concepts Used

* Functions
* Parameters
* Default Arguments
* Conditional Statements

---

## Task 2 – Discount Calculator

### Description

Processes multiple order amounts and:

* Applies discounts based on order value.
* Calculates final payable amount.
* Displays total revenue generated.

### Discount Rules

| Order Amount   | Discount |
| -------------- | -------- |
| 2000 and above | 15%      |
| 1500 – 1999    | 10%      |
| 1000 – 1499    | 7%       |
| Below 1000     | 0%       |

### Concepts Used

* Loops
* if-elif-else
* Lists
* Arithmetic Operations

---

## Task 3 – Lambda Function: GST Calculator

### Description

Creates a lambda function that:

* Adds 18% GST to a product price.
* Calculates final amount after GST.

### Concepts Used

* Lambda Functions
* Mathematical Expressions

---

## Task 4 – Using map(): Apply GST to List of Prices

### Description

Uses `map()` along with a GST lambda function to:

* Apply GST to all prices in a list.
* Generate a new list containing updated prices.

### Concepts Used

* Lambda Functions
* map()
* Lists

---

## Task 5 – Using filter(): Filter Expensive Products

### Description

Uses `filter()` to:

* Extract prices greater than 500.
* Extract prices less than or equal to 500.

### Concepts Used

* Lambda Functions
* filter()
* Lists

---

## Task 6 – Combined Utility Function

### Description

Creates a function `process_prices(prices)` that:

1. Applies a 10% discount to all prices using `map()`.
2. Filters discounted prices above 300 using `filter()`.
3. Returns both processed lists.

### Concepts Used

* Functions
* map()
* filter()
* Lambda Functions

---

## Task 7 – Menu Using Functions

### Description

Creates a menu-driven application with functions:

* Add a new price
* Show average price
* Show maximum price
* Exit program

### Available Menu Options

```text
1 -> Add Price
2 -> Show Average Price
3 -> Show Highest Price
q -> Quit
```

### Concepts Used

* Functions
* Lists
* Loops
* Menu-Driven Programming
* Exception Handling

---

## Project Structure

```text
project/
│
├── task_1.py
├── task_2.py
├── task_3.py
├── task_4.py
├── task_5.py
├── task_6.py
├── task_7.py
└── README.md
```

---

## How to Run

Open a terminal in the project directory and run any task individually.

### Run Task 1

```bash
python task_1.py
```

### Run Task 2

```bash
python task_2.py
```

### Run Task 3

```bash
python task_3.py
```

### Run Task 4

```bash
python task_4.py
```

### Run Task 5

```bash
python task_5.py
```

### Run Task 6

```bash
python task_6.py
```

### Run Task 7

```bash
python task_7.py
```

---

## Requirements

* Python 3.x
* No external libraries required

---

## Learning Outcomes

After completing these tasks, the following concepts are demonstrated:

* Function Creation
* Default Parameters
* Lambda Functions
* List Processing
* map()
* filter()
* Conditional Statements
* Looping Constructs
* Exception Handling
* Menu-Based Program Design