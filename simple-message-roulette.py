import tkinter as tk
from PIL import Image, ImageTk
import os
import random
import sys

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

def preload_images(emoji_dir, size=(64, 64)):
    """Load and resize all PNGs, return as list of (filename, ImageTk.PhotoImage) tuples."""
    if not os.path.isdir(emoji_dir):
        return []
    images = []
    for fname in os.listdir(emoji_dir):
        if fname.lower().endswith(".png"):
            try:
                img_path = os.path.join(emoji_dir, fname)
                img = Image.open(img_path).resize(size)
                tk_img = ImageTk.PhotoImage(img)
                images.append((fname, tk_img))
            except Exception as e:
                print(f"Error loading {fname}: {e}", file=sys.stderr)
    return images

# --- GUI setup ---
root = tk.Tk()
root.title("Emoji Message Roulette")

# Preload images (resized and cached)
emoji_images = preload_images(EMOJI_DIR)

emoji_label = tk.Label(root, font=("Helvetica", 20))
emoji_label.pack(pady=20)

message_label = tk.Label(root, text="", font=("Helvetica", 18))
message_label.pack(pady=10)

def show_random_emoji_and_message():
    if not emoji_images:
        emoji_label.config(text="No emoji images found!", image=None)
        emoji_label.image = None
        message_label.config(text="Please add PNGs to emoji_png.")
        return
    fname, tk_img = random.choice(emoji_images)
    emoji_label.config(image=tk_img, text="")
    emoji_label.image = tk_img  # keep a reference
    message = random.choice(PHRASES)
    message_label.config(text=message)

btn = tk.Button(root, text="Spin!", command=show_random_emoji_and_message)
btn.pack(pady=10)

# Show warning at startup if emoji folder/images missing
if not emoji_images:
    emoji_label.config(text="No emoji images found!", image=None)
    message_label.config(text="Add PNGs to emoji_png to play.")
    btn.config(state="disabled")
else:
    show_random_emoji_and_message()

root.mainloop()
