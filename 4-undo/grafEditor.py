#!/usr/bin/python
# -*- encoding: utf-8 -*-

# Graf editor

from tkinter import *
from tkinter import messagebox

def sredisce(lst):
    """Središče krogca na Canvasu z danim bounding box."""
    (x1, y1, x2, y2) = lst
    return ((x1+x2)/2, (y1+y2)/2)

class Graf():
    def __init__(self, canvas, r=7):
        self.canvas = canvas # canvas, na katerega rišemo
        self.r = r # polmer krogca, ki označuje vozlišče
        self.vozlisca = [] # seznam vseh vozlišč
        self.povezave = {} # za vsako povezavo, množica njenih krajišč
        self.aktivna_vozlisca = [] # trenutno označena vozlišča

    def dodaj_vozlisce(self, x, y):
        v = self.canvas.create_oval(x-self.r, y-self.r, x+self.r, y+self.r, fill="white")
        self.vozlisca.append(v)
        return v

    def odstrani_vozlisce(self, v):
        self.canvas.delete(v)
        # NB: s tuple naredimo kopijo, ker bomo brisali povezave
        for (p, vs) in tuple(self.povezave.items()):
            if v in vs:
                self.odstrani_povezavo(p)
        self.vozlisca.remove(v)

    def odstrani_aktivna_vozlisca(self):
        for v in self.aktivna_vozlisca:
            self.odstrani_vozlisce(v)
        self.aktivna_vozlisca = []

    def dodaj_povezavo(self, v1, v2):
        # Če povezava že obstaja, ne naredimo nič
        for vs in self.povezave.values():
            if (v1 in vs) and (v2 in vs): return
        # Dodamo povezavo
        (x1, y1) = sredisce(self.canvas.coords(v1))
        (x2, y2) = sredisce(self.canvas.coords(v2))
        p = self.canvas.create_line(x1, y1, x2, y2, width=3)
        self.canvas.tag_lower(p) # Povezavo postavimo pod vozlišča
        self.povezave[p] = {v1, v2}
        return p

    def odstrani_povezavo(self, p):
        self.canvas.delete(p)
        del self.povezave[p]

    def premakni_vozlisce(self, v, x, y):
        # Prestavi vozlišče v na nove koordinate
        self.canvas.coords(v, x-self.r, y-self.r, x+self.r, y+self.r)
        # Premakni povezave, ki imajo v za krajišče
        for (p, vs) in self.povezave.items():
            if v in vs:
                (v1, v2) = tuple(vs)
                (x1, y1) = sredisce(self.canvas.coords(v1))
                (x2, y2) = sredisce(self.canvas.coords(v2))
                self.canvas.coords(p, x1, y1, x2, y2)

    def oznaci_vozlisce(self, v):
        if v in self.aktivna_vozlisca:
            self.aktivna_vozlisca.remove(v)
            self.canvas.itemconfigure(v, fill="white")
        else:
            self.aktivna_vozlisca.append(v)
            self.canvas.itemconfigure(v, fill="red")

    def deaktiviraj_vsa_vozlisca(self):
        for v in self.aktivna_vozlisca:
            self.canvas.itemconfigure(v, fill="white")
        self.aktivna_vozlisca = []

    def za_shrambo(self):
        vs = []
        ps = []
        for v in self.vozlisca:
            koordinate = self.canvas.coords(v)
            center = sredisce(koordinate)
            vs.append((v, *center))
        for p in self.povezave.values():
            ps.append(tuple(p))
        # print(vs, '\n', ps)
        return vs, ps
            
            

