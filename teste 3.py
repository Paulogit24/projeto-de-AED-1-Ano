import tkinter as tk
from tkinter import ttk, messagebox
import json
import os

# Caminho do arquivo onde os dados serão armazenados
ARQUIVO_USUARIOS = "usuarios.json"

def carregar_usuarios():
    """Carrega os usuários do arquivo JSON."""
    if os.path.exists(ARQUIVO_USUARIOS):
        with open(ARQUIVO_USUARIOS, "r") as arquivo:
            return json.load(arquivo)
    return {}

def salvar_usuarios(usuarios):
    """Salva os usuários no arquivo JSON."""
    with open(ARQUIVO_USUARIOS, "w") as arquivo:
        json.dump(usuarios, arquivo)

# Funções de lógica
def fazer_login():
    """Processa o login do usuário."""
    usuario = login_usuario_entry.get()
    senha = login_senha_entry.get()

    if usuario in usuarios and usuarios[usuario] == senha:
        messagebox.showinfo("Login", f"Bem-vindo, {usuario}!")
        mostrar_pagina_principal()
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")

def criar_conta():
    """Cria uma nova conta."""
    usuario = criar_usuario_entry.get()
    senha = criar_senha_entry.get()

    if not usuario or not senha:
        messagebox.showerror("Erro", "Preencha todos os campos!")
        return

    if usuario in usuarios:
        messagebox.showerror("Erro", "Usuário já existe!")
    else:
        usuarios[usuario] = senha
        salvar_usuarios(usuarios)
        messagebox.showinfo("Sucesso", "Conta criada com sucesso!")
        mostrar_login()

# Funções de troca de telas
def mostrar_login():
    """Exibe a tela de login."""
    criar_frame.pack_forget()
    login_frame.pack()
    janela.update()  # Força a atualização imediata da janela

def mostrar_criar_conta():
    """Exibe a tela de criação de conta."""
    login_frame.pack_forget()
    criar_frame.pack()
    janela.update()  # Força a atualização imediata da janela

# Função para redefinir o estilo do ttk
def redefinir_estilo():
    estilo = ttk.Style()

    # Aplicando o tema "clam"
    estilo.theme_use('clam')

    # Configurando o estilo do botão
    estilo.configure("TButton",
                     background="red",    # Cor de fundo
                     foreground="white",  # Cor do texto
                     borderwidth=2,       # Largura da borda
                     relief="solid")      # Estilo da borda

# Carrega os usuários ao iniciar
usuarios = carregar_usuarios()

# Configuração da interface gráfica
janela = tk.Tk()
janela.title("Sistema de Login")
janela.geometry("300x250")
janela.configure(bg="black")

# Redefinir estilo do ttk e aplicar o tema "clam"
redefinir_estilo()

# Frame de Login
login_frame = tk.Frame(janela, bg="black")

login_label = tk.Label(login_frame, text="Login", font=("Arial", 16), bg="black", fg="white")
login_label.pack(pady=10)

login_usuario_label = tk.Label(login_frame, text="Usuário:", bg="black", fg="white")
login_usuario_label.pack()
login_usuario_entry = tk.Entry(login_frame)
login_usuario_entry.pack(pady=5)

login_senha_label = tk.Label(login_frame, text="Senha:", bg="black", fg="white")
login_senha_label.pack()
login_senha_entry = tk.Entry(login_frame, show="*")
login_senha_entry.pack(pady=5)

# Usando o botão do ttk com o estilo redefinido
login_btn = ttk.Button(login_frame, text="Fazer Login", command=fazer_login)
login_btn.pack(pady=10)

criar_conta_btn = ttk.Button(login_frame, text="Criar Conta", command=mostrar_criar_conta)
criar_conta_btn.pack(pady=5)

# Frame de Criação de Conta
criar_frame = tk.Frame(janela, bg="black")

criar_label = tk.Label(criar_frame, text="Criar Conta", font=("Arial", 16), bg="black", fg="white")
criar_label.pack(pady=10)

criar_usuario_label = tk.Label(criar_frame, text="Usuário:", bg="black", fg="white")
criar_usuario_label.pack()
criar_usuario_entry = tk.Entry(criar_frame)
criar_usuario_entry.pack(pady=5)

criar_senha_label = tk.Label(criar_frame, text="Senha:", bg="black", fg="white")
criar_senha_label.pack()
criar_senha_entry = tk.Entry(criar_frame, show="*")
criar_senha_entry.pack(pady=5)

# Usando o botão do ttk com o estilo redefinido
criar_btn = ttk.Button(criar_frame, text="Criar Conta", command=criar_conta)
criar_btn.pack(pady=10)

voltar_login_btn = ttk.Button(criar_frame, text="Voltar ao Login", command=mostrar_login)
voltar_login_btn.pack(pady=5)

# Exibe inicialmente a tela de login
login_frame.pack()

# Inicia o loop da interface
janela.mainloop()