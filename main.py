import tkinter as tk
from tkinter import ttk, messagebox
import re

root = tk.Tk()
root.title("Employee Registration and Salary Utility System")
root.geometry("700x620")

BG = "#F5F0FF"
NAVY = "#5B4A8A"
ACCENT = "#9F86C0"
WHITE = "#FFFEFF"
BORDER = "#DDD6F3"
MUTED = "#9E8EC0"
TEXT = "#3D3060"
GREEN = "#5FAD8E"
RED = "#D4717A"
AMBER = "#C99A6B"
INFO_BG = "#EDE9FF"

style = ttk.Style()
style.theme_use("clam")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

home_tab = tk.Frame(notebook, bg=BG)
emp_tab = tk.Frame(notebook, bg=BG)
salary_tab = tk.Frame(notebook, bg=BG)

notebook.add(home_tab, text="  Home  ")
notebook.add(emp_tab, text="  Employee Management  ")
notebook.add(salary_tab, text="  Salary Calculator  ")

# ---------------- HOME TAB (RESTORED) ----------------
banner = tk.Frame(home_tab, bg=NAVY, height=80)
banner.pack(fill="x")
banner.pack_propagate(False)

tk.Label(banner, text="Employee Registration and Salary Utility System",
         font=("Arial", 16, "bold"), bg=NAVY, fg=WHITE).pack(expand=True)

tk.Frame(home_tab, bg=ACCENT, height=3).pack(fill="x")

notice = tk.Frame(home_tab, bd=1, relief="solid", bg=WHITE,
                  highlightbackground=BORDER)
notice.pack(pady=20, padx=40, fill="x")

tk.Label(notice,
         text="Welcome to Employee Registration\nand Salary Utility System",
         font=("Arial", 13, "bold"), bg=WHITE, fg=NAVY,
         justify="center").pack(pady=20)

cards_row = tk.Frame(home_tab, bg=BG)
cards_row.pack(padx=40, fill="x")

def info_card(parent, title, body, col):
    f = tk.Frame(parent, bg=WHITE, bd=1, relief="solid",
                 highlightbackground=BORDER)
    f.grid(row=0, column=col, padx=6, pady=4, sticky="ew")
    parent.columnconfigure(col, weight=1)

    tk.Label(f, text=title, font=("Arial", 9, "bold"),
             bg=WHITE, fg=NAVY).pack(anchor="w", padx=12, pady=(10, 2))
    tk.Label(f, text=body, font=("Arial", 8),
             bg=WHITE, fg=MUTED, wraplength=160,
             justify="left").pack(anchor="w", padx=12, pady=(0, 10))

info_card(cards_row, "Employee Management",
          "Add, view and delete employee records with full validation.", 0)
info_card(cards_row, "Salary Calculator",
          "Calculate total salary from daily wage and working days.", 1)
info_card(cards_row, "Data Validation",
          "All fields are validated like email, name format and salary.", 2)

tk.Label(home_tab, text="Use the tabs above to get started.",
         font=("Arial", 9), fg=MUTED, bg=BG).pack(pady=(14, 0))

# ---------------- EMPLOYEE TAB ----------------
form = tk.Frame(emp_tab, bg=BG)
form.pack(pady=10)

for i, lbl in enumerate(["Name", "Department", "Salary", "Email"]):
    tk.Label(form, text=lbl, bg=BG, fg=TEXT).grid(row=i, column=0, padx=10, pady=5, sticky="e")

name = tk.Entry(form)
salary = tk.Entry(form)
email = tk.Entry(form)

name.grid(row=0, column=1)
salary.grid(row=2, column=1)
email.grid(row=3, column=1)

dept_var = tk.StringVar(value="Select Department")
dept = ttk.Combobox(form, textvariable=dept_var, state="readonly",
                    values=["Human Resources", "Finance", "Engineering",
                            "Marketing", "Operations", "Legal"])
dept.grid(row=1, column=1)

columns = ("ID", "Name", "Department", "Salary", "Email")
tree = ttk.Treeview(emp_tab, columns=columns, show="headings", height=8)

for col in columns:
    tree.heading(col, text=col)

tree.pack(pady=10)

tree.insert("", tk.END, values=(1, "Emaan Fatima", "Engineering", "60,000", "emaan@company.com"))

def clear():
    name.delete(0, tk.END)
    salary.delete(0, tk.END)
    email.delete(0, tk.END)
    dept_var.set("Select Department")

def add_employee():
    n = name.get().strip()
    dp = dept_var.get()
    s = salary.get().strip()
    em = email.get().strip()

    if not n or dp == "Select Department" or not s or not em:
        messagebox.showerror("Validation Error", "All fields are required.")
        return
    if re.search(r"\d", n):
        messagebox.showerror("Validation Error", "Name must not contain numbers.")
        return
    if not re.match(r"^[^\s@]+@[^\s@]+\.[^\s@]{2,}$", em):
        messagebox.showerror("Validation Error", "Enter a valid email address.")
        return
    try:
        sal = float(s)
        if sal <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Validation Error", "Salary must be a positive number.")
        return

    new_id = len(tree.get_children()) + 1
    tree.insert("", tk.END, values=(new_id, n, dp, "{:,.2f}".format(sal), em))

    messagebox.showinfo("Success", n + " added successfully.")
    clear()

