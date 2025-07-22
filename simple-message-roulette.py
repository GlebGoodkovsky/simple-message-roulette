import tkinter as tk
from PIL import Image, ImageTk
import os
import random

# Path to your downloaded emoji PNG folder
EMOJI_DIR = "emoji_png"

# Get all PNG files in that directory
emoji_files = [os.path.join(EMOJI_DIR, f) for f in os.listdir(EMOJI_DIR) if f.endswith(".png")]

def show_random_emoji():
    if not emoji_files:
        emoji_label.config(text="No emoji images found!")
        emoji_label.image = None
        return
    emoji_path = random.choice(emoji_files)
    img = Image.open(emoji_path).resize((64, 64))
    tk_img = ImageTk.PhotoImage(img)
    emoji_label.config(image=tk_img, text="")  # Remove any text
    emoji_label.image = tk_img  # Keep a reference so it isn't garbage collected

root = tk.Tk()
root.title("Emoji Image Viewer")

emoji_label = tk.Label(root, text="Click 'Show Emoji' to start", font=("Helvetica", 20))
emoji_label.pack(pady=20)

btn = tk.Button(root, text="Show Random Emoji", command=show_random_emoji)
btn.pack(pady=10)

root.mainloop()
