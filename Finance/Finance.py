from tkinter import *

def oi():
    oi = ("kkkkkkk, muito gay")
    resp["text"] = oi

janela = Tk()
janela.title("TESTE LGBT")
janela.geometry("300x200")
janela.config(bg='#DA70D6 ')
textoincial = Label(janela, text=("Clica no botão se você é gay"), bg="pink", fg="black")
textoincial.grid (column=0, row=0, padx=10, pady=10)

texto2 = Label(janela, text=("Esse botão aqui!"), bg="pink", fg="black")
texto2.grid (column=0,row=1, padx=10, pady=10)

botao = Button(janela, text="Vai clicar mesmo?", bg="pink", fg="black",command=oi)
botao.grid(column=0,row=2, padx=10, pady=10)

resp= Label(janela, text="",bg="pink", fg="black")
resp.grid (column=0,row=3, padx=10, pady=10)

janela.mainloop()