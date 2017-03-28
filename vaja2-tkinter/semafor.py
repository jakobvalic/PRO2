import tkinter as tk



class Semafor:

    def __init__(self, master):
        '''V okno postavi tri gumbe, enega zraven drugega.'''
        

        # ustvarimo podlago
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.grid(row = 2, column = 1)

        # ustvarimo gumbe
<<<<<<< HEAD
        gumb_zelena = tk.Button(text = "Zelena", command = lambda: self.spremeni_barvo("green"))
        gumb_zelena.grid(row = 1, column = 1, columnspan = 1)

        gumb_rumena = tk.Button(text = "Rumena", command = lambda: self.spremeni_barvo("yellow"))
        gumb_rumena.grid(row = 1, column = 2, columnspan = 1)

        gumb_rdeca = tk.Button(text = "Rdeča", command = lambda: self.spremeni_barvo("red"))
        gumb_rdeca.grid(row = 1, column = 3, columnspan = 1)
=======
        gumb_zelena = tk.Button(frame, text = "Zelena", command = lambda: self.spremeni_barvo("green"))
        gumb_zelena.pack()

        gumb_rumena = tk.Button(frame, text = "Rumena", command = lambda: self.spremeni_barvo("yellow"))
        gumb_rumena.pack()

        gumb_rdeca = tk.Button(frame, text = "Rdeča", command = lambda: self.spremeni_barvo("red"))
        gumb_rdeca.pack()
>>>>>>> 80d6b429a33173c45c04b2b0455a63135e0762fb


    def v_zeleno(self):
        self.canvas.config(bg = "green")
    
    def spremeni_barvo(self, barva):
        '''Spremeni barvo ozadja.'''
<<<<<<< HEAD
        self.canvas.config(background = barva)
        # root[bg] = barva
=======
        # root.configure(background = barva)
        root.configure(bg = barva)
>>>>>>> 80d6b429a33173c45c04b2b0455a63135e0762fb
    



# naredimo glavno okno
root = tk.Tk()

semafor = Semafor(root)

# dokler ne zapremo okna
root.mainloop()
