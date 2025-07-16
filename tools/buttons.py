import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename


def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[(
        "Text files", "*.txt"), ("Markdown files", "*.md")])
    if not filepath:
        return

    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open File: {filepath}")


def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[(
        "Text files", "*.txt"), ("Markdown files", "*.md")])
    if not filepath:
        return

    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Save File: {filepath}")
