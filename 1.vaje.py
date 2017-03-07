#multifakulteta

def multifakulteta(n, k):
    '''Izračuna multifakultetao.'''

#kolokviji

def nabor(niz):
    '''Spremeni iz niza v nabor.'''
    sez = list(niz.split(','))
    sez_pravi = [sez[0]] + [int(x) for x in sez[1:]]
    return tuple(sez_pravi)

print(nabor('Janez Novak,1,3,3,0,2'))

def nalozi(ime):
    '''Shrani v seznam imena in rezultate iz datoteke.'''
    sez_imen = list()
    with open(ime) as f:
        for vr in f:
            sez_imen.append(nabor(vr))
    return sez_imen

print(nalozi('kolokviji.txt'))

def vsote(vhodna, izhodna):
    '''Prebere, sešteje in zapiše v novo datoteko.'''
    with open(izhodna, 'w', encoding = 'utf-8') as f:
        podatki = nalozi(vhodna)
        for podatek in podatki:
            ime = podatek[0]
            ocene = podatek[1:]
            print(ime, ', ', sum(ocene), file = f, sep = '')

vsote('kolokviji.txt', 'sestevki.txt')

#posredno prevajanje

def prevedi(slo_ang, ang_nem):
    '''Prevede iz slovenščine v angleščino, nato v nemščino.'''
    prevod = dict()
    for geslo, prevod_ang in slo_ang.items():
        prevod_nem = ang_nem.get(prevod_ang, '')
        if prevod_nem:
            prevod[geslo] = prevod_nem
    return prevod

print(prevedi({'miza': 'table', 'jaz': 'I'}, {'table': 'Tisch', 'love': 'Liebe'}))


#kuhamo in pečemo

def pomnozi(recept, faktor):
    '''Sestavi in vrne nov recept.'''
    for kljuc, vrednost in recept.items():
        recept[kljuc] = vrednost * faktor
    return recept

print(pomnozi({'jajca': 4, 'moka': 500}, 2))

def imamoSestavine(recept, shramba):
    '''Preveri, ali imamo v shrambi dobolj sestavin.'''
    for kljuc, vrednost_recept in recept.items():
        if shramba.get(kljuc, 0) < vrednost_recept:
            return False
    return True

print(imamoSestavine({'jajca': 4, 'moka': 500}, {'jajca': 4, 'moka': 700}))
print(imamoSestavine({'jajca': 4, 'moka': 500, 'pecilni prašek': 1}, {'jajca': 4, 'moka': 700}))

def potrebnoKupiti(recept, shramba):
    '''Vrne slovar sestavin, ki jih je potrebno dokupiti.'''
    nakup = dict()
    for sestavina, kolicina in recept.items():
        razlika = kolicina - shramba.get(sestavina, 0)
        if razlika > 0:
            nakup[sestavina] = razlika
    return nakup

print(potrebnoKupiti({'jajca': 4, 'moka': 500}, {'jajca': 4, 'moka': 700}))
print(potrebnoKupiti({'jajca': 4, 'moka': 500, 'pecilni prašek': 1}, {'jajca': 4, 'moka': 700}))
