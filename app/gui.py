import tkinter as tk
from tkinter import messagebox

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        if weight <= 0 or height <= 0:
            raise ValueError("Weight and height must be positive values.")
        
        bmi = weight / (height ** 2)
        category = classify_bmi(bmi)
        result_label.config(text=f"Your BMI is: {bmi:.2f} ({category})")
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def reset_fields():
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)
    result_label.config(text="")
    weight_entry.focus()

# GUI setup
def main():
    global weight_entry, height_entry, result_label
    root = tk.Tk()
    root.title("BMI Calculator")
    
    # Set dark theme colors
    root.configure(bg='#0a0a0a')
    label_color = '#ffffff'
    
    tk.Label(root, text="Weight (kg):", bg='#0a0a0a', fg=label_color).pack(pady=5)
    weight_entry = tk.Entry(root, bg='#333333', fg=label_color)
    weight_entry.pack(pady=5)

    tk.Label(root, text="Height (m):", bg='#0a0a0a', fg=label_color).pack(pady=5)
    height_entry = tk.Entry(root, bg='#333333', fg=label_color)
    height_entry.pack(pady=5)

    tk.Button(root, text="Calculate BMI", command=calculate_bmi, bg='#444444', fg=label_color).pack(pady=10)
    
    tk.Button(root, text="Reset", command=reset_fields, bg='#444444', fg=label_color).pack(pady=5)

    result_label = tk.Label(root, text="", bg='#0a0a0a', fg=label_color)
    result_label.pack(pady=5)

    weight_entry.focus()

    root.mainloop()

if __name__ == "__main__":
    main()
