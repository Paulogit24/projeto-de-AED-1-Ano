import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os

# Definições da tela principal
root = tk.Tk()
root.title("7FLIX")
root.geometry("1920x1080")
root.configure(bg="black")

# Tela de Login
login_frame = tk.Frame(root, bg="black")
login_frame.pack(fill="both", expand=True)

# Carregar e mostrar logo
try:
    logo_img = Image.open("7fliX.png")
    logo_img = logo_img.resize((200, 100), Image.ANTIALIAS)
    logo_photo = ImageTk.PhotoImage(logo_img)
    logo_label = tk.Label(login_frame, image=logo_photo, bg="black")
    logo_label.pack(pady=20)
except FileNotFoundError:
    tk.Label(login_frame, text="7FLIX", font=("Helvetica", 28, "bold"), fg="red", bg="black").pack(pady=20)

# Titulo na tela
titulo = tk.Label(login_frame, text="Login", font=("Helvetica", 24, "bold"), fg="white", bg="black")
titulo.pack(pady=20)

# Entrada do Utilizador
username_label = tk.Label(login_frame, text="Utilizador:", font=("Helvetica", 16), fg="white", bg="black")
username_label.pack(pady=5)
username_entry = tk.Entry(login_frame, font=("Helvetica", 14))
username_entry.pack(pady=5)

# Entrada da senha
password_label = tk.Label(login_frame, text="Senha:", font=("Helvetica", 16), fg="white", bg="black")
password_label.pack(pady=5)
password_entry = tk.Entry(login_frame, font=("Helvetica", 14), show="*")
password_entry.pack(pady=5)

# Botão do Login
login_button = tk.Button(login_frame, text="Entrar", font=("Helvetica", 16), bg="red", fg="white", command=fazer_login)
login_button.pack(pady=10)

# Botão para criar a conta
criar_conta_button = tk.Button(login_frame, text="Criar conta", font=("Helvetica", 14), bg="gray", fg="white", command=criar_conta)
criar_conta_button.pack(pady=5)

# Tela para criar a conta
criar_conta_frame = tk.Frame(root, bg="black")

# Titulo para a tela
novo_titulo = tk.Label(criar_conta_frame, text="Criar Conta", font=("Helvetica", 24, "bold"), fg="white", bg="black")
novo_titulo.pack(pady=20)

# Entrada para criar a conta
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

voltar_button = tk.Button(criar_conta_frame, text="Voltar", font=("Helvetica", 14), bg="gray", fg="white", command=fazer_login)
voltar_button.pack(pady=5)

# Tela Principal
principal_frame = tk.Frame(root, bg="black")

titulo_principal = tk.Label(principal_frame, text="7FLIX", font=("Helvetica", 28, "bold"), fg="red", bg="black", pady=20)
titulo_principal.pack(fill="x")

# Conteúdo para a interface (como por exemplo as categorias)
main_frame = tk.Frame(principal_frame, bg="black")
main_frame.pack(fill="both", expand=True)

scrollbar = ttk.Scrollbar(main_frame, orient="vertical")
scrollbar.pack(side="right", fill="y")

canvas = tk.Canvas(main_frame, bg="black", yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.config(command=canvas.yview)

content_frame = tk.Frame(canvas, bg="black")
canvas.create_window((0, 0), window=content_frame, anchor="nw")

categorias = ["top 10", "Ação", "Comédia", "Drama", "Suspense", "Terror"]
for categoria in categorias:
    cat_label = tk.Label(content_frame, text=categoria, font=("Helvetica", 20, "bold"), fg="white", bg="black", anchor="w", pady=10)
    cat_label.pack(fill="x", padx=10)
    cat_frame = tk.Frame(content_frame, bg="black")
    cat_frame.pack(fill="x", pady=5)
    for i in range(5):
        filme_button = tk.Button(cat_frame, text=f"Filme {i+1}", width=15, height=3, bg="grey", fg="white")
        filme_button.pack(side="left", padx=5)

# Atualizar o canvas
content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Botão que é para sair
sair_button = tk.Button(principal_frame, text="Sair", font=("Helvetica", 14), bg="red", fg="white", command=sair_do_sistema)
sair_button.pack(side="bottom", pady=10)

# Executar a aplicação
root.mainloop()