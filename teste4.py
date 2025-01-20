import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  
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
    def __init__(self, title, description, link, image_path):
        self.title = title
        self.description = description
        self.link = link
        self.image_path = image_path

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("7FLIX")
        self.root.geometry("1200x800")  # Aumentei para caber as imagens
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
        # Tela para admin
        tk.Label(self.root, text="Bem-vindo ao Painel de Administrador", font=("Arial", 24), fg='white', bg='black').pack(pady=20)

    def create_home_screen(self):
        self.clear_window()

        tk.Label(self.root, text="7Flix", font=("Arial", 24), fg='white', bg='black').pack(pady=20)

        series_list = [
            Series("Outer Banks", "Mistério e aventura numa caça ao tesouro perdido.", "https://youtu.be/pipb8KRUo9g", "outerbanks.jpg"),
            Series("Squid Game", "Jogos mortais por um prêmio tentador.", "https://youtu.be/lQBmZBJCYcY", "squidgame.jpg"),
            Series("Cobra Kai", "Rivalidades reacendidas no mundo do Karatê.", "https://youtu.be/xCwwxNbtK6Y", "cobrakai.jpg"),
            Series("Stranger Things", "Forças sobrenaturais e experimentos secretos.", "https://youtu.be/otutSrxYpa4", "strangerthings.jpg"),

            Series("Breaking Bad", "Um professor do secundário com cancro do pulmão terminal junta-se a um ex-aluno para fabricar e vender metanfetaminas como forma de garantir o futuro da sua família. ""Ruptura Total"" venceu um total de 16 Emmys, incluindo quatro para Melhor Ator Dramático, para Bryan Cranston.", "https://youtu.be/2-W6_6gJda0?si=x2u9r95P8RoVfets", "breakingbad.jpg"),
            Series("Daredevil", "Cego desde criança, Matt Murdock luta contra a injustiça em Nova Iorque, durante o dia como advogado e à noite na pele do super-herói Demolidor. O ""Demolidor"" recebeu três nomeações para os Emmys de 2015 em categorias criativas, incluindo efeitos visuais.", "https://youtu.be/jAy6NJ_D5vU?si=HrCExxZg38PcwqzX", "Daredevil.jpg"),
            Series("Game of Thrones", "Game of Thrones conta a história de um lugar onde uma força destruiu o equilíbrio das estações, há muito tempo. Em uma terra onde os verões podem durar vários anos e o inverno toda uma vida, as reivindicações e as forças sobrenaturais correm as portas do Reino dos Sete Reinos.", "https://youtu.be/KPLWWIOCOOQ?si=aw47eEKzJTBd1Hkt", "GameofThrones .jpg"),
            Series("Jack Ryan", "Jack Ryan (John Krasinski) é um promissor analista da CIA que recebe uma missão perigosa após a descoberta de uma série de transferências bancárias duvidosas. Ao investigar um padrão de comunicações terroristas, ele se depara com uma intrincada estratégia que tem como meta a destruição do mundo - a começar pelos EUA", "https://youtu.be/K9KAnx4EvaE?si=Ta-gQJ9IrHAgcN6-", "JackRyan.jpg"),
        ]

        series_frame = tk.Frame(self.root, bg='black')
        series_frame.pack(pady=20)

        for serie in series_list:
            serie_frame = tk.Frame(series_frame, bd=2, relief="groove", bg='black')
            serie_frame.pack(side="left", padx=15, pady=15)

            try:
                image = Image.open(serie.image_path)
                image = image.resize((200, 300))  # Redimensiona para caber
                image = ImageTk.PhotoImage(image)
                tk.Label(serie_frame, image=image, bg='black').pack()
                serie_frame.image = image  # Prevenir garbage collection
            except Exception as e:
                tk.Label(serie_frame, text="Imagem indisponível", bg='black', fg='red').pack()

            tk.Label(serie_frame, text=serie.title, font=("Arial", 14, "bold"), fg='white', bg='black').pack()
            tk.Label(serie_frame, text=serie.description, wraplength=200, fg='white', bg='black').pack()
            tk.Button(serie_frame, text="Assistir", command=lambda s=serie: self.watch_serie(s.link), bg='black', fg='white').pack(pady=5)

    def watch_serie(self, link):
        webbrowser.open(link)

if __name__ == "__main__":
    
    root = tk.Tk()
    app = App(root)
    root.mainloop()