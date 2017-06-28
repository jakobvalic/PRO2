import tkinter as tk
import math


def piramida(platno, n, x, y, d):
    '''Nariše piramido višine n z velikostjo stopnice d. Vrh je v (x, y).'''
    sez_ID = []
    for i in range(n + 1):
        x1 = x - (i + 1) * d
        y1 = y + i * d
        x2 = x + (i + 1) * d
        y2 = y + (i + 1) * d
        id = platno.create_rectangle((x1, y1),(x2, y2), fill = "orange", outline="", activefill = "blue")
        sez_ID.append(id)
    return sez_ID    

def tarca(platno, n, x, y, d):
    '''Nariše tarčo, sestavljeno iz n obročev debeline d,
    središča obročev so v točki (x, y), center vedno črn.'''
    # najprej je treba izračunati, kakšne barve naj bo zunanji
    sez_ID = []
    barva = ["black", "white"]
    indeks_barv = 0 if n % 2 == 0 else 1 # sod -> zunanji črn
    for i in range(n, -1, -1): # začeti je treba od zunaj, drugače bi prekrili notranjega
        x1 = x - (i + 1) * d
        y1 = y - (i + 1) * d
        x2 = x + (i + 1) * d
        y2 = y + (i + 1) * d
        id = platno.create_oval((x1, y1), (x2, y2), fill=barva[indeks_barv % 2])
        sez_ID.append(id)
        indeks_barv += 1
    return sez_ID


def trikotniki(platno, n, x, y, d):
    '''Nariše trikotnik Sierpinskega redan,
    (x, y) je spodnje levo oglišče, d dolžina osnovnice.'''
    if n == 1:
        id = platno.create_polygon((x, y), (x + d, y), (x + d / 2, y - d), fill="", outline="black")
        return [id]
    else: # v takih primerih raje else kot return
        s1 = trikotniki(platno, n - 1, x, y, d / 2)
        s2 = trikotniki(platno, n - 1, x + d / 2, y, d / 2)
        s3 = trikotniki(platno, n - 1, x + d / 4, y - d / 2, d / 2)
    return s1 + s2 + s3 # vračamo ID-je; ognemo se vmesnemu spravljanju v sez_ID, extend,.. -> [...] mora biti enojen
    
    
def torta(platno, podatki, x, y, r):
    '''Na platno nariše tortni diagram. (x, y) - središče torete, r - polmar torte.
    Največji kos odmaknjen od središča.'''
    sez_ID = []
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
            ID = platno.create_arc(x_novi - r, y_novi - r, x_novi + r, y_novi + r, start = zacetek_kota, 
                              extent=razpon, style=tk.PIESLICE, fill = barve[ind_barv % len(barve)])
            sez_ID.append(ID)
        else:
            ID = platno.create_arc(x - r, y - r, x + r, y + r, start = zacetek_kota, 
                              extent=razpon, style=tk.PIESLICE, fill = barve[ind_barv % len(barve)])
            sez_ID.append(ID)
        ind_barv += 1
        zacetek_kota += razpon
    return sez_ID

