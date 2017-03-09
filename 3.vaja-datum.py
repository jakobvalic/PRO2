# razred Datum

from datetime import *
now = datetime.now()


def je_prestopno(leto):
    '''Vrne, ali je leto prestopno.'''
    if (leto % 100 == 0 and leto % 400 != 0):
        return False
    if leto % 4 == 0:
        return True
    return False

def stevilo_dni(mesec, leto):
    '''Vrne število dni danega meseca.'''
    feb = 29 if je_prestopno(leto) else 28
    dnevi = [31, feb, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return dnevi[mesec - 1]

def je_veljaven_datum(dan, mesec, leto):
    '''Pove, ali je datum veljaven.'''
    if not (1 <= mesec <= 12):
        return False
    if not (1 <= dan <= stevilo_dni(mesec, leto)):
        return False
    return True

class Datum:
    def __init__(self, dan = None, mesec = None, leto = None):
        now = datetime.now()
        
        self.dan = dan if dan else now.day
        self.mesec = mesec if mesec else now.month
        self.leto  = leto if leto else now.year
        #preverjamo veljavnost
        if not je_veljaven_datum(self.dan, self.mesec, self.leto):
            raise Exception('Datum ni veljaven.')

    def __repr__(self):
        return 'Datum({},{},{})'.format(self.dan, self.mesec, self.leto)

    def __str__(self):
        return '{}.{}.{}'.format(self.dan, self.mesec, self.leto)

    def __eq__(self, other):
        if other is None:
            return False
        return (self.leto, self.mesec, self.dan) == (other.leto, other.mesec, other.dan)

    def __lt__(self, other):
        return (self.leto, self.mesec, self.dan) < (other.leto, other.mesec, other.dan)

    def danVLetu(self):
        '''Vrne zaporedni dan leta. Pomagamo si s številom dni.'''
        if self.mesec == 1:
            return self.dan
        zap_dan = 0
        for mesec in range(self.mesec): # do trenutnega meseca
            zap_dan += stevilo_dni(mesec, self.leto)
        zap_dan += self.dan # še trenutni mesec
        return zap_dan

def datumIzNiza(niz):
    '''Sprejme datum iz niza in ga pretvori v objekt.'''
    [dan, mesec, leto] = list(map(int, niz.split('.')))
    return Datum(dan, mesec, leto)

def datumIzEMSO(emso):
    '''Vrne datum iz EMSO.'''
    dan = int(emso[:2])
    mesec = int(emso[2:4])
    letnica = emso[4:7]
    tisocletje = '1' if letnica[0] == '9' else '2'
    leto = int(tisocletje + letnica)
    return Datum(dan, mesec, leto)

def razlika_datumov(dat1, dat2):
    '''Vrne število dni med dvema datumoma.'''
    dat1, dat2 = min(dat1, dat2), max(dat1, dat2)
    # če sta istega leta
    if dat1.leto == dat2.leto:
        return dat2.danVLetu() - dat1.danVLetu()
    # če nista istega leta
    # najprej izračunamo, koliko dni je še do konca leta prvega datuma
    do_konca = 366 if je_prestopno(dat1.leto) else 365
    do_konca -= dat1.danVLetu()
    # vmesna leta
    vmes = 0
    for leto in range(dat1.leto + 1, dat2.leto):
        vmes += 366 if je_prestopno(dat1.leto) else 365
    # do datuma 2
    do_dat2 = dat2.danVLetu()
    return do_konca + vmes + do_dat2

def najmanjsi_datum(imeDatoteke):
    '''Prebere datume iz datoteke in izpiše najmanjšega.'''
    najm = None # da ne bi slučajno izbrali manjšega od najmanjšega
    for vr in open(imeDatoteke, 'r', encoding = 'utf-8'):
        trenutniDat = datumIzNiza(vr.strip())
        #  to je zelo pomembno is None -> damo prvega iz datoteke
        if najm is None or trenutniDat < najm:
            najm = trenutniDat
    return najm

def datumi(dat1, dat2):
    '''Generira vse datume med danima datumoma.'''
    dat1, dat2 = min(dat1, dat2), max(dat1, dat2)
    (dan, mesec, leto) = (dat1.dan, dat1.mesec, dat1.leto)
    while Datum(dan, mesec, leto) != dat2:
        yield Datum(dan, mesec, leto)
        # dodamo en dan datumu 1
        if dan < stevilo_dni(mesec, leto):
            dan += 1
        else: # skočimo za en mesec naprej 
            if mesec == 12: # skočimo za eno leto naprej
                (dan, mesec, leto) = (1, 1, leto + 1)
            else:
                (dan, mesec) = (1, mesec + 1)
    yield dat2 # še zadnjega

            

d1 = Datum() # današnji datum
d2 = Datum(1, 2, 1990)
d3 = Datum(24, 4, 2002)
d4 = Datum(24, 10, 2070)

d5 = datumIzNiza('1.1.1998')
d5.danVLetu

d6 = datumIzEMSO('0102990500131')
starSem = razlika_datumov(d2, d1)
studiram = razlika_datumov(Datum(1,10,2009), d1)

print('Najmanjši datum je:', najmanjsi_datum('datumi.txt'), '\n')
print([x for x in datumi(Datum(8, 12, 2016), d1)])
