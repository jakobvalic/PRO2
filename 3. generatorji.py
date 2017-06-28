# generatorji

def stevke(n):
    '''Generira števke števila n, začenši z enicami.'''
    while n != 0:
        yield n % 10
        n //= 10

# print(list(stevke(1224)))

def seznam(s):
    '''Generira elemente seznama s, izmenično od začetka do konca.'''
    if s == []:
        return 
    if len(s) == 1:
        yield s[0]
    else:
        yield s[0]
        yield s[-1]
        yield from seznam(s[1:-1])

# print(list(seznam([1, 2, 3, 4, 5, 6, 7, 8])))
# print(list(seznam(['ena', 'dva', 'tri', 'štiri', 'pet', 'šest', 'sedem'])))


def delitelji(n):
    '''Generira delitelje naravnega števila n.'''
##    for i in range(1, int(n ** 0.5) + 1):
##        if n % i == 0:
##            deltelj
    # raje brez korenov
    i = 1
    while i * i < n:
        if n % i == 0:
            yield i
            yield n // i
        i += 1
    if i * i == n: # popolni kvadrat
        yield i

# print(list(delitelji(162)))

def leonardo(n = None):
    '''Generira n Leonardovih števil.'''
    if n == 0:
        return
    if n == 1:
        yield 1
    L1 = 1
    L2 = 1
    yield L1
    yield L2
    if n is None:
        while True:
            L3 = L1 + L2 + 1
            yield L3
            L1, L2 = L2, L3
    i = 2
    while i < n:
        L3 = L1 + L2 + 1
        yield L3
        L1, L2 = L2, L3
        i += 1
        
print(list(leonardo(10)))        
g = leonardo()
print([next(g) for _ in range(15)])

    

class Izstevanka():
    def __init__(self, seznam, korak):
        self.seznam = seznam
        self.korak = korak - 1 # ker začenjamo pri 0
        self.i = 0 # kje smo
        

    def __iter__(self):
        return self
        

    def __next__(self):
        '''Vrne naslednji element. Hkrati odstrani iz seznama.'''
        if self.seznam == []:
            raise StopIteration("Vsi so bili izšteti ven.")
        # print(self.i, self.korak, self.seznam, (self.i + self.korak) % len(self.seznam))
        self.i = (self.i + self.korak) % len(self.seznam) 
        return self.seznam.pop(self.i)

        
##iz = Izstevanka(['Mojca', 'Matej', 'Cilka', 'Janez', 'Franc', 'Toni', 'Luka', 'Miha', 'Samo'], 3)
##for i in range(10):
##    print(next(iz))
    
print(list(Izstevanka(['Mojca', 'Matej', 'Cilka', 'Janez', 'Franc'], 3)))
print(list(Izstevanka([1, 2, 3, 4, 5, 6, 7], 3)))


# datumi: napiši metodo nasledji datum






import time












































