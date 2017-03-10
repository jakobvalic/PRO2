# -*- encoding: utf-8 -*-

# Področje, na katerem krogec sledi miški.

from tkinter import *

class Sledenje():
    def __init__(self, master):
        # Naredimo področje za risanje
        self.canvas = Canvas(master, width=300, height=300)
        self.canvas.pack()

        # Naredimo rdeč krogec in shranimo njegov id
        self.krogec = self.canvas.create_oval(145, 145, 155, 155, fill="red")

        # Registiramo se za premike miške
        self.canvas.bind("<Motion>", self.prestavi)

    def prestavi(self, event):
        '''Prestavi krogec tja, kjer je miška.'''
        (x,y) = (event.x, event.y)
        self.canvas.coords(self.krogec, x-5, y-5, x+5, y+5)

# Glavnemu oknu rečemo "root" (koren), ker so grafični elementi
# organizirani v drevo, glavno okno pa je koren tega drevesa

# Naredimo glavno okno
root = Tk()

aplikacija = Sledenje(root)

# Kontrolo prepustimo glavnemu oknu. Funkcija mainloop neha
# delovati, ko okno zapremo.
root.mainloop()
