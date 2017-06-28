# Ulomek

def gcd(st, im):
    '''Vrne največji skupni deljitelj dveh celih števil.'''
    najD = 1
    st, im = min(st, im), max(st, im) # Uredimo števili po velikosti
    for delitelj in range(min(int(st ** 0.5), int(im ** 0.5)), 0, -1):
        if st % delitelj == 0: # Dobili smo delitelja števca, taki zmeraj nastopajo v parih
            if im % delitelj == 0:
                if delitelj > najD:
                    najD = delitelj
            par = st // delitelj # Par je zmeraj večji (ali enak) kot delitelj
            if im % par == 0:
                najD = par
    return najD

def gcdV2(st, im):
    '''Iščemo največji skupni delitelj.'''
    najD = 1
    delitelj = 1
    while delitelj * delitelj <= min(st, im):
        if st % delitelj == 0:
            if im % delitelj == 0:
                # Delitelji vedno nastopajo v parih. Par je zmeraj večji.
                par = im // delitelj
                if st % par == 0 and najD < par:
                    najD = par
                    break
        delitelj += 1
    return najD

for st, im in zip([12, 13, 14], [24, 39, 64]):
    print(gcd(st, im), gcdV2(st, im))


def okrajsaj(st, im):
    '''Okrajša ulomek.'''
    najD = gcd(st, im)
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

    
        
u1 = Ulomek(12, 4)
u2 = Ulomek(7, 4)
u3 = Ulomek(13, 25)

print(u1)
print(u1 + u2)
print(u1 - u3)