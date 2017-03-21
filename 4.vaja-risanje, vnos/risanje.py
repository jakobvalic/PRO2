import tkinter as tk
import math


def piramida(platno, n, x, y, d):
    '''Nariše piramido višine n z velikostjo stopnice d. Vrh je v (x, y).'''
    for i in range(n + 1):
        x1 = x - (i + 1) * d
        y1 = y + i * d
        x2 = x + (i + 1) * d
        y2 = y + (i + 1) * d
        platno.create_rectangle((x1, y1),(x2, y2), fill = "orange", outline="", activefill = "blue")

def tarca(platno, n, x, y, d):
    '''Nariše tarčo, sestavljeno iz n obročev debeline d,
    središča obročev so v točki (x, y), center vedno črn.'''
    # najprej je treba izračunati, kakšne barve naj bo zunanji
    barva = ["black", "white"]
    indeks_barv = 0 if n % 2 == 0 else 1 # sod -> zunanji črn
    for i in range(n, -1, -1): # začeti je treba od zunaj, drugače bi prekrili notranjega
        x1 = x - (i + 1) * d
        y1 = y - (i + 1) * d
        x2 = x + (i + 1) * d
        y2 = y + (i + 1) * d
        platno.create_oval((x1, y1), (x2, y2), fill=barva[indeks_barv % 2])
        indeks_barv += 1


def trikotniki(platno, n, x, y, d):
    '''Nariše trikotnik Sierpinskega redan,
    (x, y) je spodnje levo oglišče, d dolžina osnovnice.'''
    if n == 1:
        platno.create_polygon((x, y), (x + d, y), (x + d / 2, y - d), fill="", outline="black")
    else: # v takih primerih raje else kot return
        trikotniki(platno, n - 1, x, y, d / 2)
        trikotniki(platno, n - 1, x + d / 2, y, d / 2)
        trikotniki(platno, n - 1, x + d / 4, y - d / 2, d / 2)
    
def torta(platno, podatki, x, y, r):
    '''Na platno nariše tortni diagram. (x, y) - središče torete, r - polmar torte.
    Največji kos odmaknjen od središča.'''
    barve = ["yellow", "blue", "red", "orange"]
    vsota = sum(podatki)
    najvecji = max(podatki)
    ind_barv = 0
    zacetek_kota = 0
    for kos in podatki:
        razpon = 360 * kos / vsota # koliko stopinj pripada kosu
        if kos == max(podatki):
            # premaknemo za izhodišče v smeri simetrale
            simetrala = zacetek_kota + razpon / 2
            simetrala_v_rad = simetrala * 2 * math.pi / 360
            x_novi = x + (r / 10) * math.cos(simetrala_v_rad)
            y_novi = y - (r / 10) * math.sin(simetrala_v_rad)
            platno.create_arc(x_novi - r, y_novi - r, x_novi + r, y_novi + r, start = zacetek_kota, 
                              extent=razpon, style=tk.PIESLICE, fill = barve[ind_barv % len(barve)])
        else:
            platno.create_arc(x - r, y - r, x + r, y + r, start = zacetek_kota, 
                              extent=razpon, style=tk.PIESLICE, fill = barve[ind_barv % len(barve)])
        ind_barv += 1
        zacetek_kota += razpon

class Risanje:
    def __init__(self, master):
        self.dim = 800
        self.platno = tk.Canvas(master, width=self.dim, height=self.dim)
        self.platno.pack()


        # iz konstruktorja pokličemo funkcije
        # piramida(self.platno, 10, self.dim/2, 50, 20)
        # tarca(self.platno, 50, self.dim / 2, self.dim / 2, 20)
        # trikotniki(self.platno, 8, 10, self.dim, 700)
        torta(self.platno, [8, 3, 5, 7], self.dim / 2, self.dim / 2, 200)
        



root = tk.Tk()

app = Risanje(root)


root.mainloop()



