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

    def create_home_screen(self):
        self.clear_window()

        tk.Label(self.root, text="7Flix", font=("Arial", 24), fg='white', bg='black').pack(pady=20)

        series_list = [
            Series("Outer Banks", "Mistério e aventura numa caça ao tesouro perdido.", "https://youtu.be/pipb8KRUo9g", "outerbanks.jpg"),
            Series("Squid Game", "Jogos mortais por um prêmio tentador.", "https://youtu.be/lQBmZBJCYcY", "squidgame.jpg"),
            Series("Cobra Kai", "Rivalidades reacendidas no mundo do Karatê.", "https://youtu.be/xCwwxNbtK6Y", "cobrakai.jpg"),
            Series("Stranger Things", "Forças sobrenaturais e experimentos secretos.", "https://youtu.be/otutSrxYpa4", "strangerthings.jpg"),
            Series("Breaking Bad", "Um professor de química fabrica metanfetaminas para sustentar sua família.", "https://youtu.be/2-W6_6gJda0", "breakingbad.jpg"),
        ]

        canvas = tk.Canvas(self.root, bg='black')
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=canvas.yview)
        series_frame = tk.Frame(canvas, bg='black')

        series_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=series_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        columns = 4
        for index, serie in enumerate(series_list):
            row = index // columns
            col = index % columns

            serie_frame = tk.Frame(series_frame, bd=2, relief="groove", bg='black')
            serie_frame.grid(row=row, column=col, padx=10, pady=10)

            try:
                if os.path.exists(serie.image_path):
                    image = Image.open(serie.image_path)
                    image = image.resize((200, 300))  # Ajusta o tamanho da imagem
                    image = ImageTk.PhotoImage(image)
                    tk.Label(serie_frame, image=image, bg='black').pack()
                    serie_frame.image = image  # Prevenir garbage collection
                else:
                    tk.Label(serie_frame, text="Imagem indisponível", bg='black', fg='red').pack()
            except Exception as e:
                tk.Label(serie_frame, text="Erro ao carregar imagem", bg='black', fg='red').pack()

            tk.Label(serie_frame, text=serie.title, font=("Arial", 14, "bold"), fg='white', bg='black').pack()
            tk.Label(serie_frame, text=serie.description, wraplength=200, fg='white', bg='black').pack()
            tk.Button(serie_frame, text="Assistir", command=lambda s=serie: self.watch_serie(s.link), bg='black', fg='white').pack(pady=5)

    def watch_serie(self, link):
        webbrowser.open(link)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
