# -*- encoding: utf-8 -*-

# Aplikacija, ki odpre okno, ter vanj postavi dva guma in števec.
# Edina razlika med to aplikacijo in demo2.py je razporeditev
# elementov, ki so tu postavljeni vodoravno.

from tkinter import *

class Stevec():
    def __init__(self, master):
        '''V okno master postavi dva gumba in števec.'''
        
        # Stanje števca je na začetku 0
        self.stevec = 0
       
        # Namesto Frame() in pack() uporabimo grid()

        # POZOR: če uporabite hkrati pack() in grid(), bo Tkinter
        # v neskončost "računal" razporeditev elementov!

        gumb_povecaj = Button(master, text=" +1 ", command=self.povecaj)
        gumb_povecaj.grid(row=0, column=0)

        gumb_zmanjsaj = Button(master, text=" -1 ", command=self.zmanjsaj)
        gumb_zmanjsaj.grid(row=1, column=1)

        self.napis_stevec = StringVar(value=str(self.stevec))
        label_stevec = Label(master, textvariable=self.napis_stevec)
        label_stevec.grid(row=2, column=0)

    def povecaj(self):
        '''Povečaj števec za 1.'''
        self.stevec = self.stevec + 1
        self.napis_stevec.set(str(self.stevec))


    def zmanjsaj(self):
        '''Zmanjšaj števec za 1.'''
        self.stevec = self.stevec - 1
        self.napis_stevec.set(str(self.stevec))




# Naredimo glavno okno
root = Tk()

aplikacija = Stevec(root)

# Kontrolo prepustimo glavnemu oknu. Funkcija mainloop neha
# delovati, ko okno zapremo.
root.mainloop()
