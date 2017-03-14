import tkinter as tk



class Semafor:

    def __init__(self, master):
        '''V okno postavi tri gumbe, enega zraven drugega.'''
        

        # ustvarimo podlago
        frame = tk.Frame(master)
        self.canvas = tk.Canvas(master, width=400, height=400)
        frame.pack()

        # ustvarimo gumbe
        gumb_zelena = tk.Button(frame, text = "Zelena", command = lambda: self.spremeni_barvo("green"))
        gumb_zelena.pack()

        gumb_rumena = tk.Button(frame, text = "Rumena", command = lambda: self.spremeni_barvo("yellow"))
        gumb_rumena.pack()

        gumb_rdeca = tk.Button(frame, text = "Rdeča", command = lambda: self.spremeni_barvo("red"))
        gumb_rdeca.pack()


    def spremeni_barvo(self, barva):
        '''Spremeni barvo ozadja.'''
        # root.configure(background = barva)
        root.configure(bg = barva)
    



# naredimo glavno okno
root = tk.Tk()

semafor = Semafor(root)

# dokler ne zapremo okna
root.mainloop()
