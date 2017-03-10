# -*- encoding: utf-8 -*-

# Preprost kalkulator, ki računa vsoto dveh celih števil.

from tkinter import *

class Vsota():
    def __init__(self, master):
        # Naredimo spremenljivki, ki hranita vrednosti polj
        self.a = IntVar(master, value=3)
        # Ko se vrednost self.a spremeni, se mora poklicati self.izracunaj
        self.a.trace("w", self.izracunaj)

        self.b = IntVar(master, value=2)
        self.b.trace("w", self.izracunaj)

        polje_a = Entry(master, textvariable=self.a)
        polje_a.grid(row=0, column=0)

        Label(master, text="+").grid(row=0, column=1)

        polje_b = Entry(master, textvariable=self.b)
        polje_b.grid(row=0, column=2)

        Label(master, text=" = ").grid(row=0, column=3)

        self.c = IntVar(master, value=self.a.get() + self.b.get())
        polje_c = Label(master, textvariable=self.c)
        polje_c.grid(row=0, column=4)

    def izracunaj(self, name, index, mode):
        try:
            self.c.set(self.a.get() + self.b.get())
        except ValueError:
            self.c.set("nedefinirano")

# Glavnemu oknu rečemo "root" (koren), ker so grafični elementi
# organizirani v drevo, glavno okno pa je koren tega drevesa

# Naredimo glavno okno
root = Tk()

aplikacija = Vsota(root)

# Kontrolo prepustimo glavnemu oknu. Funkcija mainloop neha
# delovati, ko okno zapremo.
root.mainloop()
