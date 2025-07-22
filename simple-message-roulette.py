import tkinter as tk
from PIL import Image, ImageTk
import os
import random

EMOJI_DIR = "emoji_png"
PHRASES = [
    "Stay awesome!",
    "You rock!",
    "Python power!",
    "Coding is fun!",
    "Emojis FTW!",
    "Feeling lucky?",
    "Made you smile!",
    "Keep going!",
    "You got this!",
    "Enjoy your day!"
]

# Gather all PNG emoji files
emoji_files = [os.path.join(EMOJI_DIR, f) for f in os.listdir(EMOJI_DIR) if f.endswith(".png")]

def show_random_emoji_and_message():
    if not emoji_files:
        emoji_label.config(text="No emoji images found!", image=None)
        emoji_label.image = None
        message_label.config(text="")
        return
    emoji_path = random.choice(emoji_files)
    img = Image.open(emoji_path).resize((64, 64))
    tk_img = ImageTk.PhotoImage(img)
    emoji_label.config(image=tk_img, text="")
    emoji_label.image = tk_img

    message = random.choice(PHRASES)
    # Optional: combine with emoji filename for more variety
    # Or generate messages programmatically
    message_label.config(text=message)

root = tk.Tk()
root.title("Emoji Message Roulette")

emoji_label = tk.Label(root, text="Click 'Spin' to begin", font=("Helvetica", 20))
emoji_label.pack(pady=20)

message_label = tk.Label(root, text="", font=("Helvetica", 18))
message_label.pack(pady=10)

btn = tk.Button(root, text="Spin!", command=show_random_emoji_and_message)
btn.pack(pady=10)

root.mainloop()