def delete_selected():
    sel = tree.selection()
    if not sel:
        messagebox.showwarning("Delete", "Select a row to delete.")
        return

    confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete?")
    if confirm:
        for item in sel:
            tree.delete(item)
        messagebox.showinfo("Deleted", "Record deleted successfully.")

btn_frame = tk.Frame(emp_tab, bg=BG)
btn_frame.pack()

tk.Button(btn_frame, text="Add", bg=NAVY, fg=WHITE, command=add_employee).grid(row=0, column=0, padx=5)
tk.Button(btn_frame, text="Clear", bg=AMBER, fg=WHITE, command=clear).grid(row=0, column=1, padx=5)
tk.Button(btn_frame, text="Delete", bg=RED, fg=WHITE, command=delete_selected).grid(row=0, column=2, padx=5)

# ---------------- SALARY TAB (RESTORED) ----------------
sal_banner = tk.Frame(salary_tab, bg=NAVY, height=60)
sal_banner.pack(fill="x")
sal_banner.pack_propagate(False)

tk.Label(sal_banner, text="Salary Calculator",
         font=("Arial", 14, "bold"), bg=NAVY, fg=WHITE).pack(expand=True)

tk.Frame(salary_tab, bg=ACCENT, height=3).pack(fill="x")

inp_card = tk.Frame(salary_tab, bg=WHITE, bd=1, relief="solid",
                    highlightbackground=BORDER)
inp_card.pack(padx=40, pady=20, fill="x")

tk.Label(inp_card, text="Enter Salary Details",
         font=("Arial", 10, "bold"), bg=WHITE, fg=NAVY).pack(anchor="w", padx=16, pady=(12, 4))

tk.Frame(inp_card, bg=BORDER, height=1).pack(fill="x", padx=16)

sal_form = tk.Frame(inp_card, bg=WHITE)
sal_form.pack(padx=16, pady=14, fill="x")
sal_form.columnconfigure(1, weight=1)

def sal_field(label, row):
    tk.Label(sal_form, text=label, bg=WHITE, fg=MUTED).grid(row=row*2, column=0, sticky="w")
    e = tk.Entry(sal_form)
    e.grid(row=row*2+1, column=0, sticky="ew", ipady=3)
    return e

e_wage = sal_field("Daily Wage (PKR)", 0)
e_days = sal_field("Working Days", 1)
e_bonus = sal_field("Bonus", 2)

res_card = tk.Frame(salary_tab, bg=WHITE, bd=1, relief="solid",
                    highlightbackground=BORDER)
res_card.pack(padx=40, pady=10, fill="x")

breakdown_frame = tk.Frame(res_card, bg=WHITE)
breakdown_frame.pack(padx=16, pady=10, fill="x")

lbl_basic = tk.Label(breakdown_frame, text="Basic Pay: —", bg=WHITE)
lbl_basic.pack(anchor="w")

lbl_bonus = tk.Label(breakdown_frame, text="Bonus: —", bg=WHITE)
lbl_bonus.pack(anchor="w")

lbl_total = tk.Label(breakdown_frame, text="Total Salary: —",
                     bg=WHITE, font=("Arial", 10, "bold"))
lbl_total.pack(anchor="w")

def calculate():
    try:
        wage = float(e_wage.get())
        days = int(e_days.get())
        bonus = float(e_bonus.get() or 0)

        if wage <= 0 or days <= 0 or bonus < 0:
            raise ValueError

        basic = wage * days
        total = basic + bonus

        lbl_basic.config(text="Basic Pay: PKR {:,.2f}".format(basic))
        lbl_bonus.config(text="Bonus: PKR {:,.2f}".format(bonus))
        lbl_total.config(text="Total Salary: PKR {:,.2f}".format(total), fg=GREEN)

        messagebox.showinfo("Success", "Salary calculated successfully.")

    except:
        messagebox.showerror("Error", "Enter valid numbers.")

def clear_sal():
    e_wage.delete(0, tk.END)
    e_days.delete(0, tk.END)
    e_bonus.delete(0, tk.END)

    lbl_basic.config(text="Basic Pay: —")
    lbl_bonus.config(text="Bonus: —")
    lbl_total.config(text="Total Salary: —")

tk.Button(salary_tab, text="Calculate", bg=GREEN, fg=WHITE, command=calculate).pack(pady=5)
tk.Button(salary_tab, text="Clear", bg=AMBER, fg=WHITE, command=clear_sal).pack(pady=5)

root.mainloop()
