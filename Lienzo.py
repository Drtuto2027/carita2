import tkinter as tk
from tkinter import *

class Lienzo():
    def paint(self, event):
        self.lienzo.delete("cara", "ojos", "boca")
        if(event.keysym == "Right"):
             self.x+=10
        elif (event.keysym == "Left"):
             self.x-=10
        elif (event.keysym == "Up"):
             self.y-=10
        elif (event.keysym == "Down"):
             self.y+=10
        cara = self.lienzo.create_oval(275+self.x,275+self.y, 425+self.x,425+self.y, fill="yellow", width=2, tags="cara", outline="green")
        ojoIzq = self.lienzo.create_oval(305+self.x,290,335+self.x,350, fill="black", tags="ojos")
        ojoDer = self.lienzo.create_oval(365+self.x,290,395+self.x,350, fill="black", tags="ojos")
        if(self.estado == True):
                boca = self.lienzo.create_arc(305+self.x, 370, 395+self.x, 410, start=0, extent=180, tags="boca")
                self.estado=False
        else:
                boca = self.lienzo.create_arc(305+self.x, 370, 395+self.x, 410, start=0, extent=-180, tags="boca")
                self.estado=True
           

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Carita")
        self.ventana.config(width=750, height=750)
        self.ventana.resizable(0,0)

        self.x = 0
        self.y = 0
        self.estado = True

        self.lienzo = tk.Canvas(self.ventana, bg="gray")
        self.lienzo.place(width=700, height=700, relx=0.5, rely=0.5, anchor="center")

        self.ventana.bind("<KeyRelease>", self.paint)
        
        self.ventana.mainloop()