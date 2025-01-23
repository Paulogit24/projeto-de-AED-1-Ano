import tkinter as tk
from tkinter import Toplevel, PhotoImage

def abrir_nova_janela():
    nova_janela = Toplevel(root)
    nova_janela.title("Nova Janela")

    # Definir ícone para nova janela (funciona em Windows, Linux e macOS)
    icone = PhotoImage(file="/Users/miguelbasso/Downloads/png-transparent-logo-computer-icons-ico-miscellaneous-circle-symbol.png")  # Usando PNG
    nova_janela.iconphoto(True, icone)

    # Definir um rótulo na nova janela
    tk.Label(nova_janela, text="Esta é uma nova janela!").pack(pady=20)

# Criando janela principal
root = tk.Tk()
root.title("Janela Principal")

# Definir ícone para janela principal
icone_principal = PhotoImage(file="/Users/miguelbasso/Downloads/png-transparent-logo-computer-icons-ico-miscellaneous-circle-symbol.png")
root.iconphoto(True, icone_principal)

# Botão para abrir nova janela
btn_abrir = tk.Button(root, text="Abrir Nova Janela", command=abrir_nova_janela)
btn_abrir.pack(pady=20)

root.mainloop()