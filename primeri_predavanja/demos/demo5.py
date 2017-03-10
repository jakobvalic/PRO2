# -*- encoding: utf-8 -*-

# Področje, na katerega lahko rišemo krogce.
# S pritiskom na levi gumb narišemo krogec.

from tkinter import *

class Krogci():
    def __init__(self, master):
        # Naredimo področje za risanje
        self.canvas = Canvas(master, width=300, height=300)
        self.canvas.pack()

        # Registiramo se za klike z levim gumbom na canvasu
        self.canvas.bind("<Button-1>", self.narisi_krogec)

    def narisi_krogec(self, event):
        '''Nariši krogec, kjer trenutno stoji miška.'''
        self.canvas.create_oval(event.x-5, event.y-5, event.x+5, event.y+5)


# Glavnemu oknu rečemo "root" (koren), ker so grafični elementi
# organizirani v drevo, glavno okno pa je koren tega drevesa

# Naredimo glavno okno
root = Tk()

aplikacija = Krogci(root)

# Kontrolo prepustimo glavnemu oknu. Funkcija mainloop neha
# delovati, ko okno zapremo.
root.mainloop()
