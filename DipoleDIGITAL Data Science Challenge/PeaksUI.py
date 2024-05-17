from tkinter import *
from tkinter import filedialog as FileDialog
from io import open

#PeakAnalyser packages
import pandas as pd
import matplotlib.pyplot as plt
from io import open
from scipy.signal import find_peaks

import peakAnalyser

file_root = "" #La utilizamos para almacenar la ruta del fichero
def abrir():
    global file_root
    mensaje.set("Open file")
    file_root = FileDialog.askopenfilename(
            initialdir=".", 
            filetype=(("Text files","*.txt"),),
            title="Open text file")
    
    if file_root != "":
        fichero = open(file_root, "r")
        fichero.close()
        root.title(file_root + " - My editor")

root = Tk()
root.title("My editor")

#Menu superior
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=abrir)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(menu=filemenu, label="Archive")


#Cuerpo del UI
prominence1 = StringVar("5")
prominence2 = StringVar("5")

labelProm1 = Label(root, text="Numero 1")
labelProm1.grid(row=0,column=0,sticky="w",padx=5,pady=5)

peakProm1 = Entry(root, textvariable=prominence1)
peakProm1.grid(row=0,column=1)
peakProm1.config(justify="right",state="normal")

labelProm2 = Label(root, text="Numero 2")
labelProm2.grid(row=1,column=0,sticky="w",padx=5,pady=5)

peakProm2 = Entry(root,textvariable=prominence2)
peakProm2.grid(row=1,column=1)
peakProm2.config(justify="center",state="normal")

espacio = Label(root, text=" ")
espacio.grid(row=2,column=0)
boton = Button(root, text="Analyse",command=analyserFunc(file_root,prominence1,prominence2))
boton.grid(row=3,column=1)

# Monitor inferior
mensaje = StringVar()
mensaje.set("Welcome to my editor")
monitor = Label(root, textvar=mensaje, justify="left")
monitor.pack(side="left")

root.config(menu=menubar)
#Bucle de aplicacion al final
root.mainloop()