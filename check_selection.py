import tkinter as tk
import os
def abc(duplicates):
    def get_selected_values():
        global selected_values
        selected_values = [item for item, var in checkboxes.items() if var.get()]
        print("Selected values:", selected_values)
        root.destroy()
    def create_checkboxes(duplicates):
        for index, path in enumerate(duplicates):
            var = tk.BooleanVar()
            checkboxes[path] = var
            checkbox = tk.Checkbutton(root, text=path, variable=var, font=("Georgia",12))
            checkbox.grid(row=index, column=0, sticky="w")
    root = tk.Tk()
    root.title("Select Files to Delete")
    checkboxes = {}
    create_checkboxes(duplicates)
    select_button = tk.Button(root, text="Select for Deletion", bg="black", fg="white", command=get_selected_values, font=("Georgia",12))
    select_button.grid(row=len(duplicates), column=0, pady=10)
    root.mainloop()
    if selected_values:
        print(selected_values)
        for i in selected_values:
            os.remove(i)
            print("Deleted File at path:",i)