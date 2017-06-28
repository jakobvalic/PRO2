# -*- encoding: utf-8 -*-

# Aplikacija, ki odpre okno, ter vanj postavi števec, dva gumba in meni.
# Edina razlika med to aplikacijo in demo2.py je dodani menu.

from tkinter import *

class Stevec():
    def __init__(self, master):
        '''V okno master postavi dva gumba in števec.'''

        # Stanje števca je na začetku 0
        self.stevec = 0

        # Glavni menu
        menu = Menu(master)
        master.config(menu=menu) # Dodamo menu

        # Naredimo podmenu "File"
        file_menu = Menu(menu)
        menu.add_cascade(label="File", menu=file_menu)

        # Dodamo izbire v file_menu
        file_menu.add_command(label="Izbira 1", command=self.izbira1)
        file_menu.add_command(label="Izbira 2", command=self.izbira2)
        file_menu.add_separator() # To doda separator v menu
        file_menu.add_command(label="Quit", command=master.destroy)

        # Naredimo podemnu "Edit"
        edit_menu = Menu(menu)
        menu.add_cascade(label="Edit", menu=edit_menu)

        # Dodamo izbire v edit_menu. Te izbire ne delajo ničesar,
        # ker nismo nastavili command=...
        edit_menu.add_command(label="Copy")
        edit_menu.add_command(label="Cut")
        edit_menu.add_command(label="Paste")
        edit_menu.add_command(label="Delete")

        # Najprej naredimo grafični element Frame, ki služi kot
        # "kontejner", v katerega postavimo gumbe in napise
        frame = Frame(master) # Ta okvir je vsebovan v master-ju
        frame.pack()          # To dejansko naredi vsebino vidno

        gumb_povecaj = Button(frame, text=" +1 ", command=self.povecaj)
        gumb_povecaj.pack()

        gumb_zmanjsaj = Button(frame, text=" -1 ", command=self.zmanjsaj)
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

    def izbira1(self):
        '''Se izvede, ko izberemo izbiro 1 iz menuja.'''
        print('Izbrali ste izbiro 1. To je odlična izbira!')

    def izbira2(self):
        '''Se izvede, ko izberemo izbiro 2 iz menuja.'''
        print('Izbrali ste izbiro 2. To je super izbira!')


# Naredimo glavno okno
root = Tk()

aplikacija = Stevec(root)

# Kontrolo prepustimo glavnemu oknu. Funkcija mainloop neha
# delovati, ko okno zapremo.
root.mainloop()
