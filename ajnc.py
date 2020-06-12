import random
from turtle import *
from math import *

tracer(False)
bgcolor('#008000')
#crtanje

    #pozicije
def poz_i1():
    pu()
    goto(-230,-150)
    pd()
def poz_i2():
    pu()
    goto(-115,-150)
    pd()
def poz_i3():
    pu()
    goto(0,-150)
    pd()
def poz_i4():
    pu()
    goto(115,-150)
    pd()
def poz_i5():
    pu()
    goto(230,-150)
    pd()
def poz_d1():
    pu()
    goto(-230,100)
    pd()
def poz_d2():
    pu()
    goto(-115,100)
    pd()
def poz_d3():
    pu()
    goto(0,100)
    pd()
def poz_d4():
    pu()
    goto(115,100)
    pd()
def poz_d5():
    pu()
    goto(230,100)
    pd()

    #karte
def oblik_karte():
    pd()
    pensize(3)
    pencolor('black')
    fillcolor('white')
    begin_fill()
    for i in range (2):
        fd(75)
        circle(15,90)
        fd(150)
        circle(15,90)
    end_fill()

def znak(s,boja):
    color(boja)
    begin_fill()
    write(s, move=False, align ='left', font = ('Arial',25,'normal'))
    end_fill()

#Funkcija za kartu tref
def karta_tref(oznaka):
    def tref (size):
        def pravokutnik (size):
            color('black')
            begin_fill()
            for i in range (2):
                fd(size)
                lt(90)
                fd(size/10)
                lt(90)
            end_fill()
        def krug (size):
            color('black')
            begin_fill()
            circle (size)
            end_fill()
        pravokutnik (size)
        pu()
        fd(size/2+size/20)
        lt(90)
        fd(size/10)
        pd()
        pravokutnik (size)
        pu()
        fd(size)
        lt(90)
        fd(size/20)
        rt(180)
        pd()
        krug(size/3)
        pu()
        fd(size/20)
        rt(90)
        fd(size/3)
        pd()
        krug(size/3)
        pu()
        rt(90)
        fd(size/10)
        rt(90)
        pd()
        krug(size/3)
        pu()
    oblik_karte()
    pu()
    fd(12.5)
    lt(90)
    fd(15)
    rt(90)
    pd()
    tref(50)
    fd(85)
    rt(90)
    bk(42)
    znak(oznaka,'black')
    fd(70)
    lt(90)
    fd(5)
    rt(90)
    pensize(0.5)
    tref(15)
    rt(90)
    pu()
#Funkcija za kartu pik
def karta_pik(oznaka):
    def pik (size):
        def krug(size):
            color('black')
            begin_fill()
            circle (size)
            end_fill()
        color('black')
        begin_fill()
        fd(size)
        lt(110)
        fd(size)
        lt(70)
        fd(-(size-(2*(size*cos(70)))-(size/20)))
        lt(70)
        fd(size)
        end_fill()
        lt(110)
        pu()
        fd(size/2)
        lt(90)
        fd(size+(size/5))
        pd()
        krug (size/2)
        rt(180)
        krug (size/2)
        pu()
        rt(90)
        fd((size/2)+(size/5))
        rt(90)
        fd((size/2)-(size/20))
        rt(30)
        pd()
        color('black')
        begin_fill()
        fd(size+((size/5)*2))
        rt(120)
        fd(size+((size/5)*2))
        rt(60)
        fd(size)
        rt(90)
        fd(size+(size/5))
        end_fill()
        pu()
    oblik_karte()
    pu()
    fd(22.5)
    lt(90)
    fd(15)
    rt(90)
    pd()
    pik(30)
    rt(60)
    fd(80)
    rt(90)
    bk(20)
    znak(oznaka,'black')
    fd(75)
    lt(90)
    fd(4)
    rt(90)
    pik(10)
    pd()
    rt(150)
    
#Funkcija za kartu herc
def karta_herc(oznaka):
    def herc(size):
        def srce(size):
            for i in range (200):
                rt(1)
                fd(1*size)
        color('red')
        begin_fill()
        lt(140)
        fd(111.65*size)
        srce(size)
        lt(120)
        srce(size)
        fd(111.65*size)
        end_fill()
    oblik_karte()
    pu()
    fd(38)
    lt(90)
    fd(15)
    rt(90)
    herc(0.4)
    rt(130)
    fd(125)
    rt(90)
    bk(45)
    znak(oznaka,'red')
    fd(75)
    lt(90)
    fd(5)
    rt(90)
    herc(0.15)
    lt(140)

