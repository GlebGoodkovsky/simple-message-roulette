import tkinter as tk
from tkinter import messagebox
import random
from datetime import datetime

def generate_random_messages(num):
    phrases = ["message{}".format(i) for i in range(1, 11)]
    emojis = ["🔴", "🟠", "🟡", "🟢", "🔵"]
    if not phrases or not emojis:
        messagebox.showerror("Error", "No phrases or emojis to generate")
        return
    for _ in range(num):
        phrase = random.choice(phrases)
        emoji = random.choice(emojis)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"{phrase} {timestamp}: {emoji}")

def run():
    try:
        num_phrases = int(num_entry.get())
        if num_phrases < 1:
            raise ValueError
        generate_random_messages(num_phrases)
    except ValueError:
        messagebox.showerror("Input error", "Please enter a positive integer.")

root = tk.Tk()
root.title("Message Generator")
frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

label = tk.Label(frame, text="Number of Messages:")
label.grid(row=0, column=0)
num_entry = tk.Entry(frame)
num_entry.grid(row=0, column=1)

run_button = tk.Button(frame, text="Run", command=run)
run_button.grid(row=1, column=0, columnspan=2, pady=5)

root.mainloop()
