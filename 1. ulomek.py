# Ulomek

def gcd(a, b):
    '''GCD s sprotnim nižanjem števil a in b.'''
    delitelj = 2
    najD = 1
    while a != 1 and b != 1 and delitelj <= min(a, b):
        if a % delitelj == 0 and b % delitelj == 0:
            a //= delitelj
            b //= delitelj
            najD *= delitelj
        else:
            delitelj += 1
    return najD

def gcdVgrajeni(a, b):
    '''Vgrajen algoritem: from fractions import gcd.'''
    while b:
        a, b = b, a%b
    return a

for a in range(1, 100): # Preverimo usklajenost algoritmov
    for b in range(1, 300):
        assert gcd(a, b) == gcdVgrajeni(a, b)


def okrajsaj(st, im):
    '''Okrajša ulomek.'''
    najD = gcdVgrajeni(st, im)
    okrajsan_st = st // najD
    okrajsan_im = im // najD
    assert gcd(okrajsan_st, okrajsan_im) == 1 # Zagotovimo se, da funkcija gcd deluje pravilno
    return okrajsan_st, okrajsan_im


class Ulomek:
    def __init__(self, stevec, imenovalec = 1):
        try:
            stevec / imenovalec
        except:
            raise ValueError('Deljenje z 0 ni mogoče.')
        okrajsani_stevec, okrajsani_imenovalec = okrajsaj(stevec, imenovalec)
        self.stevec = okrajsani_stevec
        self.imenovalec = okrajsani_imenovalec
        
    def __repr__(self):
        if self.imenovalec == 1:
            return 'Ulomek({})'.format(self.stevec)
        return 'Ulomek({}, {})'.format(self.stevec, self.imenovalec)
    

    def __str__(self):
        if self.imenovalec == 1:
            return str(self.stevec) # Vračati mora string
        return '{}/{}'.format(self.stevec, self.imenovalec)

    def __add__(self, other):
        '''Vrne vsoto ulomkov.'''
        # Oba sta že okrajšana
        nov_st = self.stevec * other.imenovalec + other.stevec * self.imenovalec
        nov_im = self.imenovalec * other.imenovalec
        return Ulomek(nov_st, nov_im)

    def __sub__(self, other):
        '''Vrne razliko ulomkov.'''
        nov_st = self.stevec * other.imenovalec - other.stevec * self.imenovalec
        nov_im = self.imenovalec * other.imenovalec
        return Ulomek(nov_st, nov_im)


    def __mul__(self, other):
        return Ulomek(self.stevec * other.stevec, self.imenovalec * other.imenovalec)

    def __truediv__(self, other):
        if other.imenovalec == 0:
            raise Exception("Deljenje z 0 ni dovoljeno.")
        return self * Ulomek(other.imenovalec, other.stevec)
    
    def pristej(self, other):
        '''Prišteje ulomek trenutnemu.'''
        ulomeVsote = self + other
        self.stevec = ulomeVsote.stevec
        self.imenovalec = ulomeVsote.imenovalec

    def odstej(self, other):
        '''Odšteje od trenutnega ulomka.'''
        ulomekRazlike = self - other
        self.stevec = ulomekRazlike.stevec
        self.imenovalec = ulomekRazlike.imenovalec

    def pomnozi(self, other):
        '''Pomnoži trenutni ulomek.'''
        ulomekProdukta = self * other
        self.stevec = ulomekProdukta.stevec
        self.imenovalec = ulomekProdukta.imenovalec

    def deli(self, other):
        '''Deli z ulomkom.'''
        try:
            ulomekKvocienta = self / other
            self.stevec = ulomekKvocienta.stevec
            self.imenovalec = ulomekKvocienta.imenovalec
        except:
            raise Exception('Čuj ti, nea gre to tak na izi. Deljenje z 0 ni mogoče.')
    


        
u1 = Ulomek(12, 4)
u2 = Ulomek(7, 4)
u3 = Ulomek(13, 25)

print(u1)
print(u1 + u2)
print(u1 - u3)

u1.pristej(u2)
print(u1, u2)

u3.odstej(u2)
print(u3, u2)

u3.deli(u1)
print(u3)

# Če poženemo spodnjo vrstico, bo sprožilo izjemo, kot smo hoteli v varovalnem bloku
# u3.deli(Ulomek(0))



# Okrajšaj ulomke iz datoteke

def okrajsajUlomke(vhod, izhod):
    '''Prebere ulomke in jih okrajšane zapiše v novo datoteko.'''
    with open(izhod, 'w') as f:
        for vr in open(vhod, 'r', encoding='utf-8'):
            (st, im) = map(int, vr.strip().split('/'))
            print(Ulomek(st, im), file=f)

okrajsajUlomke(r'ulomki.txt', r'okrajsaniUlomki.txt')

# Sešteje ulomke iz datoteke

def sestejUlomke(vhod):
    '''Sešteje ulomke iz datoteke.'''
    vsotaUlomkov = Ulomek(0)
    for vr in open(vhod, 'r', encoding='utf-8'):
        (st, im) = map(int, vr.strip().split('/'))
        # print(Ulomek(st, im))
        # print(vsotaUlomkov)
        vsotaUlomkov.pristej(Ulomek(st, im))
    return vsotaUlomkov

print('Vsota ulomkov je:', sestejUlomke('ulomki.txt'))

# Izračunaj izraze

def izracunajIzraze(vhod, izhod):
    '''Izračuna izraze iz datoteke in jih izpiše v drugo datoteko.'''
    with open(izhod, 'w', encoding='utf-8') as f:
        for vr in open(vhod, 'r', encoding='utf-8'):
            izrazi = vr.strip().split()
            rezultat = Ulomek
            for i in range(len(izrazi)):
                if i == 0: # Prvega vzamemo za osnovo
                    rezultat = Ulomek(*map(int, izrazi[i].split('/')))
                elif i % 2 != 0: # Lihi elementi podajo operacijo
                    operacija = izrazi[i]
                else: # Na sodih mestih se pojavljajo ulomki
                    trenutniUlomek = (Ulomek(*map(int, izrazi[i].split('/'))))
                    # Sedaj upoštevamo operacijo
                    if operacija == '+':
                        rezultat.pristej(trenutniUlomek)
                    elif operacija == '-':
                        rezultat.odstej(trenutniUlomek)
                    elif operacija == '*':
                        rezultat.pomnozi(trenutniUlomek)
                    elif operacija == '/':
                        rezultat.deli(trenutniUlomek)
                    else:
                        print(operacija, 'ni veljavna operacija.')
                print(rezultat)
            print(vr.strip(), '=', str(rezultat), file=f)

izracunajIzraze(r'izrazi.txt', r'izrazi_rezultati.txt')


