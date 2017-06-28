#!/usr/bin/python
# -*- encoding: utf-8 -*-

from tkinter import *
import random
import time

# Gravitacija
g = 9.8 * 10  # 1 meter = 10 točk na zaslonu

# Preprost primer animacije s Tkinter.

class Krogla():
    '''Krogla, ki se premika v pravokotniku dane širine in višine.
    Začetna pozicija in hitrost sta izbrani naključno.'''

    # POZOR: os y še vedno kaže navzdol!

    def __init__(self, r, width, height):
        self.width = width
        self.height = height
        self.r = r
        # Začetna pozicija
        self.x = random.uniform(r, width - r)
        self.y = random.uniform(r, height - r)
        # Začetna hitrost
        self.vx = random.uniform(-width/3, width/3)
        self.vy = random.uniform(-height/2, height/2)

    def energija(self):
        return 0.5 * (self.vx * self.vx + self.vy * self.vy) - g * self.y

    def premakni(self, dt):
        '''Izračunaj novo stanje krogle po preteku časa dt.'''
        self.x = self.x + self.vx * dt
        self.y = self.y + self.vy * dt + 0.5 * g * dt * dt
        self.vy = self.vy + g * dt        # os y kaže navzdol!
        # Preverimo odboje
        if self.x - self.r < 0:
            self.vx = -self.vx
        if self.x + self.r > self.width:
            self.vx = -self.vx
        if self.y - self.r < 0:
            self.vy = -self.vy
        if self.y + self.r > self.height:
            self.vy = -self.vy

class Boing():
    def __init__(self, master):
        width = 300
        height = 300
        self.energija = DoubleVar(master)
        Label(master, textvariable=self.energija).grid(row=1, column=0)
        self.dt = 0.05
        self.krogla = Krogla(30, width, height)
        self.canvas = Canvas(master, width=width, height=height)
        self.canvas.grid(row=0, column=0)
        self.krogla_id = self.canvas.create_oval(self.krogla.x - self.krogla.r,
                                                 self.krogla.y - self.krogla.r,
                                                 self.krogla.x + self.krogla.r,
                                                 self.krogla.y + self.krogla.r,
                                                 fill = "red")
        # Zaženemo animacijo
        self.zadnji_cas = time.time()
        self.animacija()

    def animacija(self):
        """Naredimo en korak animacije."""
        trenutni_cas = time.time()
        dt = trenutni_cas - self.zadnji_cas
        print (dt - self.dt)
        self.zadnji_cas = trenutni_cas
        self.krogla.premakni(dt)
        self.energija.set(self.krogla.energija())
        self.canvas.coords(self.krogla_id,
                           self.krogla.x - self.krogla.r,
                           self.krogla.y - self.krogla.r,
                           self.krogla.x + self.krogla.r,
                           self.krogla.y + self.krogla.r)
        self.canvas.after(int(self.dt * 1000), self.animacija)


# Glavnemu oknu rečemo "root" (koren), ker so grafični elementi
# organizirani v drevo, glavno okno pa je koren tega drevesa

# Naredimo glavno okno
root = Tk()

root.title("Boing")

aplikacija = Boing(root)

# Kontrolo prepustimo glavnemu oknu. Funkcija mainloop neha
# delovati, ko okno zapremo.
root.mainloop()
