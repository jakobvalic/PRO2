# -*- encoding: utf-8 -*-

# Aplikacija, ki odpre okno, ter vanj postavi dva guma in števec

from tkinter import *

class Stevec():
    def __init__(self, master):
        '''V okno master postavi dva gumba in števec.'''
        
        # Stanje števca je na začetku 0
        self.stevec = 0
       
        # Najprej naredimo grafični element Frame, ki služi kot
        # "kontejner", v katerega postavimo gumbe in napise
        frame = Frame(master) # Ta okvir je vsebovan v master-ju
        frame.pack()          # To dejansko naredi vsebino vidno

        gumb_povecaj = Button(frame, text="Povecaj!", command=self.povecaj)
        gumb_povecaj.pack()

        gumb_zmanjsaj = Button(frame, text="Zmanjsaj!", command=self.zmanjsaj)
        gumb_zmanjsaj.pack()

        self.napis_stevec = StringVar(value=str(self.stevec))
        label_stevec = Label(frame, textvariable=self.napis_stevec)
        label_stevec.pack()


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

stevec = Stevec(root)

# Kontrolo prepustimo glavnemu oknu. Funkcija mainloop neha
# delovati, ko okno zapremo.
root.mainloop()
