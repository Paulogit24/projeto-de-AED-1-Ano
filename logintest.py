"""users.py

Métodos relacionados com os utilizadores

Criar conta, autenticação, validação password,...
"""
import customtkinter
import datetime
import CTkMessagebox
from  PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os



Fusers=".\\contas/utilizadore.txt"

def lerUsers(): #Lê o ficheiro de utilizadores.txt
    fileUsers=open(Fusers, "r", encoding="utf-8")
    listaUsers= fileUsers.readlines()
    fileUsers.close()
    return listaUsers

def validaConta (userName, userPass): #Validar autenticação com uma conta: LOGIN
    listausers = lerUsers()
    for linha in listausers:

        if linha.split(";")[0]== userName and linha.split(";") [1] == userPass:
            msg = "Bem-vindo" + userName
            return msg
    msg = "O UserName ou a Password estão incorretos!"
    #CTkMessagebox.showerror("error", msg)
    return msg

def criaconta(userName, userPass, userPassConfirm):   #Criar uma nova conta de utilizador

    if userName == "" or userPass == "":
        msg = "O username e a password não podem ser vazios!"
        return False, msg

    if userPass != userPassConfirm:
        msg ="A password não coincide com a sua confirmação!"
        return False, msg
    listaUsers =lerUsers()
    for linha in listaUsers:
        fields = linha.split(";")
        if fields[0] == userName:
            msg = "Já existe um utilizador com esse username!"
            return False, msg
    
    # acrescenta user ao ficheiro
    fileUsers =open(Fusers, "a")
    linha =userName + ";" + userPass + ";" + "user"+ "\n"
    fileUsers.write(linha)
    fileUsers.close()
    msg = "Conta criada com sucesso!"
    return True, msg

# Configuração da janela principal
root = tk.Tk()
root.title("7FLIX")
root.geometry("1024x768")
root.configure(bg="black")

# ----- Tela de Login -----
login_frame = tk.Frame(root, bg="black")
login_frame.pack(fill="both", expand=True)

# Carregar e exibir o logo
try:
    logo_img = Image.open("7fliX.png")
    logo_img = logo_img.resize((200, 100), Image.ANTIALIAS)
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(login_frame, image=logo_photo, bg="black")
    logo_label.pack(pady=20)
except FileNotFoundError:
    tk.Label(login_frame, text="7FLIX", font=("Helvetica", 28, "bold"), fg="red", bg="black").pack(pady=20)

# Título da tela
titulo = tk.Label(login_frame, text="Login", font=("Helvetica", 24, "bold"), fg="white", bg="black")
titulo.pack(pady=20)

# Entrada de usuário
username_label = tk.Label(login_frame, text="Usuário:", font=("Helvetica", 16), fg="white", bg="black")
username_label.pack(pady=5)
username_entry = tk.Entry(login_frame, font=("Helvetica", 14))
username_entry.pack(pady=5)
username=username_entry.get()
# Entrada de senha
password_label = tk.Label(login_frame, text="Senha:", font=("Helvetica", 16), fg="white", bg="black")
password_label.pack(pady=5)
password_entry = tk.Entry(login_frame, font=("Helvetica", 14), show="*")
password_entry.pack(pady=5)
password= password_entry.get()

# Botão de login
login_button = tk.Button(login_frame, text="Entrar", font=("Helvetica", 16), bg="red", fg="white", command=validaConta(username,password))
login_button.pack(pady=10)

# Botão para criar conta
criar_conta_button = tk.Button(login_frame, text="Criar Conta", font=("Helvetica", 14), bg="gray", fg="white", command=criaconta)
criar_conta_button.pack(pady=5)

root.mainloop()