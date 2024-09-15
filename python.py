#Tengo que buscar como achicar imagenes
#Tengo que buscar como usar padding

import tkinter as tk
from tkinter import ttk
user = "pedro12"
password = "hola"

def verificar(entryUsuario, entryContraseña, usuario, contraseña, msj, labelImg, trueImg, falseImg):
    infoUsuario = entryUsuario.get()
    infoContraseña = entryContraseña.get()

    if infoUsuario == usuario and infoContraseña == contraseña:
        msj.configure(text = f"Usuario o contraseña correctos")
        labelImg.configure(image = trueImg)
    else:
        msj.configure(text = f"Usuario o contraseña incorrectos")
        labelImg.configure(image = falseImg)



root = tk.Tk()
root.title("Usuario-Contraseña")
root.geometry("700x700")
imagen = tk.PhotoImage(file="enojado.png" )
error = tk.PhotoImage(file="erroor.png")
correcto = tk.PhotoImage(file="correcto.png")
#Solo me deja png's
root.grid_rowconfigure(0, weight = 1)
root.grid_rowconfigure(1, weight = 1)
root.grid_rowconfigure(2, weight = 1)
root.grid_rowconfigure(3, weight = 1)
root.grid_rowconfigure(4, weight = 1)
root.grid_columnconfigure(0, weight = 1)
root.grid_columnconfigure(1, weight = 1)


label_usuario = ttk.Label(root, text = "Ingrese el nombre de usuario")
label_usuario.grid(row = 0, column = 0)
entry_usuario = ttk.Entry(root)
entry_usuario.grid(row = 1, column = 0)

label_contraseña = ttk.Label(root, text = "Ingrese una contraseña")
label_contraseña.grid(row = 2, column = 0)
entry_contraseña = ttk.Entry(root)
entry_contraseña.grid(row = 3, column = 0)

boton = ttk.Button(root, text = "Ingresar", command=lambda:verificar(entry_usuario,entry_contraseña,user,password,label_mensaje,label_img, correcto, error))
boton.grid(row = 4, column = 0)

label_mensaje = ttk.Label(root, text= "Usuario-Contraseña")
label_mensaje.grid(row = 1, column = 1)
label_img = ttk.Label(root)
label_img.grid(row = 2, column = 1)

root.mainloop()