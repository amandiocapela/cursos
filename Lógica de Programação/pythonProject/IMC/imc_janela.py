import tkinter
from tkinter import Button, Entry, Label, messagebox, PhotoImage
import imc_modulo as imc

def acao():
    print("Botão Pressionado")
    indice = imc.calcula_imc(peso=peso.get(), altura=altura.get())
    classificacao = imc.classifica_imc(indice)
    msg = messagebox.showinfo("Classificação IMC", classificacao)

principal = tkinter.Tk()
# Código da interface aqui.

# Logo
#imagem = PhotoImage(file="logo.jpg")
#logo = Label(principal, imagem=imagem)
#logo.image = imagem
#logo.grid(row=0, column=0, rowspan=2)

# Etiqueta e caisa de entrada de Altura
etiqueta_altura = Label(principal, text="Altura: ")
etiqueta_altura.grid(row=0, column=1)

altura = Entry(principal)
altura.grid(row=0, column=2)

# Etiqueta e caisa de entrada de Peso
etiqueta_peso = Label(principal, text="Peso: ")
etiqueta_peso.grid(row=1, column=1)

peso = Entry(principal)
peso.grid(row=1, column=2)

# Botão para Calcular
botao = Button(principal, text="Calcular", command=acao)
botao.grid(row=2, column=2)

principal.mainloop()