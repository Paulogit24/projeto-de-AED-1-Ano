import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

# Dados simulados para login e séries
usuarios = {"admin": "admin123"}  # Login de exemplo para administrador
series = []  # Lista de séries gerenciada pelo administrador

# Funções Gerais
def sair_do_sistema():
    root.destroy()

def fazer_login():
    usuario = username_entry.get()
    senha = password_entry.get()
    if usuario in usuarios and usuarios[usuario] == senha:
        if usuario == "admin":
            acessar_admin()
        else:
            acessar_usuario()
    else:
        messagebox.showerror("Erro de Login", "Usuário ou senha incorretos.")

def criar_conta():
    novo_usuario = novo_username_entry.get()
    nova_senha = nova_password_entry.get()
    confirmar_senha = confirmar_password_entry.get()
    
    if not novo_usuario or not nova_senha:
        messagebox.showwarning("Aviso", "Todos os campos são obrigatórios.")
        return
    
    if novo_usuario in usuarios:
        messagebox.showerror("Erro", "Usuário já existe.")
        return
    
    if nova_senha != confirmar_senha:
        messagebox.showerror("Erro", "As senhas não coincidem.")
        return
    
    usuarios[novo_usuario] = nova_senha
    messagebox.showinfo("Sucesso", "Conta criada com sucesso!")
    voltar_para_login()

def acessar_admin():
    login_frame.pack_forget()
    criar_conta_frame.pack_forget()
    principal_frame.pack_forget()
    admin_frame.pack(fill="both", expand=True)
    atualizar_series()

def acessar_usuario():
    login_frame.pack_forget()
    criar_conta_frame.pack_forget()
    admin_frame.pack_forget()
    principal_frame.pack(fill="both", expand=True)

def voltar_para_login():
    criar_conta_frame.pack_forget()
    admin_frame.pack_forget()
    principal_frame.pack_forget()
    login_frame.pack(fill="both", expand=True)

# Funções Administrativas
def adicionar_serie():
    serie = adicionar_serie_entry.get().strip()
    if serie:
        series.append(serie)
        atualizar_series()
        adicionar_serie_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "O campo da série não pode estar vazio.")

def remover_serie():
    try:
        selecionada = series_lista.get(series_lista.curselection())
        series.remove(selecionada)
        atualizar_series()
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma série para remover.")

def atualizar_series():
    series_lista.delete(0, tk.END)
    for serie in series:
        series_lista.insert(tk.END, serie)

# Tela Principal
root = tk.Tk()
root.title("7FLIX")
root.geometry("1920x1080")
root.configure(bg="black")

# Tela de Login
login_frame = tk.Frame(root, bg="black")
login_frame.pack(fill="both", expand=True)

try:
    logo_img = Image.open("7fliX.png")
    logo_img = logo_img.resize((200, 100), Image.ANTIALIAS)
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(login_frame, image=logo_photo, bg="black")
    logo_label.pack(pady=20)
except FileNotFoundError:
    tk.Label(login_frame, text="7FLIX", font=("Helvetica", 28, "bold"), fg="red", bg="black").pack(pady=20)

titulo = tk.Label(login_frame, text="Login", font=("Helvetica", 24, "bold"), fg="white", bg="black")
titulo.pack(pady=20)

username_label = tk.Label(login_frame, text="Utilizador:", font=("Helvetica", 16), fg="white", bg="black")
username_label.pack(pady=5)
username_entry = tk.Entry(login_frame, font=("Helvetica", 14))
username_entry.pack(pady=5)

password_label = tk.Label(login_frame, text="Senha:", font=("Helvetica", 16), fg="white", bg="black")
password_label.pack(pady=5)
password_entry = tk.Entry(login_frame, font=("Helvetica", 14), show="*")
password_entry.pack(pady=5)

login_button = tk.Button(login_frame, text="Entrar", font=("Helvetica", 16), bg="red", fg="white", command=fazer_login)
login_button.pack(pady=10)

criar_conta_button = tk.Button(login_frame, text="Criar conta", font=("Helvetica", 14), bg="gray", fg="white", command=criar_conta)
criar_conta_button.pack(pady=5)

# Tela para criar a conta
criar_conta_frame = tk.Frame(root, bg="black")

novo_titulo = tk.Label(criar_conta_frame, text="Criar Conta", font=("Helvetica", 24, "bold"), fg="white", bg="black")
novo_titulo.pack(pady=20)

novo_username_label = tk.Label(criar_conta_frame, text="Novo Utilizador:", font=("Helvetica", 16), fg="white", bg="black")
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

registrar_button = tk.Button(criar_conta_frame, text="Registrar", font=("Helvetica", 16), bg="red", fg="white", command=criar_conta)
registrar_button.pack(pady=10)

voltar_button = tk.Button(criar_conta_frame, text="Voltar", font=("Helvetica", 14), bg="gray", fg="white", command=voltar_para_login)
voltar_button.pack(pady=5)

# Tela de Administração
admin_frame = tk.Frame(root, bg="black")

admin_titulo = tk.Label(admin_frame, text="Área Administrativa", font=("Helvetica", 24, "bold"), fg="white", bg="black")
admin_titulo.pack(pady=20)

adicionar_serie_label = tk.Label(admin_frame, text="Adicionar Série:", font=("Helvetica", 16), fg="white", bg="black")
adicionar_serie_label.pack(pady=5)
adicionar_serie_entry = tk.Entry(admin_frame, font=("Helvetica", 14))
adicionar_serie_entry.pack(pady=5)

adicionar_button = tk.Button(admin_frame, text="Adicionar", font=("Helvetica", 14), bg="red", fg="white", command=adicionar_serie)
adicionar_button.pack(pady=5)

series_lista = tk.Listbox(admin_frame, font=("Helvetica", 14), bg="black", fg="white", selectmode=tk.SINGLE)
series_lista.pack(fill="both", expand=True, padx=20, pady=10)

remover_button = tk.Button(admin_frame, text="Remover", font=("Helvetica", 14), bg="red", fg="white", command=remover_serie)
remover_button.pack(pady=5)

voltar_button = tk.Button(admin_frame, text="Voltar", font=("Helvetica", 14), bg="gray", fg="white", command=voltar_para_login)
voltar_button.pack(pady=10)

# Tela Principal (para usuários comuns)
principal_frame = tk.Frame(root, bg="black")

titulo_principal = tk.Label(principal_frame, text="7FLIX", font=("Helvetica", 28, "bold"), fg="red", bg="black", pady=20)
titulo_principal.pack(fill="x")

# Executar a aplicação
root.mainloop()