class Risanje:
    def __init__(self, master):
        # V __init__ damo vse objekte, menije in ukaze
        self.dim = 800
        self.platno = tk.Canvas(master, width=self.dim, height=self.dim)
        self.platno.pack(side=tk.RIGHT)
        self.zgo_risanja = []
        self.premikamo = None


        # Ustvarimo menu in podmenuje
        menu = tk.Menu(master)
        menuNarisi = tk.Menu(menu, tearoff=0)
        menuPobrisi = tk.Menu(menu, tearoff=0)

        # Dodamo ukaze
        menuNarisi.add_command(label="Nariši piramido", command=self.piramida)
        menuNarisi.add_command(label="Nariši tarčo", command=self.tarca)
        menuNarisi.add_command(label="Nariši trikotnike", command=self.trikotniki)
        menuNarisi.add_command(label="Nariši torto", command=self.torta)
        
        menuPobrisi.add_command(label="Pobriši enega", command=self.pobrisi_enega)
        menuPobrisi.add_command(label="Pobriši vse", command=self.pobrisi_vse)

        # Okno skonfiguriramo tako, da vsebuje željeni menu in podmenuje
        master.config(menu=menu)
        menu.add_cascade(label="Nariši", menu=menuNarisi)
        menu.add_cascade(label="Pobriši", menu=menuPobrisi)


        # Ustvarimo okno za parametre
        okno = tk.Frame(master)
        okno.pack()
        # Napisi
        tk.Label(okno, text="Parametri").grid(row=1, column=1)
        tk.Label(okno, text="Položaj x:").grid(row=2, column=1)
        tk.Label(okno, text="Položaj y:").grid(row=3, column=1)
        tk.Label(okno, text="Velikost").grid(row=4, column=1)
        # Vnosna polja
        self.parametri = tk.Entry(okno)
        self.parametri.grid(row=1, column=2)
        self.polozaj_x = tk.Entry(okno)
        self.polozaj_x.grid(row=2, column=2)
        self.polozaj_y = tk.Entry(okno)
        self.polozaj_y.grid(row=3, column=2)
        self.velikost = tk.Entry(okno)
        self.velikost.grid(row=4, column=2)

        # Registriramo se za klik z miško
        self.platno.bind('<Button-1>', self.kateri_lik)
        self.platno.bind('<B1-Motion>', self.premakni_lik)

        # Iz konstruktorja takoj narišemo like, če bi želeli
        # piramida(self.platno, 10, self.dim/2, 50, 20)
        # tarca(self.platno, 50, self.dim / 2, self.dim / 2, 20)
        # trikotniki(self.platno, 8, 10, self.dim, 700)
        # torta(self.platno, [8, 3, 5, 7], self.dim / 2, self.dim / 2, 200)

    def kateri_lik(self, event):
        self.x, self.y = event.x, event.y
        liki = self.platno.find_overlapping(self.x, self.y, self.x+1, self.y+1)
        if len(liki) != 0:
            id = liki[-1]
            for lik in self.zgo_risanja:
                if id in lik:
                    self.premikamo = lik
        else:
            self.premikamo = None
        

    def premakni_lik(self, event):
        
        if self.premikamo is not None:
            dx, dy = event.x - self.x, event.y - self.y
            for elt in self.premikamo:
                self.platno.move(elt, dx, dy)
        self.x, self.y = event.x, event.y
        

    def piramida(self):
        n = int(self.parametri.get() or 10)
        x = int(self.polozaj_x.get() or self.dim/2)
        y = int(self.polozaj_y.get() or 50)
        d = int(self.velikost.get() or 20)
        id = piramida(self.platno, n, x, y, d)
        self.zgo_risanja.append(id)

    def tarca(self):
        n = int(self.parametri.get() or 50)
        x = int(self.polozaj_x.get() or self.dim/2)
        y = int(self.polozaj_y.get() or self.dim/2)
        d = int(self.velikost.get() or 20)
        id = tarca(self.platno, n, x, y, d)
        self.zgo_risanja.append(id)

    def trikotniki(self):
        n = int(self.parametri.get() or 8)
        x = int(self.polozaj_x.get() or 10)
        y = int(self.polozaj_y.get() or self.dim)
        d = int(self.velikost.get() or 700)
        id = trikotniki(self.platno, n, x, y, d)
        self.zgo_risanja.append(id)

    def torta(self):
        sez_parametrov = list(map(int,(self.parametri.get().split() or [8, 3, 5, 7])))
        x = int(self.polozaj_x.get() or self.dim/2)
        y = int(self.polozaj_y.get() or self.dim/2)
        d = int(self.velikost.get() or 200)
        id = torta(self.platno, sez_parametrov, x, y, d)
        self.zgo_risanja.append(id)


    def pobrisi_enega(self):
        if self.zgo_risanja != []:
            zadnji = self.zgo_risanja.pop()
            for elt in zadnji:
                self.platno.delete(elt)

    def pobrisi_vse(self):
        self.platno.delete(tk.ALL)
        
        
        
        



        



root = tk.Tk()

app = Risanje(root)


root.mainloop()



