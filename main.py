import shutil
import os
import pathlib
from tkinter import messagebox
from tkinter import filedialog

print("**************************************")
print("Backup de usuários")
print("**************************************")

username = input("Informe o login do usuário: ")
op = messagebox.askyesno(title="Atenção", message="Deseja selecionar um diretório para salvar os backups ?")

if op:
    pathOrigin = filedialog.askdirectory()
    pathDest = filedialog.askdirectory()

    if os.path.exists(pathDest):
        nome = pathlib.PurePath(pathOrigin).name
        pathDest = os.path.join(pathDest, nome)

    shutil.copytree(pathOrigin, pathDest)

