import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def on_open():
    messagebox.showinfo("Action", "Open clicked!")

def on_settings():
    messagebox.showinfo("Action", "Settings clicked!")

def on_about():
    messagebox.showinfo("About", "This is a demo app like Calibre.")

# Crée la fenêtre principale
root = tk.Tk()
root.title("Scenet")
root.geometry("800x600")

# Barre de menu
menu_bar = tk.Menu(root)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=on_open)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=on_about)
menu_bar.add_cascade(label="Help", menu=help_menu)

root.config(menu=menu_bar)

# Barre d'outils
toolbar = tk.Frame(root, bd=1, relief=tk.RAISED)
open_btn = tk.Button(toolbar, text="Open", command=on_open)
open_btn.pack(side=tk.LEFT, padx=2, pady=2)

settings_btn = tk.Button(toolbar, text="Settings", command=on_settings)
settings_btn.pack(side=tk.LEFT, padx=2, pady=2)

toolbar.pack(side=tk.TOP, fill=tk.X)

# Section principale : Treeview + Preview
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=True)

# Liste (Treeview) à gauche
tree_frame = tk.Frame(main_frame)
tree_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

tree = ttk.Treeview(tree_frame, columns=("Title", "Author", "Year"), show="headings")
tree.heading("Title", text="Title")
tree.heading("Author", text="Author")
tree.heading("Year", text="Year")
tree.pack(fill=tk.BOTH, expand=True)

# Ajouter des exemples d'éléments à la liste
sample_data = [
    ("Book 1", "Author A", "2020"),
    ("Book 2", "Author B", "2021"),
    ("Book 3", "Author C", "2019"),
]
for item in sample_data:
    tree.insert("", tk.END, values=item)

# Aperçu à droite
preview_frame = tk.Frame(main_frame, width=200, relief=tk.SUNKEN, bd=1)
preview_frame.pack(side=tk.RIGHT, fill=tk.Y)

preview_label = tk.Label(preview_frame, text="Preview", font=("Arial", 16))
preview_label.pack(pady=10)

preview_content = tk.Label(preview_frame, text="Select a book to preview details.", wraplength=180, justify=tk.LEFT)
preview_content.pack(padx=10, pady=10)

# Fonction pour afficher les détails dans le panneau de prévisualisation
def show_preview(event):
    selected_item = tree.focus()
    if selected_item:
        values = tree.item(selected_item, "values")
        preview_content.config(text=f"Title: {values[0]}\nAuthor: {values[1]}\nYear: {values[2]}")

tree.bind("<<TreeviewSelect>>", show_preview)

# Lance la boucle principale
root.mainloop()