#Funkcija za kartu karo
def karta_karo(oznaka):
    def karo(size):
        color('red')
        begin_fill()
        for i in range (2):
            lt(60)
            fd(size)
        lt(120)
        fd(size)
        lt(60)
        fd(size)
        end_fill()
    oblik_karte()
    pu()
    fd(35)
    lt(90)
    fd(15)
    rt(90)
    karo(55)
    lt(150)
    fd(125)
    rt(90)
    bk(42)
    znak(oznaka,'red')
    fd(82)
    lt(90)
    fd(5)
    rt(90)
    karo(17)
    lt(60)

#Okrenuta karta
def okrenuta():
    poz_d1()
    pd()
    pensize(3)
    pencolor('black')
    fillcolor('blue')
    begin_fill()
    for i in range (2):
        fd(75)
        circle(15,90)
        fd(150)
        circle(15,90)
    end_fill()

#karte
def crtaj(di,poz,s,znak):
    if di.lower()=='i':
        if poz==1:
            poz_i1()
        elif poz==2:
            poz_i2()
        elif poz==3:
            poz_i3()
        elif poz==4:
            poz_i4()
        else:
            poz_i5()
    else:
        if poz==1:
            poz_d1()
        elif poz==2:
            poz_d2()
        elif poz==3:
            poz_d3()
        elif poz==4:
            poz_d4()
        else:
            poz_d5()
    a=''
    if znak=='Dva':
        a='2'
    elif znak=='Tri':
        a='3'
    elif znak=='Četiri':
        a='4'
    elif znak=='Pet':
        a='5'
    elif znak=='Šest':
        a='6'
    elif znak=='Sedam':
        a='7'
    elif znak=='Osam':
        a='8'
    elif znak=='Devet':
        a='9'
    elif znak=='Deset':
        a='10'
    elif znak=='Dečko':
        a='D'
    elif znak=='Baba':
        a='B'
    elif znak=='Kralj':
        a='K'
    else:
        a='A'

    if s=='Herc':
        karta_herc(a)
    elif s=='Karo':
        karta_karo(a)
    elif s=='Pik':
        karta_pik(a)
    else:
        karta_tref(a)
            
    

#igra
boje = ('Herc', 'Karo', 'Pik', 'Tref')
brojevi = ('Dva', 'Tri', 'Četiri', 'Pet', 'Šest', 'Sedam', 'Osam', 'Devet', 'Deset', 'Dečko', 'Baba', 'Kralj', 'As')
vrijednosti = {'Dva':2, 'Tri':3, 'Četiri':4, 'Pet':5, 'Šest':6, 'Sedam':7, 'Osam':8, 'Devet':9, 'Deset':10, 'Dečko':10, 'Baba':10, 'Kralj':10, 'As':11}

igra=True

class Karta:
    def __init__(self,boja,broj):
        self.boja = boja
        self.broj = broj

    def __str__ (self):
        return self.broj + ' ' + self.boja

class Dek:
    def __init__(self):
        self.dek = []
        for boja in boje:
            for broj in brojevi:
                self.dek.append(Karta(boja,broj))
    def __str__(self):
        deck_comp = ''
        for karta in self.dek:
            deck_comp += '\n' + karta.__str__()
        return 'Dek ima:' + deck_comp
    
    def miješanje(self):
        random.shuffle(self.dek)

    def dijeli(self):
        jedna_karta = self.dek.pop()
        return jedna_karta

class Ruka:
    def __init__(self):
        self.karte = []
        self.vrijednost = 0
        self.asevi = 0

    def vuci_kartu(self,karta):
        self.karte.append(karta)
        self.vrijednost += vrijednosti[karta.broj]
        if karta.broj == 'As':
            self.asevi += 1

    def vrijednost_asa(self):
        while self.vrijednost > 21 and self.asevi:
            self.vrijednost -=10
            self.asevi -=1

class Novac:
    def __init__(self):
        self.ukupno = 100 #odredi koliko novca osoba ima na početku
        self.ulog = 0

    def dobitak(self):
        self.ukupno += self.ulog

    def gubitak(self):
        self.ukupno -= self.ulog

def uloži(novac):
    while True:
        try:
            novac.ulog=int(input('Koliko želite uložiti? '))
        except ValueError:
            print('Unjeli ste krivi iznos!')
        else:
            if novac.ulog>novac.ukupno:
                print('Unjeli ste prevelik iznos, vaš iznos je: ',novac.ukupno)
            else:
                break

def uzmi_kartu(dek,ruka):
    ruka.vuci_kartu(dek.dijeli())
    ruka.vrijednost_asa()

def uzmi_ili_ne(dek,ruka):
    global igra

    while True:
        x = input("\nHoćeš li vući kartu ili ne? Upiši 'Da' ili 'Ne'")

        if x.lower() == 'da':
            uzmi_kartu(dek,ruka)

        elif x.lower() == 'ne':
            print('\nIgrač ne uzima kartu, dijelitelj igra...')
            igra = False
        else:
            print('Krivi unos, pokušaj ponovo')
            continue
        break

