import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("App de Séries - Estilo Netflix")
        self.root.geometry("800x600")
        self.users = {}  # Dicionário para armazenar usuários
        self.create_login_screen()

    def create_login_screen(self):
        # Limpar a janela
        for widget in self.root.winfo_children():
            widget.destroy()

        # Tela de Login/Registro
        tk.Label(self.root, text="Bem-vindo!", font=("Arial", 24)).pack(pady=20)
        tk.Label(self.root, text="Usuário:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        
        tk.Label(self.root, text="Senha:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()

        tk.Button(self.root, text="Entrar", command=self.login).pack(pady=5)
        tk.Button(self.root, text="Registrar", command=self.register).pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username in self.users and self.users[username] == password:
            messagebox.showinfo("Login", "Login bem-sucedido!")
            self.create_home_screen()
        else:
            messagebox.showerror("Erro", "Usuário ou senha inválidos.")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if username in self.users:
            messagebox.showerror("Erro", "Usuário já registrado.")
        elif not username or not password:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos.")
        else:
            self.users[username] = password
            messagebox.showinfo("Registro", "Usuário registrado com sucesso!")

    def create_home_screen(self):
        # Limpar a janela
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Bem-vindo à Home de Séries!", font=("Arial", 24)).pack(pady=20)

        series = [
            {"title": "Stranger Things", "img": "", "desc": "Mistério e ficção científica."},
            {"title": "The Witcher", "img": "", "desc": "Baseado nos livros e games."},
            {"title": "Breaking Bad", "img": "", "desc": "Um professor de química vira traficante."},
            {"title": "Money Heist", "img": "", "desc": "O maior assalto da história."},
        ]

        series_frame = tk.Frame(self.root)
        series_frame.pack()

        for serie in series:
            serie_frame = tk.Frame(series_frame, bd=2, relief="groove")
            serie_frame.pack(side="left", padx=10, pady=10)
            
            tk.Label(serie_frame, text=serie["title"], font=("Arial", 14, "bold")).pack()
            tk.Label(serie_frame, text=serie["desc"], wraplength=150).pack()
            tk.Button(serie_frame, text="Assistir", command=lambda s=serie: self.watch_serie(s["title"])).pack(pady=5)

    def watch_serie(self, serie_title):
        messagebox.showinfo("Assistindo", f"Você está assistindo a {serie_title}!")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()