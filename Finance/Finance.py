import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox

root = tk.Tk()
root.title("Tu é?")
root.geometry("600x600")
root.configure(background="pink")

def move_button_1(e):
    if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 40:
        x = random.randint(0, root.winfo_width() - button_1.winfo_width())
        y = random.randint(0, root.winfo_height() - button_1.winfo_height())
        button_1.place(x=x, y=y)

def accepted():
    messagebox.showinfo("KKKKKK VIADINHO")

def denied():
    button_1.destroy()

margin = Canvas(root, width=500, bg="pink", height=100,
                bd=0, highlightthickness=0, relief='ridge')
margin.pack()
text_id = Label(root, bg="pink", text='Você é gay?',fg='#590d22', font=('Montserrat', 24, 'bold'))
text_id.pack()
button_1 = tk.Button(root, text="Não", bg="pink", command=denied, relief=RIDGE, bd=3, font=('Montserrat', 8, 'bold'))
button_1.pack()
root.bind('<Motion>', move_button_1)
button_2 = tk.Button(root, text="Sim", bg="pink", relief=RIDGE, bd=3, command=accepted, font=("Montserrat", 14, 'bold'))
button_2.pack()

root.mainloop()