def pokaži1(igrač, dijelitelj):
            print("\nDijeliteljeva ruka: ")
            print("Karta je skrivena")
            print(dijelitelj.karte[1])
            print("\nIgračeva ruka: ", *igrač.karte, sep='\n ')
            print("Igračeva ruka=",igrač.vrijednost)
            igračlista=igrač.karte
            dlista=dijelitelj.karte
            strlista=[]
            dstrlista=[]
            for i in range(len(igračlista)):
                a=str(igračlista[i])
                s=a.split()
                strlista.append(s)
            for i in range(len(strlista)):
                poz=i+1
                a=strlista[i][0]
                b=strlista[i][1]
                crtaj('i',poz,b,a)
            for i in range(len(dlista)):
                q=str(dlista[i])
                w=q.split()
                dstrlista.append(w)
            poz=0
            m=dstrlista[i][0]
            n=dstrlista[i][1]
            okrenuta()
            for i in range(1,len(dstrlista)):
                poz=i+1
                m=dstrlista[i][0]
                n=dstrlista[i][1]
                crtaj('d',poz,n,m)
                
def pokaži2(igrač, dijelitelj):
            print("\nDijeliteljeva ruka: ", *dijelitelj.karte, sep='\n')
            print("\nDijeliteljeva ruka: ", dijelitelj.vrijednost)
            print("\nIgračeva ruka: ",*igrač.karte,sep='\n')
            print("Igračeva ruka=",igrač.vrijednost)
            igračlista=igrač.karte
            dlista=dijelitelj.karte
            strlista=[]
            dstrlista=[]
            for i in range(len(igračlista)):
                a=str(igračlista[i])
                s=a.split()
                strlista.append(s)
            for i in range(len(strlista)):
                poz=i+1
                a=strlista[i][0]
                b=strlista[i][1]
                crtaj('i',poz,b,a)
            for i in range(len(dlista)):
                q=str(dlista[i])
                w=q.split()
                dstrlista.append(w)
            for i in range(len(dstrlista)):
                poz=i+1
                m=dstrlista[i][0]
                n=dstrlista[i][1]
                crtaj('d',poz,n,m)

def igrač_preko(igrač,dijelitelj,novac):
    print('Igrač je prešao 21!')
    novac.gubitak()

def igrač_pobjeda(igrač,dijelitelj,novac):
    print('Igrač pobjeđuje!')
    novac.dobitak()

def dijelitelj_preko(igrač,dijelitelj,novac):
    print('Dijelitelj je prešao 21!')
    novac.dobitak()

def dijelitelj_pobjeda(igrač,dijelitelj,novac):
    print('Dijelitelj pobjeđuje!')
    novac.gubitak()

def izjednačeno(igrač,dijelitelj):
    print('Izjednačeno je!')

novac=Novac()
while True:

    print('Dođite što bliže 21 ali ne preko kako bi pobjedili!!')

    dek=Dek()
    dek.miješanje()

    i_ruka=Ruka()
    i_ruka.vuci_kartu(dek.dijeli())
    i_ruka.vuci_kartu(dek.dijeli())

    d_ruka=Ruka()
    d_ruka.vuci_kartu(dek.dijeli())
    d_ruka.vuci_kartu(dek.dijeli())



    uloži(novac)

    pokaži1(i_ruka,d_ruka)

    while igra:
        uzmi_ili_ne(dek,i_ruka)

        pokaži1(i_ruka,d_ruka)

        if i_ruka.vrijednost>21:
            igrač_preko(i_ruka,d_ruka,novac)
            break

    if i_ruka.vrijednost<=21:
        while d_ruka.vrijednost<17:
            uzmi_kartu(dek,d_ruka)

        pokaži2(i_ruka,d_ruka)

        if d_ruka.vrijednost>21:
                dijelitelj_preko(i_ruka,d_ruka,novac)
        elif d_ruka.vrijednost>i_ruka.vrijednost:
                dijelitelj_pobjeda(i_ruka,d_ruka,novac)
        elif d_ruka.vrijednost<i_ruka.vrijednost:
                igrač_pobjeda(i_ruka,d_ruka,novac)
        else:
            izjednačeno(i_ruka,d_ruka)

    print('Vaš trenutni iznos: ',novac.ukupno)

    nova_igra=input('Želite li igrati opet? Unesite Da ili Ne')

    if nova_igra.lower()=='da':
        clear()
        igra=True
        continue
    else:
        print('Doviđenja!')
        break
        
