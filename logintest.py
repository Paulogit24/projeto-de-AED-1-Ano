"""users.py

Métodos relacionados com os utilizadores

Criar conta, autenticação, validação password,...
"""

fusers=".\\files\\utilizadores.txt"

def lerUsers(): #Lê o ficheiro de utilizadores.txt
    fileUsers=open(fusers, "r", encoding="utf-8")
    listaUsers= fileUsers.readlines()
    fileUsers.close()
    return listaUsers

def validaConta (userName, userPass): #Validar autenticação com uma conta: LOGIN
    listausers = lerUsers()
    for linha in listaUsers:

        if linha.split(";")[0]== userName and linha.split(";") [1] == userPass:
            msg = "Bem-vindo" + userName
            return msg
    msg = "O UserName ou a Password estão incorretos!"
    return msg

def criaconta(userName, userPass, userPassConfirm):   #Criar uma nova conta de utilizador

    if userName == "" or userPass == "":
        msg = "O username e a password não podem ser vazios!"
        return False, msg

    if userPass != userPassConfirm:
        msg ="A password não coincide com a sua confirmação!"
        return False, msg
    listaUsers =lerUsers()
    for linha in listaUsers:
        fields = linha.split(";")
        if fields[0] == userName:
            msg = "Já existe um utilizador com esse username!"
            return False, msg
    # acrescenta user ao ficheiro
    fileUsers =open(fUsers, "a")
    linha =userName + ";" + userPass + ";" + "user"+ "\n"
    fileUsers.write(linha)
    fileUsers.close()
    msg = "Conta criada com sucesso!"
    return True, msg