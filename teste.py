import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

# Funções gerais
def salvar_usuario(nome, senha):
    """Salvar o novo usuário no arquivo usuarios.txt."""
    with open("usuarios.txt", "a") as arquivo:
        arquivo.write(f"{nome},{senha}\n")

def verificar_usuario(nome, senha):
    """Verificar se o usuário e senha estão no arquivo."""
    if not os.path.exists("usuarios.txt"):
        return False
    with open("usuarios.txt", "r") as arquivo:
        usuarios = [linha.strip().split(",") for linha in arquivo.readlines()]
    for usuario, user_senha in usuarios:
        if usuario == nome and user_senha == senha:
            return True
    return False

def criar_conta():
    """Exibir tela para criar conta."""
    login_frame.pack_forget()
    criar_conta_frame.pack(fill="both", expand=True)

def voltar_para_login():
    """Voltar para a tela de login."""
    criar_conta_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)

def registrar_usuario():
    """Registrar o usuário e salvar no sistema."""
    nome = novo_username_entry.get()
    senha = nova_password_entry.get()
    confirmar_senha = confirmar_password_entry.get()

    if not nome or not senha:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
        return

    if senha != confirmar_senha:
        messagebox.showerror("Erro", "As senhas não coincidem!")
        return

    salvar_usuario(nome, senha)
    messagebox.showinfo("Sucesso", "Conta criada com sucesso!")
    voltar_para_login()

def fazer_login():
    """Fazer login com os dados inseridos."""
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "admin123":
        abrir_pagina_principal("Administrador")
    elif verificar_usuario(username, password):
        abrir_pagina_principal("Utilizador")
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")

def abrir_pagina_principal(usuario_tipo):
    """Abrir a página principal do sistema."""
    login_frame.pack_forget()
    principal_frame.pack(fill="both", expand=True)

    if usuario_tipo == "Administrador":
        messagebox.showinfo("Bem-vindo", "Você entrou como Administrador.")
    else:
        messagebox.showinfo("Bem-vindo", "Você entrou como Utilizador.")

def sair_do_sistema():
    """Encerrar o sistema."""
    root.destroy()

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
    logo_img = Image.open("7flix.png")
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

# Entrada de senha
password_label = tk.Label(login_frame, text="Senha:", font=("Helvetica", 16), fg="white", bg="black")
password_label.pack(pady=5)
password_entry = tk.Entry(login_frame, font=("Helvetica", 14), show="*")
password_entry.pack(pady=5)

# Botão de login
login_button = tk.Button(login_frame, text="Entrar", font=("Helvetica", 16), bg="red", fg="white", command=fazer_login)
login_button.pack(pady=10)

# Botão para criar conta
criar_conta_button = tk.Button(login_frame, text="Criar Conta", font=("Helvetica", 14), bg="gray", fg="white", command=criar_conta)
criar_conta_button.pack(pady=5)

# ----- Tela Criar Conta -----
criar_conta_frame = tk.Frame(root, bg="black")

# Título da tela
novo_titulo = tk.Label(criar_conta_frame, text="Criar Conta", font=("Helvetica", 24, "bold"), fg="white", bg="black")
novo_titulo.pack(pady=20)

# Entradas para criar conta
novo_username_label = tk.Label(criar_conta_frame, text="Novo Usuário:", font=("Helvetica", 16), fg="white", bg="black")
novo_username_label.pack(pady=5)
novo_username_entry = tk.Entry(criar_conta_frame, font=("Helvetica", 14))
novo_username_entry.pack(pady=5)

nova_password_label = tk.Label(criar_conta_frame, text="Senha:", font=("Helvetica", 16), fg="white", bg="black")
nova_password_label.pack(pady=5)
nova_password_entry = tk.Entry(criar_conta_frame, font=("Helvetica", 14), show="*")
nova_password_entry.pack(pady=5)

confirmar_password_label = tk.Label(criar_conta_frame, text="Confirmar Senha:", font=("Helvetica", 16), fg="white", bg="black")
confirmar_password_label.pack(pady=5)
confirmar_password_entry = tk.Entry(criar_conta_frame, font=("Helvetica", 14), show="*")
confirmar_password_entry.pack(pady=5)

registrar_button = tk.Button(criar_conta_frame, text="Registrar", font=("Helvetica", 16), bg="red", fg="white", command=registrar_usuario)
registrar_button.pack(pady=10)

voltar_button = tk.Button(criar_conta_frame, text="Voltar", font=("Helvetica", 14), bg="gray", fg="white", command=voltar_para_login)
voltar_button.pack(pady=5)

# ----- Tela Principal -----
principal_frame = tk.Frame(root, bg="black")

titulo_principal = tk.Label(principal_frame, text="7FLIX", font=("Helvetica", 28, "bold"), fg="red", bg="black", pady=20)
titulo_principal.pack(fill="x")

# Conteúdo da interface (exemplo das categorias)
main_frame = tk.Frame(principal_frame, bg="black")
main_frame.pack(fill="both", expand=True)

scrollbar = ttk.Scrollbar(main_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

canvas = tk.Canvas(main_frame, bg="black", yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.config(command=canvas.yview)

content_frame = tk.Frame(canvas, bg="black")
canvas.create_window((0, 0), window=content_frame, anchor="nw")

categorias = ["Ação", "Comédia", "Drama", "Ficção Científica", "Terror"]
for categoria in categorias:
    cat_label = tk.Label(content_frame, text=categoria, font=("Helvetica", 20, "bold"), fg="white", bg="black", anchor="w", pady=10)
    cat_label.pack(fill="x", padx=10)
    cat_frame = tk.Frame(content_frame, bg="black")
    cat_frame.pack(fill="x", pady=5)
    for i in range(5):
        filme_button = tk.Button(cat_frame, text=f"Filme {i+1}", width=15, height=3, bg="grey", fg="white")
        filme_button.pack(side="left", padx=5)

# Atualizando o canvas
content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Botão para sair
sair_button = tk.Button(principal_frame, text="Sair", font=("Helvetica", 14), bg="red", fg="white", command=sair_do_sistema)
sair_button.pack(side="bottom", pady=10)

# Executando a aplicação
root.mainloop()


