from random import uniform
from tkinter import (
    Label,
    Button,
    Tk,
    messagebox, 
)

tituloMensagemErro = "trololo"
mensagemErro = "Vai ter que ir no botão sim XD"
tituloBotaoSim = "Você aceitou"
mensagemBotaoSim = "Agora somos namorados"
texto = "Quer namorar comigo?"

def _():
    pass
    
def close_window():
    messagebox.showerror(tituloMensagemErro, mensagemErro)

def chance_pos(event=None):
    numx = uniform(0.05, 0.90)
    numy = uniform(0.1, 0.90)
    button2.place(relx=str(numx),rely=str(numy))

def trolei():
    messagebox.showinfo(tituloBotaoSim, mensagemBotaoSim)
    root.destroy()


root = Tk()
root.geometry('700x400+550+250')
root.protocol("WM_DELETE_WINDOW", close_window)

label1 = Label(root, text=texto, font=("Helvetica", 16))
button1 = Button(text="Sim", command=trolei, height=2, width=10)
button2 = Button(text="Nâo", command=_, height=2, width=10)
button2.bind("<Enter><Motion>", chance_pos)
button2.bind("<Button-1>", lambda _: "break", add=True)


label1.place(relx='0.34',rely='0.08')
button1.place(relx='0.22',rely='0.68')
button2.place(relx='0.62',rely='0.68')


if __name__ == "__main__":
    root.mainloop()
