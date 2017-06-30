# Multifakulteta

def multifakulteta(n, k):
    '''Izračuna multifakulteto.'''
    rez = 1
    while n > 0:
        rez *= n
        n -= k
    return rez

print(multifakulteta(6,1 )) # Navadna fakulteta 6!
print(multifakulteta(8,2)) # 8 * 6 * 4 * 2
print(multifakulteta(13,3), '\n')


# Štetje



# Kolokviji

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
    with open(izhodna, 'w', encoding='utf-8') as f:
        podatki = nalozi(vhodna)
        for podatek in podatki:
            ime = podatek[0]
            ocene = podatek[1:]
            print(ime, ', ', sum(ocene), file=f, sep='')

vsote('kolokviji.txt', 'sestevki_kolokvijev.txt')
print()


# Štetje

def stetje(niz):
    '''Z iteracijo po nizu.'''
    nov_niz = ''
    stevec = 1
    for znak in niz:
        if znak == '#':
            nov_niz += str(stevec)
            stevec += 1
        else:
            nov_niz += znak
    return nov_niz

def stetjeV2(niz):
    '''Znak # nadomesti z zaporedno številko od 1 naprej.'''
    stLojtr = niz.count('#')
    nizOklepaji = '{}'.join(niz.split('#')) # Ustvarimo pogoje za format
    return nizOklepaji.format(*[i for i in range(1, stLojtr + 1)]) # Ukaz *[seznam] razpakira vrednosti v seznamu, npr
                                                                   # *[1, 2, 3] -> 1, 2, 3

print(stetje('a# b# ### -#-#- (#,#) xy # #'))
print(stetjeV2('a# b# ### -#-#- (#,#) xy # #'), '\n')


# Posredno prevajanje

def prevedi(slo_ang, ang_nem):
    '''Prevede iz slovenščine v angleščino, nato v nemščino.'''
    prevod = dict()
    for geslo, prevod_ang in slo_ang.items():
        prevod_nem = ang_nem.get(prevod_ang, None) # Če gesla ni, vrne None
        if prevod_nem:
            prevod[geslo] = prevod_nem
    return prevod

print(prevedi({'miza': 'table', 'jaz': 'I'}, {'table': 'Tisch', 'love': 'Liebe'}), '\n')


# Kuhamo in pečemo

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
