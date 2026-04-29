# Payroll Management System (Tkinter)

## Overview

This is a Python-based desktop GUI application built using Tkinter. The system allows users to manage employee records and calculate salaries through an interactive interface.

---

## Features

### 1. Employee Management

* Add new employees
* View employee records in a table
* Delete selected employee records
* Input validation for all fields

### 2. Salary Calculator

* Calculate salary using:

  * Daily wage
  * Number of working days
  * Optional bonus
* Displays breakdown of salary calculation

### 3. Data Validation

* Ensures all fields are filled
* Validates email format using regex
* Prevents numeric values in name field
* Ensures salary is a positive number

---

## Technologies Used

* Python 3.x
* Tkinter (GUI library)
* ttk (Themed widgets)
* re module (Regular Expressions)

---

## How to Run

1. Install Python (3.x recommended)
2. Save the file as `main.py`
3. Open terminal or command prompt
4. Run the program:

   ```bash
   python main.py
   ```

---

## Project Structure

* Home Tab → Introduction dashboard
* Employee Management Tab → Add/View/Delete employees
* Salary Calculator Tab → Salary computation system

---

## Logic Summary

* Treeview used for tabular employee data
* Regex used for email and name validation
* Float/int conversion used for salary calculations
* Messagebox used for error and success notifications

---

## Author

This project was developed as part of a Python GUI lab assignment to understand desktop application development using Tkinter.

---

## Conclusion

This project demonstrates how a simple HR system can be built using Python GUI, covering real-world concepts like validation, data handling, and user interaction.
