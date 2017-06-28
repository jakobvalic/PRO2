# razred Ulomek

def gcd(st, im):
    '''Vrne največji skupni deljitelj dveh celih števil.'''
    najD = 1
    st, im = min(st, im), max(st, im)
    for delitelj in range(min(int(st ** 0.5), int(im ** 0.5)), 0, -1):
        if st % delitelj == 0: # dobili smo delitelja števca, taki zmeraj nastopajo v parih
            if im % delitelj == 0:
                if delitelj > najD:
                    najD = delitelj
            par = st // delitelj # par je zmeraj večji (ali enak) kot delitelj
            if im % par == 0:
                najD = par
    return najD

def okrajsaj(st, im):
    '''Okrajša ulomek.'''
    najD = gcd(st, im)
    assert gcd(st//najD, im//najD) == 1
    return st // najD, im // najD


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
        return '{}/{}'.format(self.stevec, self.imenovalec)


    def __mul__(self, other):
        return Ulomek(self.stevec * other.stevec, self.imenovalec * other.imenovalec)


    def __add__(self, other):
        '''Vrne nov ulomek.'''
        #oba sta že okrajšana
        nov_st = self.stevec * other.imenovalec + other.stevec * self.imenovalec
        nov_im = self.imenovalec * other.imenovalec
        return Ulomek(nov_st, nov_im)

    def __truediv__(self, other):
        if other.imenovalec == 0:
            raise Exception("Deljenje z 0 ni dovoljeno.")
        return self * Ulomek(other.imenovalec, other.stevec)

    
        
u1 = Ulomek(12, 4)
u2 = Ulomek(7, 4)
u3 = Ulomek(13, 25)

