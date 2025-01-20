import tkinter as tk
from tkinter import messagebox
import webbrowser

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
    def __init__(self, title, description, link):
        self.title = title
        self.description = description
        self.link = link

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("7FLIX")
        self.root.geometry("800x600")
        self.root.configure(bg='black')  
        self.user_manager = UserManager()

        # Menu no canto superior direito
        self.create_top_bar()

        # Primeira tela será de login
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

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if self.user_manager.validate_user(username, password):
            messagebox.showinfo("Correto!")
            self.create_home_screen()
        else:
            messagebox.showerror("Errado")

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        if not username or not password:
            messagebox.showerror("Erro", "Por favor, completa todos os campos.")
            return
        
        if self.user_manager.register_user(username, password):
            messagebox.showinfo("Registo", "Utilizador registrado com sucesso!")
        else:
            messagebox.showerror("Erro", "Utilizador já registado.")

    def admin_screen(self):
        self.clear_window()
        # Tela para admin
        tk.Label(self.root, text="Bem-vindo ao Painel de Administrador", font=("Arial", 24), fg='white', bg='black').pack(pady=20)

    def create_home_screen(self):
        self.clear_window()
        
        tk.Label(self.root, text="Home", font=("Arial", 24), fg='white', bg='black').pack(pady=20)

        series_list = [
            Series("Outer Banks", "Numa ilha de ricos e pobres da Carolina do Norte, John B e o seu grupo coeso de amigos encontram mistério e aventura numa caça ao tesouro perdido.", "https://youtu.be/pipb8KRUo9g?si=_vXSA884tjmI4zHj"),
            Series("Squid Game", "Squid Game é uma série de suspense e drama.", "https://youtu.be/lQBmZBJCYcY?si=UwWbwzus7BQei8Iq"),
            Series("Cobra Kai", "Cobra Kai é uma série que continua a história de Karate Kid.", "https://youtu.be/xCwwxNbtK6Y?si=6oDRwRoTIS4-pjtJ"),
            Series("Stranger Things", "Stranger Things mistura ficção científica e terror.", "https://youtu.be/otutSrxYpa4?si=PsPP5WzcU3hh3OLD"),
            Series("Teen Wolf", "Teen Wolf segue Scott McCall, um adolescente que vira lobisomem e enfrenta ameaças sobrenaturais.", "https://youtu.be/BmHM5eUp9w4?si=2_P20b6sslN_Ktiw"),
            Series("You", "Um jovem perigosamente charmoso e intensamente obsessivo toma medidas extremas para se inserir na vida daqueles por quem ele é fascinado.", "https://youtu.be/xcicf6XmtnM?si=gxIBPcQAx1_LbvYB"),
        ]

        series_frame = tk.Frame(self.root, bg='black')
        series_frame.pack(pady=20)

        for serie in series_list:
            serie_frame = tk.Frame(series_frame, bd=2, relief="groove", bg='black')
            serie_frame.pack(side="left", padx=10, pady=10)
            
            tk.Label(serie_frame, text=serie.title, font=("Arial", 14, "bold"), fg='white', bg='black').pack()
            tk.Label(serie_frame, text=serie.description, wraplength=150, fg='white', bg='black').pack()
            tk.Button(serie_frame, text="Assistir", command=lambda s=serie: self.watch_serie(s.link), bg='black', fg='white').pack(pady=5)

    def watch_serie(self, link):
        webbrowser.open(link)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
