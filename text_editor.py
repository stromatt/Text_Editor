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


def main():
    window = tk.Tk()
    window.title("Text editor")

    # getting screen width and height of display
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    # setting tkinter window size
    window.geometry("%dx%d" % (width, height))
    window.configure(bg="black")

    text_edit = tk.Text(
        window, font="Helvetica 18", bg="#303446")
    text_edit.pack(pady=40, padx=20, fill="both", expand=True)
#    text_edit.pack(fill=tk.BOTH, expand=True)

    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    save_button = tk.Button(
        frame, text="Save", command=lambda: save_file(window, text_edit),
        bg="#303446", fg="white")
    open_button = tk.Button(
        frame, text="Open", command=lambda: open_file(window, text_edit),
        bg="#303446", fg="white")
    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, sticky="ew")
    frame.pack(pady=40, padx=20, anchor="nw", before=text_edit, side="left")

    def select_all(event):
        text_edit.tag_add(tk.SEL, "1.0", tk.END)
        text_edit.mark_set(tk.INSERT, "1.0")
        text_edit.see(tk.INSERT)
        return 'break'

    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))
    window.bind("<Control-Key-a>", select_all)
    window.bind("<Control-Key-A>", select_all)
    window.mainloop()


main()
