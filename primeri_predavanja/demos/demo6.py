# -*- encoding: utf-8 -*-

# Področje, na katerega lahko rišemo lomljeno črto.
# S pritiskom na levi gumb začnemo risati novo lomljeno črto,
# z desnim gumbom nadaljujemo prejšnjo črto.

from tkinter import *


class Crta():
    def __init__(self, master):
        # Trenutna točka, od koder bomo nadaljevali lomljeno
        # črto. Na začetku je ni.
        self.tocka = None

        # Naredimo področje za risanje
        self.canvas = Canvas(master, width=300, height=300)
        self.canvas.pack()

        # Registiramo se za klike z levim gumbom na canvasu
        self.canvas.bind("<Button-1>", self.nadaljuj_crto)

        # Registiramo se za klike z desnim gumbom na canvasu
        self.canvas.bind("<Button-2>", self.zacni_crto)


    def nadaljuj_crto(self, event):
        '''Nadaljuj lomljeno črto.'''
        if self.tocka is not None:
            (x, y) = self.tocka
            self.canvas.create_line(x, y, event.x, event.y)
            self.tocka = (event.x, event.y)


    def zacni_crto(self, event):
        '''Začni risati novo lomljeno črto.'''
        self.tocka = (event.x, event.y)
        self.canvas.create_oval(event.x-3, event.y-3, event.x+3, event.y+3)


# Glavnemu oknu rečemo "root" (koren), ker so grafični elementi
# organizirani v drevo, glavno okno pa je koren tega drevesa

# Naredimo glavno okno
root = Tk()

aplikacija = Crta(root)

# Kontrolo prepustimo glavnemu oknu. Funkcija mainloop neha
# delovati, ko okno zapremo.
root.mainloop()
