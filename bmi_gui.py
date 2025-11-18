import tkinter as tk
from tkinter import messagebox
import csv
import os
import matplotlib.pyplot as plt # type: ignore

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())

        if weight <= 0 or height <= 0:
            messagebox.showerror("Error", "Weight and Height must be positive numbers!")
            return

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        result_label.config(text=f"BMI: {bmi:.2f}\nCategory: {category}")

        save_data(bmi, category)

    except ValueError:
        messagebox.showerror("Error", "Enter valid numbers!")

def save_data(bmi, category):
    file_exists = os.path.isfile("bmi_data.csv")

    with open("bmi_data.csv", "a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["BMI", "Category"])
        writer.writerow([bmi, category])

def show_graph():
    if not os.path.isfile("bmi_data.csv"):
        messagebox.showerror("Error", "No data found!")
        return

    bmi_values = []

    with open("bmi_data.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            bmi_values.append(float(row["BMI"]))

    plt.plot(bmi_values, marker='o')
    plt.title("BMI Trend Graph")
    plt.xlabel("Entry Number")
    plt.ylabel("BMI Value")
    plt.grid()
    plt.show()

# GUI Setup
root = tk.Tk()
root.title("Advanced BMI Calculator")
root.geometry("350x350")

tk.Label(root, text="Enter Weight (kg):").pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

tk.Label(root, text="Enter Height (m):").pack()
height_entry = tk.Entry(root)
height_entry.pack()

tk.Button(root, text="Calculate BMI", command=calculate_bmi).pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

tk.Button(root, text="Show BMI Trend Graph", command=show_graph).pack(pady=10)

root.mainloop()
