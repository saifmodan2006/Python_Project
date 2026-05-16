# Make a BMI Calculator
from tkinter import *
from tkinter import messagebox  
def calculate_bmi():
    try:
        weight = float(entry_weight.get())
        height = float(entry_height.get()) / 100  # Convert cm to meters
        bmi = weight / (height ** 2)
        bmi = round(bmi, 2)
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"
        messagebox.showinfo("BMI Result", f"Your BMI is {bmi} ({category})")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")
root = Tk()
root.title("BMI Calculator")
root.geometry("300x200")
label_weight = Label(root, text="Weight (kg):")
label_weight.pack(pady=5)
entry_weight = Entry(root)
entry_weight.pack(pady=5)
label_height = Label(root, text="Height (cm):")
label_height.pack(pady=5)
entry_height = Entry(root)
entry_height.pack(pady=5)
button_calculate = Button(root, text="Calculate BMI", command=calculate_bmi)
button_calculate.pack(pady=20)
if __name__ == "__main__":
    root.mainloop()
    