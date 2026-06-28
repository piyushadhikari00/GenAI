# Week 4 – Python File Handling and Data Processing

## Overview

This assignment focuses on learning and applying Python File Handling concepts. Through Tasks 1–7, various techniques for reading, writing, appending, processing, and validating file data were implemented.

The tasks gradually progress from basic file operations to building small file-based applications that generate reports and process structured data.

---

# Topics Learned

## 1. File Creation and Writing

Learned how to create new files and store data permanently using Python.

### Concepts Covered

* Opening files using `open()`
* Write Mode (`"w"`)
* Writing text using `write()`
* Creating structured file content

### Example

```python
file = open("data.txt", "w")
file.write("Hello World")
file.close()
```

---

## 2. Reading Files

Learned multiple methods of reading data from files.

### Methods Studied

### `read()`

Reads the entire file content.

```python
content = file.read()
```

### `readline()`

Reads one line at a time.

```python
line = file.readline()
```

### `readlines()`

Reads all lines and stores them in a list.

```python
lines = file.readlines()
```

---

## 3. Cleaning File Data

Learned how to remove unwanted characters while processing file content.

### `strip()`

Removes:

* Spaces
* Tabs
* Newline characters (`\n`)

Example:

```python
line = line.strip()
```

---

## 4. Converting File Data into Integers

Learned how to transform text-based file data into numeric values for calculations.

### Example

```python
sales.append(int(line.strip()))
```

---

## 5. Appending Data to Existing Files

Learned how to add new information without deleting existing data.

### Append Mode

```python
file = open("sales_data.txt", "a")
```

### Applications

* Adding new sales records
* Updating logs
* Storing new user entries

---

## 6. Generating Reports from File Data

Learned how to analyze data stored inside files.

### Operations Performed

* Total Sales Calculation
* Highest Sale Identification
* Lowest Sale Identification
* Average Sales Calculation

### Functions Learned

#### `sum()`

Calculates total.

```python
sum(numbers)
```

#### `max()`

Finds largest value.

```python
max(numbers)
```

#### `min()`

Finds smallest value.

```python
min(numbers)
```

#### `len()`

Counts items.

```python
len(numbers)
```

---

## 7. User Input and File Storage

Learned how to collect information from users and save it into files.

### Skills Practiced

* Input handling
* Data formatting
* File writing
* Data retrieval

### Example Format

```text
ProductName | Price
```

---

## 8. File Existence Validation

Learned how to safely open files and prevent runtime errors.

### Module Used

```python
import os
```

### Function Learned

#### `os.path.exists()`

Checks whether a file exists before opening it.

```python
if os.path.exists(filename):
```

### Benefits

* Prevents program crashes
* Improves reliability
* Better user experience

---

## 9. Dictionaries

Learned how to store related information using key-value pairs.

### Example

```python
prices = {
    "Mouse": 500,
    "Keyboard": 800
}
```

### Accessing Values

```python
prices["Mouse"]
```

---

## 10. Dictionary Traversal

Learned how to process all dictionary entries.

### `items()`

Returns both key and value.

```python
for product, price in prices.items():
```

---

## 11. Report Generation

Built a mini-project that:

* Processes product prices
* Applies discounts
* Generates reports
* Stores reports in files
* Calculates summary statistics

### Real-World Applications

* Billing Systems
* Inventory Systems
* Sales Tracking
* E-commerce Reporting

---

# Files Included

```text
week4/
│
├── task_1.py
├── task_2.py
├── task_3.py
├── task_4.py
├── task_5.py
├── task_6.py
├── task_7.py
├── sales_data.txt
├── products.txt
├── discount_report.txt
└── README.md
```

---

# How to Run

Run any task individually:

```bash
python task_1.py
```

```bash
python task_2.py
```

```bash
python task_3.py
```

```bash
python task_4.py
```

```bash
python task_5.py
```

```bash
python task_6.py
```

```bash
python task_7.py
```

---

# Key Learning Outcomes

After completing these tasks, the following Python concepts were practiced:

* File Handling
* Reading Files
* Writing Files
* Appending Files
* Data Cleaning
* Type Conversion
* Lists
* Dictionaries
* User Input
* Report Generation
* Error Handling
* File Validation
* Data Analysis
* Summary Statistics

These tasks provide a strong foundation for building larger applications involving file management, data processing, and report generation in Python.