import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import webbrowser
import os

class UserManager:
    def __init__(self):
        self.users = {}

    def register_user(self, username, password):
        if username in self.users:
            return False
        self.users[username] = password
        return True

    def validate_user(self, username, password):
        return self.users.get(username) == password

class Series:
    def __init__(self, title, description, link, image_path):
        self.title = title
        self.description = description
        self.link = link
        self.image_path = image_path

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("7FLIX")
        self.root.geometry("1200x800")
        self.root.configure(bg='black')
        self.user_manager = UserManager()
        self.create_top_bar()
        self.create_login_screen()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_top_bar(self):
        top_bar_frame = tk.Frame(self.root, bg='black')
        top_bar_frame.pack(fill='x', side='top')
        tk.Button(top_bar_frame, text="Login", command=self.create_login_screen, bg='black', fg='white', font=("Arial", 12)).pack(side='right', padx=10)
        tk.Button(top_bar_frame, text="Administrador", command=self.admin_screen, bg='black', fg='white', font=("Arial", 12)).pack(side='right', padx=10)

    def create_login_screen(self):
        self.clear_window()
        login_frame = tk.Frame(self.root, bg='black')
        login_frame.pack(pady=100)

        tk.Label(login_frame, text="Bem-vindo!", font=("Arial", 24), fg='white', bg='black').pack(pady=20)
        tk.Label(login_frame, text="Utilizador:", font=("Arial", 14), fg='white', bg='black').pack()
        self.username_entry = tk.Entry(login_frame, font=("Arial", 14))
        self.username_entry.pack(pady=5)
        tk.Label(login_frame, text="Senha:", font=("Arial", 14), fg='white', bg='black').pack()
        self.password_entry = tk.Entry(login_frame, show="*", font=("Arial", 14))
        self.password_entry.pack(pady=5)

        tk.Button(login_frame, text="Entrar", command=self.login, bg='black', fg='white', font=("Arial", 12)).pack(pady=5)
        tk.Button(login_frame, text="Registar", command=self.register, bg='black', fg='white', font=("Arial", 12)).pack(pady=5)
        tk.Button(self.root, text="Ajuda", command=self.create_help_screen, bg='black', fg='white', font=("Arial", 12)).pack(side='left', padx=10, pady=10)

    def create_help_screen(self):
        self.clear_window()
        help_frame = tk.Frame(self.root, bg='black')
        help_frame.pack(pady=50)

        tk.Label(help_frame, text="Perguntas Frequentes", font=("Arial", 24), fg='white', bg='black').pack(pady=20)
        questions = [
            "Como criar minha conta?",
            "Como entrar na minha conta (fazer login)?",
            "Como contactar os criadores da aplicacao?"
        ]

        for question in questions:
            question_frame = tk.Frame(help_frame, bg='gray', padx=10, pady=10)
            question_frame.pack(pady=10, fill='x', expand=True)
            tk.Label(question_frame, text=question, font=("Arial", 14), fg='white', bg='gray').pack()

        tk.Button(self.root, text="Voltar", command=self.create_login_screen, bg='black', fg='white', font=("Arial", 12)).pack(side='left', padx=10, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if self.user_manager.validate_user(username, password):
            messagebox.showinfo("Sucesso!", "Login bem-sucedido.")
            self.create_home_screen()
        else:
            messagebox.showerror("Erro", "Utilizador ou senha incorretos.")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if not username or not password:
            messagebox.showerror("Erro", "Por favor, completa todos os campos.")
            return
        if self.user_manager.register_user(username, password):
            messagebox.showinfo("Registo", "Utilizador registrado com sucesso!")
        else:
            messagebox.showerror("Erro", "Utilizador já registrado.")

    def admin_screen(self):
        self.clear_window()
        tk.Label(self.root, text="Bem-vindo ao Painel de Administrador", font=("Arial", 24), fg='white', bg='black').pack(pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
