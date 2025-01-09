import customtkinter
import os
import datetime
import CTkMessagebox
from  tkinter import ttk
from  PIL import Image, ImageTk

fUsers = ".\\users.txt"

def logacount():   #le o fichiero users.txt
    fileusers = open(fUsers, "r", encoding="utf-8")
    listausers = fileusers.readlines()
    fileusers.close
    return listausers

def createAcount():  #função de criação de contas
    username=input("nome de utilizador: ")