import tkinter as tk



class Semafor:

    def __init__(self, master):
        '''V okno postavi tri gumbe, enega zraven drugega.'''
        
        # ustvarimo podlago
        self.canvas = tk.Canvas(master, width=400, height=400)
        self.canvas.grid(row = 2, column = 1, columnspan = 3)

        # ustvarimo gumbe
        gumb_zelena = tk.Button(text = "Zelena", command = lambda: self.spremeni_barvo("green"))
        gumb_zelena.grid(row = 1, column = 1)

        gumb_rumena = tk.Button(text = "Rumena", command = lambda: self.spremeni_barvo("yellow"))
        gumb_rumena.grid(row = 1, column = 2)

        gumb_rdeca = tk.Button(text = "Rdeča", command = lambda: self.spremeni_barvo("red"))
        gumb_rdeca.grid(row = 1, column = 3)



    def spremeni_barvo(self, barva):
        '''Spremeni barvo ozadja.'''
        # root.configure(background = barva)
        self.canvas.configure(bg = barva)
    



# naredimo glavno okno
root = tk.Tk()

semafor = Semafor(root)

# dokler ne zapremo okna
root.mainloop()
