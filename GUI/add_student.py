import tkinter as tk
from tkinter import messagebox
from pymongo import MongoClient
from datetime import datetime

# Kết nối với MongoDB Atlas
def connect_to_mongodb(class_ID):
    try:
        client = MongoClient()
        db = client["basicdb"]
        collection = db[class_ID]
        return collection
    except Exception as e:
        messagebox.showerror("Error", f"Could not connect to MongoDB: {e}")
        return None

def add_student(name, student_id, dob, class_ID):
    if not name or not student_id or not dob:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        # Kiểm tra định dạng ngày sinh
        dob_datetime = datetime.strptime(dob, "%Y-%m-%d")
    except ValueError:
        messagebox.showerror("Error", "Date of birth must be in YYYY-MM-DD format.")
        return

    # Dữ liệu sinh viên
    student_data = {
        "_id": student_id,
        "name": name,
        "date_of_birth": dob
    }

    # Lưu vào MongoDB
    collection = connect_to_mongodb(class_ID)
    if collection:
        try:
            collection.insert_one(student_data)
            messagebox.showinfo("Success", "Student added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Could not add student: {e}")
def window(add_std_frame: tk.Frame, class_ID):
    
    # Labels and Entries
    tk.Label(add_std_frame, text="Student Name:").grid(row=0, column=0, padx=10, pady=10)
    entry_name = tk.Entry(add_std_frame, width=30)
    entry_name.grid(row=0, column=1, padx=10, pady=10)
    entry_name.place()

    tk.Label(add_std_frame, text="Student ID:").grid(row=1, column=0, padx=10, pady=10)
    entry_id = tk.Entry(add_std_frame, width=30)
    entry_id.grid(row=1, column=1, padx=10, pady=10)
    entry_id.place()
    tk.Label(add_std_frame, text="Date of Birth (YYYY-MM-DD):").grid(row=2, column=0, padx=10, pady=10)
    entry_dob = tk.Entry(add_std_frame, width=30)
    entry_dob.grid(row=2, column=1, padx=10, pady=10)

    # Buttons
    btn_add = tk.Button(add_std_frame, text="Add Student", command=lambda:add_student(entry_name.get(), entry_id.get(), entry_dob.get(), class_ID))
    btn_add.grid(row=3, column=0, columnspan=2, pady=20)
    btn_add.place()
if __name__ == '__main__':
    window()