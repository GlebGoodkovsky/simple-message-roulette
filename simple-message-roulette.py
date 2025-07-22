import tkinter as tk
from tkinter import scrolledtext
import random
from datetime import datetime

def generate_random_messages(num):
    phrases = [f"message{i}" for i in range(1, 11)]
    emojis = ["🔴", "🟠", "🟡", "🟢", "🔵"]
    output_box.delete(1.0, tk.END)  # Clear previous output

    for _ in range(num):
        phrase = random.choice(phrases)
        emoji = random.choice(emojis)
        timestamp = datetime.now().strftime("%H:%M:%S")
        result = f"{phrase} {timestamp}: {emoji}\n"
        output_box.insert(tk.END, result)

def run():
    try:
        count = int(entry.get())
        if count < 1:
            raise ValueError
        generate_random_messages(count)
    except ValueError:
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, "❌ Please enter a valid positive number.\n")

# Create main window
root = tk.Tk()
root.title("Simple Message Generator")

# Input area
entry_frame = tk.Frame(root)
entry_frame.pack(pady=10)

tk.Label(entry_frame, text="Number of Messages:").pack(side=tk.LEFT, padx=5)
entry = tk.Entry(entry_frame, width=5)
entry.pack(side=tk.LEFT)

tk.Button(entry_frame, text="Generate", command=run).pack(side=tk.LEFT, padx=5)

# Output area
output_box = scrolledtext.ScrolledText(root, width=40, height=10, wrap=tk.WORD)
output_box.pack(padx=10, pady=10)

# Start GUI loop
root.mainloop()
