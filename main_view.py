import tkinter as tk
from tkinter import filedialog
import os

def open_file():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    file_dialog = filedialog.askopenfilename(initialdir=script_directory)
    if file_dialog:
        run_selected_script(file_dialog)
        if file_dialog not in opened_files_listbox.get(0, tk.END):
            opened_files_listbox.insert(tk.END, file_dialog)
            limit_recent_files()
            save_recent_files()
            

def run_selected_script(selected_file):
    try:
        with open(selected_file, 'r') as script_file:
            script_content = script_file.read()
        exec(script_content)
    except Exception as e:
        print(f"Error running script: {e}")

def run_script(event):
    selected_file = opened_files_listbox.get(opened_files_listbox.curselection())
    if selected_file:
        run_selected_script(selected_file)

def limit_recent_files():
    file_paths = opened_files_listbox.get(0, tk.END)
    recent_file_paths = list(set(file_paths))[-5:]
    opened_files_listbox.delete(0, tk.END)
    for path in recent_file_paths:
        opened_files_listbox.insert(tk.END, path)

def save_recent_files():
    file_paths = opened_files_listbox.get(0, tk.END)
    with open("recent_files.txt", "w") as file:
        for path in file_paths:
            file.write(path + "\n")

root = tk.Tk()
root.title("File Opener")
root.geometry("1200x600")  # Set the window size to 1200x600

# create a menubar
menubar = tk.Menu(root)
root.config(menu=menubar)

# create the file_menu
file_menu = tk.Menu(
    menubar,
    tearoff=0
)

# add menu items to the File menu
file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
file_menu.add_command(label='Close')
file_menu.add_separator()

# add Exit menu item
file_menu.add_command(
    label='Exit',
    command=root.destroy
)

# add the File menu to the menubar
menubar.add_cascade(
    label="File",
    menu=file_menu
)
# create the Help menu
help_menu = tk.Menu(
    menubar,
    tearoff=0
)

help_menu.add_command(label='Welcome')
help_menu.add_command(label='About...')

# add the Help menu to the menubar
menubar.add_cascade(
    label="Help",
    menu=help_menu
)


open_button = tk.Button(root, text="Open File in Script Directory", command=open_file)
open_button.pack(side=tk.LEFT, padx=20)

opened_files_listbox = tk.Listbox(root)
opened_files_listbox.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True,padx=10, pady=10)

opened_files_listbox.bind("<Double-Button-1>", run_script)

if os.path.exists("recent_files.txt"):
    with open("recent_files.txt", "r") as file:
        recent_file_paths = [line.strip() for line in file.readlines()]
        for path in recent_file_paths:
            if path not in opened_files_listbox.get(0, tk.END):
                opened_files_listbox.insert(tk.END, path)

root.mainloop()

