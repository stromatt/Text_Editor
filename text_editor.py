import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Color scheme
# coolors.co/palette/0d1b2a-1b263b-....n
bgcolor1 = "#0D1B2A"
bgcolor2 = "#1B263B"
bgcolor3 = "#415A77"
bgcolor4 = "#778DA9"
bgcolor5 = "#E0E1DD"

content_undo = []
count = 0


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
    window.configure(bg=bgcolor1)

    text_edit = tk.Text(
        window, font="Helvetica 18", bg=bgcolor2, fg=bgcolor5)
    text_edit.pack(pady=40, padx=20, fill="both", expand=True)
#    text_edit.pack(fill=tk.BOTH, expand=True)

    frame = tk.Frame(
        window, relief=tk.RAISED, bd=2, bg=bgcolor4)
    save_button = tk.Button(
        frame, text="Save", command=lambda: save_file(window, text_edit),
        bg=bgcolor3, fg=bgcolor5, highlightbackground=bgcolor1)
    open_button = tk.Button(
        frame, text="Open", command=lambda: open_file(window, text_edit),
        bg=bgcolor3, fg=bgcolor5, highlightbackground=bgcolor1)
    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, sticky="ew")
    frame.pack(pady=40, padx=20, anchor="nw", before=text_edit, side="left")

    def select_all(event):
        text_edit.tag_add(tk.SEL, "1.0", tk.END)
        text_edit.mark_set(tk.INSERT, "1.0")
        text_edit.see(tk.INSERT)
        return 'break'

    undo_len = 10

    def undo_tree(window, text_edit, count):
        if len(content_undo) < undo_len:
            content_undo.append(text_edit.get(1.0, tk.END))
        else:
            j = 1
            for i in range(undo_len):
                print(content_undo[i])
                content_undo[i] = content_undo[j]
                if j < len(content_undo)-1:
                    j += 1
            content_undo[len(content_undo)-1] = text_edit.get(1.0, tk.END)
            count = len(content_undo)-1
            print(count)
            return count

    def undo(window, text_edit, conent_undo, count):
        print(count)
        count += -2
        print(count)
        count = len(content_undo) - 2
        print(count)
        if count == 0:
            return "break"
        text_edit.delete(1.0, tk.END)
#        content = content_undo[count].read()
        text_edit.insert(tk.END, content_undo[count])

    def undo_return(window, text_edit, conent_undo, count):
        count = len(content_undo) - 1
        print(count)
        if count == 0:
            return "break"
        text_edit.delete(1.0, tk.END)
#        content = content_undo[count].read()
        text_edit.insert(tk.END, content_undo[count])

    def key_handler(event):
        print(event.char, event.keysym, event.keycode)
        # 37 ctrl
        # 133 super
        # 64 alt
        # 50 shift
        if event.keycode != 37 and\
                event.keycode != 133 and\
                event.keycode != 64 and\
                event.keycode != 50:
            undo_tree(window, text_edit, count)
            return count

    window.bind("<Key>", key_handler)

    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))
    window.bind("<Control-Key-a>", select_all)
    window.bind("<Control-Key-A>", select_all)
    window.bind("<Control-z>", lambda x: undo(window,
                text_edit, content_undo, count))
    window.bind("<Control-r>", lambda x: undo_return(window,
                text_edit, content_undo, count))
#    window.bind("<KeyPress>", lambda x: undo_tree(window, text_edit))

    window.mainloop()


main()
