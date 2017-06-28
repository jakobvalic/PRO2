# -*- encoding: utf-8 -*-

# Prikaz drsnika za izbiro vrednosti. Dva drsnika določata
# polmera elipse.

from tkinter import *

class Elipsa():
    def __init__(self, master):
        # Polmera elipse
        self.a = 70
        self.b = 30

        # Drsnika
        scale_a = Scale(master, orient=HORIZONTAL, from_=0, to=150,
                        command=self.posodobi_a, length=300)
        scale_a.set(self.a)
        scale_a.grid(row=1, column=1)

        scale_b = Scale(master, orient=VERTICAL, from_=0, to=150,
                        command=self.posodobi_b, length=300)
        scale_b.set(self.b)
        scale_b.grid(row=0, column=0)

        self.canvas = Canvas(master, width=300, height=300)
        self.canvas.grid(row=0, column=1)
        # bounding box
        self.elipsa = self.canvas.create_oval(0,0,1,1,fill="white")
        self.narisi()

    def posodobi_a(self, x):
        self.a = int(x)
        self.narisi()

    def posodobi_b(self, y):
        self.b = int(y)
        self.narisi()

    def narisi(self):
        self.canvas.coords(self.elipsa,
                           150-self.a, 150-self.b,
                           150+self.a, 150+self.b)


# Glavnemu oknu rečemo "root" (koren), ker so grafični elementi
# organizirani v drevo, glavno okno pa je koren tega drevesa

# Naredimo glavno okno
root = Tk()

aplikacija = Elipsa(root)

# Kontrolo prepustimo glavnemu oknu. Funkcija mainloop neha
# delovati, ko okno zapremo.
root.mainloop()
