import tkinter as tk
import math
import time



class Ura():

    def __init__(self, master):
        '''Nariše uro in definira njeno premikanje.'''

        self.velikost = 800
        self.center = self.velikost / 2
        self.radij = self.velikost / 2

        self.canvas = tk.Canvas(master, width = self.velikost, height = self.velikost)
        self.canvas.pack()

        # številčnica
        self.canvas.create_oval(0, 0, self.velikost, self.velikost)
        self.canvas.create_oval(self.center + 5, self.center + 5, self.center - 5, self.center - 5)

        stevila = [i for i in range(1, 13)]
        fi = 3 / 2 * math.pi + math.pi / 6
        odmik_ure = 20
        for i in range(12): # narišemo števila
            x_teksta = self.center + (self.radij - odmik_ure) * math.cos(fi)
            y_teksta = self.center + (self.radij - odmik_ure) * math.sin(fi)
            self.canvas.create_text(x_teksta, y_teksta, text = str(stevila[i]), font = '24px')
            fi += math.pi / 6
            
        
        
        # sekundni kazalec
        odmik_kazalca = 20
        self.obodna_tocka = (self.center, self.center - self.radij)
        self.id = self.canvas.create_line(self.center, self.center, self.obodna_tocka)
    

    
    def anim(self):
        # spremenimo koordinate sekundnega kazalca
        (x, y) = self.obodna_tocka
        self.obodna_tocka = x + self.radij * 2 * math.pi / 60, y + self.radij * 2 * math.pi / 60
        self.canvas.coords(self.id, self.center, self.center, x + self.radij * 2 * math.pi / 60, y + self.radij * 2 * math.pi / 60)

        self.canvas.after(1000, self.anim)
        
        


##         
##        self.obodna_tocka = (center + radij * math.cos(fi), center + radij * math.sin(fi))
##
##
##        
##

##

        

        
# naredimo glavno okno
root = tk.Tk()

ura = Ura(root)
ura.anim()

# dokler ne zapremo okna
root.mainloop()
