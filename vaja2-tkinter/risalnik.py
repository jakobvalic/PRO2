import tkinter as tk



class Risalnik():

    def __init__(self, master):
        '''Definira risanje z miško.'''
            
        self.canvas = tk.Canvas(master, width = 300, height = 300)
        self.canvas.pack()

        self.tocka = None


        # registriramo se za klik in premik miške
        self.canvas.bind("<B1-Motion>", self.risi)

        # ko spustimo miško
        self.canvas.bind("<ButtonRelease-1>", self.spusti)


    def risi(self, event):
        '''Riše črto.'''
        if self.tocka is None:
            self.tocka = (event.x, event.y) # od kje začnemo risati
        (x, y) = self.tocka
        self.canvas.create_line(x, y, event.x, event.y)
        self.tocka = (event.x, event.y)
        
        
    def spusti(self, event):
        '''Ponastavi točko na None.'''
        self.tocka = None

    def pobrisi(self):
        '''Počisti risalno površino.'''
        self.canvas.delete("all")



# naredimo glavno okno
root = tk.Tk()

risalnik = Risalnik(root)

# dokler ne zapremo okna
root.mainloop()
