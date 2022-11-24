from tkinter import *
import tkinter as tk
from tkinter import ttk
import tkinter
from tkinter import messagebox

def con():
    u = (txtu.get())
    p = (txtp.get())
    if u=='' or p=='':
        messagebox.showinfo(title="Error", message="Uno o ambos espacios no fueron llenados")
    elif u==user and p==password:
        messagebox.showinfo(title="Bienvenido", message=" Cool ")
        ventana2 = Toplevel(ventana)
        ventana2.geometry("600x400")
        ventana2.title("Bienvenido")
        var = IntVar()
        bg2 = PhotoImage(file= "bg.png")
        my_label2 = Label(ventana2, image=bg2)
        my_label2.place(x=0, y=0, relwidth=1, relheight=1)
        lbl_img2 = Label(ventana2, image=img)
        lbl_img2.place(relx=0.38, rely=0.1)
        
        R1 = Radiobutton(ventana2, text="Rutina 1", fg="white", bg="black", padx = 20, variable=var, value=1)
        R1.pack(anchor=W)

        R2 = Radiobutton(ventana2, text="Rutina 2", fg="white", bg="black", padx = 20, variable=var, value=2)
        R2.pack(anchor=W)
        
        R3 = Radiobutton(ventana2, text="Rutina 3", fg="white", bg="black", padx = 20, variable=var, value=2)
        R3.pack(anchor=W)
        ventana2.mainloop()
        
        
    else:
        messagebox.showinfo(title="Invalido", message="Su usuario o contrasena son incorrectos")

user="MarioGaelFer"
password="RoboDog"

ventana = Tk()
ventana.geometry("600x400")
ventana.title("Login")
ventana.iconbitmap('Login.ico')

bg = PhotoImage(file= "bg.png")
my_label = Label(ventana, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

img = PhotoImage(file="usering.png")
lbl_img = Label(ventana, image=img)
lbl_img.place(relx=0.38, rely=0.1)

lblu=Label(ventana, text=" Usuario ", bg='#580570', foreground='white').place(relx=.25, rely=.45)
txtu=Entry(ventana, justify=CENTER, bg='#DBA6EB', width=30)
txtu.place(relx=.36, rely=.45)

lblp=Label(ventana, text=" Contrasena ", bg='#580570', foreground='white').place(relx=.22, rely=.55)
txtp=Entry(ventana, justify=CENTER, bg='#DBA6EB', width=30, show="*")
txtp.place(relx=.36, rely=.55)

btnregistrar=Button(ventana, text="INGRESAR", width=15, height=1, bg='purple', foreground='white', activebackground='pink',
                    activeforeground='white', font=("Century", 12, 'bold'),border=5, command=con)
btnregistrar.place(relx=0.37, rely=0.70)
btnsalir=Button(ventana, text="SALIR", width=15, bg='#161476', foreground='white', command= ventana.destroy)
btnsalir.place(relx=0.77, rely=0.85)



ventana.resizable(False, False)
ventana.mainloop()
