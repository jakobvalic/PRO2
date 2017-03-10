# Primer objektnega programiranja

import random

class Virus():
    def __init__(self, laboratorij, max_starost, kuznost, inkubacija):
        self.laboratorij = laboratorij # virus je v tem laboratoriju
        self.max_starost = max_starost # starejsi od toliko umre
        self.kuznost = kuznost # verjetnost, da uspesno napade celico
        self.inkubacija = inkubacija # kako dolgo je v celici, preden deluje
        self.rojstvo = laboratorij.zdaj()

    def __repr__(self):
        return '[virus {0}]'.format(self.rojstvo)

    def starost(self):
        '''Trenutna starost virusa'''
        return self.laboratorij.zdaj() - self.rojstvo

    def klon(self):
        '''Vrni kopijo virusa, ki ima rojstvo nastavljeno na trenutni cas.'''
        return Virus(self.laboratorij, self.max_starost,
                     self.kuznost, self.inkubacija)

    def naredi_korak(self):
        # Ce je virus prestar, odmre
        if self.starost() >= self.max_starost:
            self.laboratorij.odstrani_virus(self)
        else:
            # Naključno izberi celico in jo poskusi okuziti
            c = self.laboratorij.nakljucna_celica()
            if c is not None:
                if random.random() <= self.kuznost:
                    c.okuzi(self)

class Celica():
    def __init__(self, laboratorij, max_starost):
        self.laboratorij = laboratorij # celica je v tem okolju
        self.max_starost = max_starost # pri tej starosti se razdeli
        self.rojstvo = laboratorij.zdaj()
        self.parazit = None # Virus, ki jo je okuzil, ali None
        self.okuzba_ob = None # Kdaj se je celica okužila

    def __repr__(self):
        if self.parazit:
            return '[celica {0}, okuzba={1}]'.format(
                self.rojstvo, self.cas_okuzbe)
        else:
            return '[celica {0}]'.format(self.rojstvo)

    def okuzi(self, v):
        '''Virus v okuži celico self.'''
        if self.parazit is None:
            self.parazit = v
            self.okuzba_ob = self.laboratorij.zdaj()

    def starost(self):
        '''Vrni trenutno starost celice.'''
        return self.laboratorij.zdaj() - self.rojstvo

    def klon(self):
        '''Vrni kopijo celice, ki ima rojstvo nastavljeno na trenutni čas.'''
        assert (self.parazit is None) # ne smemo se klonirati okuženi
        return Celica(self.laboratorij, self.max_starost)

    def cas_okuzbe(self):
        '''Vrni cas okuzbe. Povzroči napako, če se kliče na neokuženi celici.'''
        assert (self.okuzba_ob is not None)
        return (self.laboratorij.zdaj() - self.okuzba_ob)

    def je_okuzena(self):
        return (self.parazit is not None)

    def naredi_korak(self):
        if self.je_okuzena():
            if self.cas_okuzbe() >= self.parazit.inkubacija:
                # nastaneta nova virusa, ta celica odmre
                self.laboratorij.dodaj_virus(self.parazit.klon())
                self.laboratorij.dodaj_virus(self.parazit.klon())
                self.laboratorij.odstrani_celico(self)
        elif self.starost() >= self.max_starost:
            # Se razdelimo
            self.laboratorij.dodaj_celico(self.klon())
            self.laboratorij.dodaj_celico(self.klon())
            self.laboratorij.odstrani_celico(self)


class Laboratorij():
    def __init__(self, virusi, celice):
        self.cas = 0
        self.virusi = virusi
        self.celice = celice

    def __repr__(self):
        return "cas = {0}, celice = {1}, virusi = {2}".format(
            self.zdaj(),
            len(self.celice),
            len(self.virusi))

    def zdaj(self):
        '''Vrni trenutni čas.'''
        return self.cas

    def naredi_korak(self):
        '''Izvedi en naredi_korak simulacije.'''
        self.cas += 1
        # V vsaki celici naredimo en naredi_korak simulacije
        # POZOR: ker simulacija spreminja seznam self.celice, mora
        # zanka for potekati po kopiji seznama, ki ga dobimo s self.celice[:]
        for c in self.celice[:]:
            c.naredi_korak()
        # V vsakem virusu naredimo en naredi_korak simulacije
        for v in self.virusi[:]:
            v.naredi_korak()

    def nakljucna_celica(self):
        '''Vrni naključno celico, ali None, če ni nobene.'''
        if len(self.celice) == 0:
            return None
        else:
            return random.choice(self.celice)

    def dodaj_celico(self, c):
        self.celice.append(c)

    def odstrani_celico(self, c):
        self.celice.remove(c)

    def dodaj_virus(self, v):
        self.virusi.append(v)

    def odstrani_virus(self, v):
        self.virusi.remove(v)

# Glavni program
lab = Laboratorij([], [])
# Matična celica
c = Celica(lab, 3)
lab.dodaj_celico(c)
# Matični virus
v = Virus(lab, 3, 0.6, 1)
lab.dodaj_virus(v)
while len(lab.celice) > 0 or len(lab.virusi) > 0:
    print (lab)
    lab.naredi_korak()
