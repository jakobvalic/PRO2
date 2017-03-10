# -*- encoding: utf-8 -*-

# Prikaz drsnika za izbiro vrednosti. Dva drsnika določata
# polmera elipse.

from tkinter import *

class Elipsa():
    def __init__(self, master):
        # Začetne dimenzije elipse
        zacetni_a = 30
        zacetni_b = 70

        # Drsnika
        self.scale_a = Scale(master, orient=HORIZONTAL, from_=0, to=150,
                        command=self.posodobi_a, length=300)
        self.scale_a.set(zacetni_a)
        self.scale_a.grid(row=1, column=1)

        self.scale_b = Scale(master, orient=VERTICAL, from_=0, to=150,
                        command=self.posodobi_b, length=300)
        self.scale_b.set(zacetni_b)
        self.scale_b.grid(row=0, column=0)

        self.canvas = Canvas(master, width=300, height=300)
        self.canvas.grid(row=0, column=1)
        # bounding box
        self.elipsa = self.canvas.create_oval(0,0,1,1,fill="white")
        self.narisi(zacetni_a, zacetni_b)

    def posodobi_a(self, x):
        y = int(self.scale_b.get())
        self.narisi(int(x), y)

    def posodobi_b(self, y):
        x = int(self.scale_a.get())
        self.narisi(x, int(y))

    def narisi(self, a, b):
        self.canvas.coords(self.elipsa,
                           150 - a, 150 - b,
                           150 + a, 150 + b)


# Glavnemu oknu rečemo "root" (koren), ker so grafični elementi
# organizirani v drevo, glavno okno pa je koren tega drevesa

# Naredimo glavno okno
root = Tk()

aplikacija = Elipsa(root)

# Kontrolo prepustimo glavnemu oknu. Funkcija mainloop neha
# delovati, ko okno zapremo.
root.mainloop()
