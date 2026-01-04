import tkinter as tk
from tkinter import messagebox

# ---------------- Data ----------------
students = []

# ---------------- Functions ----------------
def add_student():
    name = name_entry.get()
    roll = roll_entry.get()
    branch = branch_entry.get()

    if not name or not roll or not branch:
        messagebox.showwarning("Missing Data", "Please fill all fields")
        return

    students.append({"name": name, "roll": roll, "branch": branch})
    update_listbox()
    clear_fields()
    messagebox.showinfo("Success", "Student added successfully")

def delete_student():
    selected = listbox.curselection()
    if not selected:
        messagebox.showwarning("No Selection", "Please select a student")
        return

    students.pop(selected[0])
    update_listbox()
    messagebox.showinfo("Deleted", "Student removed")

def update_listbox():
    listbox.delete(0, tk.END)
    for s in students:
        listbox.insert(
            tk.END,
            f"  {s['roll']}  |  {s['name']}  |  {s['branch']}"
        )

def clear_fields():
    name_entry.delete(0, tk.END)
    roll_entry.delete(0, tk.END)
    branch_entry.delete(0, tk.END)

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Student Management System")
root.geometry("500x550")
root.configure(bg="#f4f6f8")
root.resizable(False, False)

# -------- Header --------
header = tk.Frame(root, bg="#2c3e50", height=70)
header.pack(fill="x")

tk.Label(
    header,
    text="Student Management System",
    bg="#2c3e50",
    fg="white",
    font=("Segoe UI", 16, "bold")
).pack(pady=18)

# -------- Card --------
card = tk.Frame(root, bg="white", bd=0, relief="flat")
card.pack(padx=20, pady=20, fill="x")

tk.Label(
    card,
    text="Add Student",
    bg="white",
    fg="#2c3e50",
    font=("Segoe UI", 13, "bold")
).pack(pady=(15, 10))

# -------- Form --------
form = tk.Frame(card, bg="white")
form.pack(padx=20, pady=10)

def styled_entry(parent):
    e = tk.Entry(
        parent,
        font=("Segoe UI", 10),
        bd=1,
        relief="solid",
        width=30
    )
    return e

tk.Label(form, text="Name", bg="white").grid(row=0, column=0, sticky="w", pady=5)
name_entry = styled_entry(form)
name_entry.grid(row=1, column=0, pady=5)

tk.Label(form, text="Roll No", bg="white").grid(row=2, column=0, sticky="w", pady=5)
roll_entry = styled_entry(form)
roll_entry.grid(row=3, column=0, pady=5)

tk.Label(form, text="Branch", bg="white").grid(row=4, column=0, sticky="w", pady=5)
branch_entry = styled_entry(form)
branch_entry.grid(row=5, column=0, pady=5)

# -------- Buttons --------
btn_frame = tk.Frame(card, bg="white")
btn_frame.pack(pady=15)

tk.Button(
    btn_frame,
    text="Add Student",
    command=add_student,
    bg="#27ae60",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=15,
    bd=0,
    cursor="hand2"
).grid(row=0, column=0, padx=10)

tk.Button(
    btn_frame,
    text="Delete Selected",
    command=delete_student,
    bg="#e74c3c",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    width=15,
    bd=0,
    cursor="hand2"
).grid(row=0, column=1, padx=10)

# -------- List Section --------
list_frame = tk.Frame(root, bg="white")
list_frame.pack(padx=20, pady=(0, 20), fill="both", expand=True)

tk.Label(
    list_frame,
    text="Student Records",
    bg="white",
    fg="#2c3e50",
    font=("Segoe UI", 12, "bold")
).pack(pady=10)

listbox = tk.Listbox(
    list_frame,
    font=("Consolas", 10),
    bd=0,
    height=10,
    selectbackground="#3498db",
    activestyle="none"
)
listbox.pack(padx=10, pady=10, fill="both", expand=True)

root.mainloop()