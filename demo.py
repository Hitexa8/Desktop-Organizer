import tkinter as tk

def function1():
    print("Button 1 clicked")

def function2():
    print("Button 2 clicked")

root = tk.Tk()
root.title("Buttons Example")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

button1 = tk.Button(frame, text="Button 1", command=function1, width=20)
button1.pack(side=tk.LEFT, padx=10)

button2 = tk.Button(frame, text="Button 2", command=function2, width=20)
button2.pack(side=tk.RIGHT, padx=10)

root.mainloop()
