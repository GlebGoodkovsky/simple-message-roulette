# 🎰 Simple Message Roulette

A clean, modern, and fun desktop app that gives you a random motivational message with an emoji every time you hit **Spin**.  
Built with [Electron](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.electronjs.org%2F) (for the desktop UI) and [Python](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.python.org%2F) (for the message logic), this project is a practical demonstration of combining different technologies—and learning by building.

---

- **Why Electron & Python?**
    - Electron is the go-to for modern, cross-platform desktop UIs using web tech (HTML, CSS, JS)[1][6].
    - Python is beloved for its simplicity and power, especially for logic and AI/automation tasks.
- **How AI Helped:**
    
    - I used AI (LLMs, code assistants, and search tools) to help scaffold the architecture, solve hurdles, debug code, and refine explanations.
    - The process included asking AI why certain tech (like child_process, python-shell, and Electron's security model) works as it does, not just mindlessly copying code.
- **Outcome:**
    - The app’s design, code, and this README were all produced as part of a hands-on learning process with AI as a partner—accelerating both implementation and deeper conceptual understanding.

---

## ✨ Features

- **Simple UI:** Clean, distraction-free interface with a single fun purpose.
- **Native Desktop:** Runs anywhere—Windows, Linux, macOS (with Node.js and Python 3).
- **Random Messages & Emojis:** Each click gives you a new surprise.
- **Python-Powered Logic:** The message/emoji combo comes from a Python script—a perfect starter for connecting "backend" logic to frontend.
- **Easy to Modify:** Want to use your own quotes and emoji? Just edit a single Python file and restart.
- **No Internet Required:** 100% local; nothing goes online.
- **Simple Stack:** HTML + CSS + JS + Python — no frameworks or build tools required.
- **No LocalStorage / DB:** No storage — each click is a new message.

---

## 🛠️ Tech Stack

The project leverages a straightforward yet effective tech stack:

- **UI Layer:** Built using standard **HTML** for structure and **CSS** for styling, ensuring a clean and modern look. 
- **Frontend Logic:** **JavaScript** within renderer.js handles user interactions and communication.
- **Backend Logic:** A **Python 3** script (spin.py) generates the random messages and emojis.
- **Inter-Process Communication:** Node.js's child_process API is used by renderer.js to execute the Python script.
- **Desktop Application Shell:** **Electron** provides the framework for creating the cross-platform desktop application.

---

## 🚀 How to Run

### ⬇️ 1. Clone This Repo

```bash
git clone https://github.com/GlebGoodkovsky/simple-message-roulette.git
cd simple-message-roulette/my-electron-app
```

### 📦 2. Install Dependencies

```bash
npm install
```

> Requires [Node.js](https://www.google.com/url?sa=E&q=https%3A%2F%2Fnodejs.org%2F) and [Python 3](https://www.google.com/url?sa=E&q=https%3A%2F%2Fwww.python.org%2F) to be installed.

### ▶️ 3. Launch the App

```bash
npm start
```

### 4. The app window will open. Click "Spin" and enjoy a rotating series of fun messages.

---

## 🎛 How It Works

- The **app window** is rendered by Electron with HTML/CSS for the interface.
    
- When you click **Spin**, renderer.js launches spin.py using Node's child process system.
    
- The Python script picks a random quote and emoji, and prints it.
    
- The app instantly updates with the new message from Python.
    

---

## 🐍 Customize Your Messages

Want to make it your own?  
Edit the lists at the top of spin.py—add, remove, or change messages and emojis, save, then restart the app!

Generated python

```python
# spin.py

import random

emojis = ["😁", "🔥", "😎", "🌈", "🚀", "🌀"]
messages = [
"Stay awesome!",
"You rock!",
"Python power!",
"Keep coding!",
"Enjoy your day!",
"You got this!"
]

print(random.choice(messages) + " " + random.choice(emojis))
```

---

## 🧪 Example Output

- “Keep coding! 🚀”
- “You rock! 🌈”
- “Stay awesome! 😎”

Each spin is unique — pull from the list randomly.

---

## 🤝 Contributing & Learning

- Suggestions, bug reports, and learning questions are welcome!
    
- This repo is also a showcase for **learning to code with AI tools**: all stages, from code to documentation, used AI to boost speed, explain concepts, and catch mistakes.
    
- If you're learning or using AI coding partners, feel free to fork and remix for your own experiments.
    

---