class GrafEditor():
    def __init__(self, master, width=500, height=500):

        self.zgodovina = []
        
        # Poskrbimo, da se vsebina glavnega okna razteguje,
        # ko uporabnik spremeni velikost okna
        top = master.winfo_toplevel()
        top.rowconfigure(0, weight=1)
        top.columnconfigure(0, weight=1)
        master.rowconfigure(0, weight=1) # Vrstica 0 je raztegljiva
        master.columnconfigure(0, weight=1) # Stolpec 0 je raztegljiv

        # Postavimo glavni menu
        menu = Menu(master)
        master.config(menu = menu)

        # Podmenu z ukazi
        ukazi_menu = Menu(menu)
        menu.add_cascade(label="Ukazi", menu=ukazi_menu)
        ukazi_menu.add_command(label="Zbriši", command=self.zbrisi_graf)
        ukazi_menu.add_command(label="Pomoč", command=self.pomoc)

        # Postavimo canvas
        self.canvas = Canvas(master, width=width, height=height)
        self.canvas.grid(row=0, column=0, sticky=N+S+E+W)
        self.canvas.focus_set()

        # Naredimo prazen graf
        self.graf = Graf(self.canvas)

        # Vozlišče, ki ga premikamo
        self.premikamo_vozlisce = None

        # id ukaza bind, ki ga moramo razveljaviti, ko je konec premikanja
        self.premikamo_vozlisce_bind = None

        # Vežemo ukaze na dogodke
        self.canvas.bind('<Button-1>', self.dodaj_ali_oznaci_vozlisce)
        self.canvas.bind('<Shift-ButtonPress-1>', self.zacni_premik_vozlisca)
        self.canvas.bind('<Shift-ButtonRelease-1>', self.koncaj_premik_vozlisca)
        self.canvas.bind('<Escape>', self.deaktiviraj_vozlisca)
        self.canvas.bind('<BackSpace>', self.odstrani_vozlisca)
        self.canvas.bind('<Delete>', self.odstrani_vozlisca)
        self.canvas.bind('<Tab>', self.dodaj_povezavo)
        self.canvas.bind('<Control-z>', lambda x: self.razveljavi()) # lahko pa ...bind('<Control-z>', self.razveljavi)
                                                                     # in dodamo en argument pri def razveljavi(self, event)

    def najblizje_vozlisce(self, x, y):
        for v in self.canvas.find_closest(x, y):
            if v in self.graf.vozlisca:
                (x1, y1, x2, y2) = self.canvas.coords(v)
                if x1 <= x and x <= x2 and y1 <= y and y <= y2:
                    return v
        return None

    def dodaj_ali_oznaci_vozlisce(self, event):
        v = self.najblizje_vozlisce(event.x, event.y)
        if v is None:
            self.shrani()
            self.graf.dodaj_vozlisce(event.x, event.y)
        else:
            self.graf.oznaci_vozlisce(v)

    def deaktiviraj_vozlisca(self, event):
        self.graf.deaktiviraj_vsa_vozlisca()

    def odstrani_vozlisca(self, event):
        self.shrani()
        self.graf.odstrani_aktivna_vozlisca()

    def zacni_premik_vozlisca(self, event):
        v = self.najblizje_vozlisce(event.x, event.y)
        if v is not None:
            self.shrani()
            self.premikamo_vozlisce = v
            self.premikamo_vozlisce_bind = self.canvas.bind('<Motion>', self.premakni_vozlisce)

    def koncaj_premik_vozlisca(self, event):
        self.premikamo_vozlisce = None
        if self.premikamo_vozlisce_bind is not None:
            self.canvas.unbind(self.premikamo_vozlisce_bind)
        self.premikamo_vozlisce_bind = None

    def premakni_vozlisce(self, event):
        if self.premikamo_vozlisce is not None:
            self.graf.premakni_vozlisce(self.premikamo_vozlisce, event.x, event.y)

    def dodaj_povezavo(self, event):
        if len(self.graf.aktivna_vozlisca) >= 2:
            self.shrani() # shranimo pred dodajanjem
            p = self.graf.aktivna_vozlisca[0]
            for q in self.graf.aktivna_vozlisca[1:]:
                self.graf.dodaj_povezavo(p, q)
                p = q
            self.graf.deaktiviraj_vsa_vozlisca()

    def zbrisi_graf(self, shrani = True):
        if shrani:
            self.shrani()
        self.graf = Graf(self.canvas)
        self.premikamo_vozlisce = None
        if self.premikamo_vozlisce_bind:
            self.canvas.unbind(self.premikamo_vozlisce_bind)
        self.canvas.delete(ALL)

    def razveljavi(self):
        '''Pobriše trenutni graf in ga nadomesti z zadnjim iz zgodovoine iz seznama.'''
        print('Razveljavljam...')
        if self.zgodovina == []:
            return
        (vs, ps) = self.zgodovina.pop()
        self.zbrisi_graf(False)
        # nazaj narišemo vozlišča in povezava; to storimo s pomočjo Graf (le na canvasu)
        sl_novih_id = dict()
        for v in vs:
            id_vozlisca, x, y = v
            nov_id = self.graf.dodaj_vozlisce(x, y)        
            sl_novih_id[id_vozlisca] = nov_id
        for p in ps: # nariše črto med dvemi točkami s podanim ID-jem
            v1, v2 = p
            nov_v1, nov_v2 = sl_novih_id[v1], sl_novih_id[v2]
            self.graf.dodaj_povezavo(nov_v1, nov_v2)
        

    def shrani(self):
        '''V seznam self.zgodovina doda trenutni graf.'''
        self.zgodovina.append(self.graf.za_shrambo())
        print(self.zgodovina)
        

    def pomoc(self):
        messagebox.showinfo(title="Navodila", message="""
Urejevalnik grafov.

klik: dodaj/označi vozlišče
shift+premik: premakni vozlišče
Delete: zbriši označena vozlišča
Esc: odznači  vozlišča
Tab: dodaj povezavo""")

# GLAVNI PROGRAM

root = Tk()
root.title("Graf editor")
app = GrafEditor(root)
root.mainloop()
