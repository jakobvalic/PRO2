# razred Ulomek

def gcd(st, im):
    '''Vrne največji skupni deljitelj dveh celih števil.'''
    najD = 1
    st, im = min(st, im), max(st, im)
    for delitelj in range(min(int(st ** 0.5), int(im ** 0.5)), 0, -1):
        if st % delitelj == 0: # dobili smo delitelja števca, taki zmeraj nastopajo v parih
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
    def __init__(self, stevec, imenovalec):
        try:
            stevec / imenovalec
        except:
            raise ValueError('Deljenje z 0 ni mogoče.')
        okrajsani_stevec, okrajsani_imenovalec = okrajsaj(stevec, imenovalec)
        self.stevec = okrajsani_stevec
        self.imenovalec = okrajsani_imenovalec
        

