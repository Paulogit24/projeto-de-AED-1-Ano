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
        self.root.geometry("1000x600")
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

        #Botão de login no canto superior direito
        tk.Button(top_bar_frame, text="Login", command=self.create_login_screen, bg='black', fg='white', font=("Arial", 12)).pack(side='right', padx=10)

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

   #sub menu
        self.create_bottom_menu()

    def create_bottom_menu(self):
        bottom_menu_frame = tk.Frame(self.root, bg='black')
        bottom_menu_frame.pack(side='bottom', fill='x')

        tk.Button(bottom_menu_frame, text="Ajuda", bg='black', fg='white', font=("Arial", 12),
                  command=lambda: messagebox.showinfo("Ajuda", "Bem vindo podes criar conta, para aceder ao website! :)")).pack(side='left', padx=10)
        tk.Button(bottom_menu_frame, text="Sobre", bg='black', fg='white', font=("Arial", 12),
                  command=lambda: messagebox.showinfo("Sobre", "7FLIX é uma plantaforma de divulgar séries, seja bem-vindo")).pack(side='left', padx=10)

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

        top_bar_frame = tk.Frame(self.root, bg='black')
        top_bar_frame.pack(fill='x', side='top')

        # Botão de Administrador
        tk.Button(top_bar_frame, text="Administrador", command=self.admin_screen, bg='red', fg='white', font=("Arial", 12)).pack(side='right', padx=10)

        tk.Label(self.root, text="7Flix", font=("Arial", 24), fg='white', bg='black').pack(pady=20)

        series_list = [
            Series("Outer Banks", "Mistério e aventura numa caça ao tesouro perdido.", "https://youtu.be/pipb8KRUo9g", "outerbanks.jpg"),
            Series("Squid Game", "Jogos mortais por um prêmio tentador.", "https://youtu.be/lQBmZBJCYcY", "squidgame.jpg"),
            Series("Cobra Kai", "Rivalidades reacendidas no mundo do Karatê.", "https://youtu.be/xCwwxNbtK6Y", "cobrakai.jpg"),
            Series("Stranger Things", "Forças sobrenaturais e experimentos secretos.", "https://youtu.be/otutSrxYpa4", "strangerthings.jpg"),
            Series("Breaking Bad", "Um professor de química fabrica metanfetaminas para sustentar sua família.", "https://youtu.be/2-W6_6gJda0", "breakingbad.jpg"),

            Series("The Witcher", "Aventura épica num mundo de monstros e magia.", "https://youtu.be/ndl1W4ltcmg?si=bHZ0xNFQGdaWAy0_", "TheWitcher.jpg"),
            Series("The Crown", "Um olhar dramático sobre a vida da Rainha Elizabeth II e a monarquia britânica.", "https://youtu.be/JWtnJjn6ng0?si=4vdz4EWrqRvKTn5h", "TheCrown.jpg"),
            Series("Peaky Blinders", "A história de uma família criminosa na Inglaterra dos anos 1920.", "https://youtu.be/oVzVdvGIC7U?si=aH9a9xQM2GLpchah", "PeakyBlinders.jpg"),
            Series("The Boys", "Super-heróis corruptos são desafiados por um grupo de justiceiros.", "https://youtu.be/I0RC15nmjpU?si=X2XKVE9nu6Hc310z", "TheBoys.jpg"),
            Series("Euphoria", "Jovens enfrentam desafios como amor, identidade e vícios.", "https://youtu.be/6XGnv7Zgbeg?si=Zj80y9QqXWq3iyiX", "Euphoria.jpg"),
            Series("Friends", "As aventuras e confusões de seis amigos em Nova Iorque.", "https://youtu.be/Zg2LCD5QOJs?si=PphM8Fg4QL3UJEnO", "Friends.jpg"),
            Series("Dark", "Uma trama misteriosa de viagens no tempo numa pequena cidade alemã.", "https://youtu.be/ESEUoa-mz2c?si=px_w2me3q7XPaY0l", "Dark.jpg"),
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
                    image = image.resize((200, 300)) 
                    image = ImageTk.PhotoImage(image)
                    tk.Label(serie_frame, image=image, bg='black').pack()
                    serie_frame.image = image  
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
