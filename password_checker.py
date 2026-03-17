import re
import tkinter as tk

def check_password():
    password = entry.get()
    
    if len(password) < 8:
        result.set("Weak: At least 8 characters required")
    elif not re.search(r"[0-9]", password):
        result.set("Weak: Add a number")
    elif not re.search(r"[A-Z]", password):
        result.set("Weak: Add uppercase letter")
    elif not re.search(r"[a-z]", password):
        result.set("Weak: Add lowercase letter")
    elif not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        result.set("Weak: Add special character")
    else:
        result.set("Strong Password ✅")

# Create window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x200")

# UI Elements
label = tk.Label(root, text="Enter Password:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(root, show="*", width=30)
entry.pack(pady=5)

button = tk.Button(root, text="Check Strength", command=check_password)
button.pack(pady=10)

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Arial", 12))
result_label.pack(pady=10)

# Run app
root.mainloop()