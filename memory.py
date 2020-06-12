from turtle import*
import turtle
from random import *
speed(0)
ht()

def crtac(a,b,j,i):
    if b==0:
        pu()
        goto(-235,-235+a*i)
        fd (a*j)
        pd()
        karta(a)
    elif b==1:
        pu()
        goto(-235,-235+a*i)
        fd (a*j)
        pd()
        karta1(a)
    elif b==2:
        pu()
        goto(-235,-235+a*i)
        fd (a*j)
        pd()
        karta2(a)
    elif b==3:
        pu()
        goto(-235,-235+a*i)
        fd (a*j)
        pd()
        karta3(a)
    elif b==4:
        pu()
        goto(-235,-235+a*i)
        fd (a*j)
        pd()
        karta4(a)
    elif b==5:
        pu()
        goto(-235,-235+a*i)
        fd (a*j)
        pd()
        karta5(a)
    elif b==6:
        pu()
        goto(-235,-235+a*i)
        fd (a*j)
        pd()
        karta6(a)
    elif b==7:
        pu()
        goto(-235,-235+a*i)
        fd (a*j)
        pd()
        karta7(a)
    elif b==8:
        pu()
        goto(-235,-235+a*i)
        fd (a*j)
        pd()
        karta8(a)
    elif b==9:
        pu()
        goto(-235,-235+a*i)
        fd (a*j)
        pd()
        karta9(a)
    elif b==10:
        pu()
        goto(-235,-235+a*i)
        fd (a*j)
        pd()
        karta10(a)
    elif b==11:
        pu()
        goto(-235,-235+a*i)
        fd (a*j)
        pd()
        karta11(a)
    elif b==12:
        pu()
        goto(-235,-235+a*i)
        fd (a*j)
        pd()
        karta12(a)
    elif b==13:
        pu()
        goto(-235,-235+a*i)
        fd (a*j)
        pd()
        karta13(a)
    elif b==14:
        pu()
        goto(-235,-235+a*i)
        fd (a*j)
        pd()
        karta14(a)
    elif b==15:
        pu()
        goto(-235,-235+a*i)
        fd (a*j)
        pd()
        karta15(a)
    elif b==16:
        pu()
        goto(-235,-235+a*i)
        fd (a*j)
        pd()
        karta16(a)
    elif b==17:
        pu()
        goto(-235,-235+a*i)
        fd (a*j)
        pd()
        karta17(a)
    elif b==18:
        pu()
        goto(-235,-235+a*i)
        fd (a*j)
        pd()
        bijelo(a)
    elif b==19:
        pu()
        goto(-235,-235+a*i)
        fd (a*j)
        pd()
        okrenuta(a)

def brojac(a,x):
    s=0
    for i in a:
        for j in i:
            if j==x:
                s+=1
    return s

def bijelo(a):
    pencolor("white")
    colormode(255)
    fillcolor('white')
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()

def karta(a):
    pencolor("black")
    colormode(255)
    fillcolor('purple')
    begin_fill()
    fd(a)
    lt(90)
    fd(a)
    lt(90)
    fd(a)
    lt(90)
    fd(a)
    lt(90)
    end_fill()

def karta1(a):
    pencolor("black")
    colormode(255)
    fillcolor('tomato')
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    pu()
    lt(45)
    fd(a/2)
    pd()
    color('bisque')
    shape("turtle")
    turtlesize(a/100)
    stamp()
    pu()
    fd(a/4)
    lt(40)
    fd(a/8)
    stamp()
    pu()
    bk(a/8)
    rt(100)
    fd(a/5)
    stamp()
    pu()
    lt(170)
    fd(a/2)
    pd()
    stamp()
    pu()
    rt(20)
    bk(a/1.6)
    pd()
    stamp()

def karta2(a):
    pencolor("black")
    colormode(255)
    fillcolor('gold')
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    pu()
    fd(a/4)
    lt(90)
    fd(a/4)
    rt(90)
    pd()
    pensize(a/4)
    pencolor('cyan')
    for i in range(4):
        fd(a/2)
        lt(90)
    pensize(a/8)
    pencolor('deep pink')
    for i in range(4):
        fd(a/2)
        lt(90)
    pensize(a/15)
    pencolor('honeydew')
    for i in range(4):
        fd(a/2)
        lt(90)
    pensize(a/30)
    pencolor('gold')
    for i in range(4):
        fd(a/2)
        lt(90)

def karta3(a):
    pencolor("black")
    colormode(255)
    fillcolor('medium spring green')
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    pu()
    lt(45)
    fd(a/1.8)
    pd()
    color('pink')
    shape("turtle")
    turtlesize(a/50)
    stamp()


def karta4(a):
    pencolor("black")
    colormode(255)
    fillcolor('magenta')
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    pu()
    fd(a/4)
    lt(90)
    fd(a/4)
    rt(90)
    pd()
    pensize(a/4)
    pencolor('medium purple')
    for i in range(4):
        fd(a/2)
        lt(90)
    pensize(a/10)
    pencolor('dark magenta')
    for i in range(4):
        fd(a/2)
        lt(90)
    
        

def karta5(a):
    pencolor("black")
    colormode(255)
    fillcolor(65,105,225)
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    fd(a/3)
    lt(90)
    pencolor(65,105,225)
    fd(a/3)
    rt(90)
    color("yellow","yellow")
    begin_fill()
    for i in range (5):
        fd(a/2)
        rt(144)
    end_fill()
    pencolor(65,105,225)
    bk(a/4)
    lt(90)
    fd(a/3)
    rt(90)
    color("yellow","yellow")
    begin_fill()
    for i in range (5):
        fd(a/3)
        rt(144)
    end_fill()
    
def karta6(a):
    pencolor("black")
    colormode(255)
    fillcolor(211,211,211)
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    pu()
    lt(90)
    fd(a)
    rt(90)
    pd()
    pensize(2)
    pencolor(75,0,130)
    side = a
    for i in range(100):
        fd(side)
        rt(90) 
        side = side - 2
        
def karta7(a):
    pencolor("black")
    colormode(255)
    fillcolor(0,128,128)
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    pu()
    lt(90)
    fd(a/2+a/8.5)
    pd()
    rt(90)
    pencolor(255,160,122)
    side = a
    for i in range(a//2):
        fd(side)
        rt(144) 
        side = side - 2

def karta8(a):
    pencolor("black")
    colormode(255)
    fillcolor(176,224,230)
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    fillcolor(144,238,144)
    begin_fill()
    fd(a)
    lt(90)
    fd(a/3)
    lt(90)
    fd(a)
    lt(90)
    fd(a/3)
    end_fill()
    lt(90)
    pu()
    fd(a/1.3)
    lt(90)
    fd(a/1.8)
    rt(70)
    pd()
    fillcolor('white')
    pencolor('white')
    begin_fill()
    circle(a/10,180)
    rt(100)
    circle(a/9,150)
    rt(100)
    circle(a/8,100)
    rt(90)
    circle(a/7,80)
    rt(30)
    circle(a/10,200)
    rt(70)
    circle(a/5,50)
    rt(70)
    circle(a/12,120)
    rt(160)
    circle(a/9,210)
    end_fill()
    setheading(0)

def karta9(a):
    pencolor("black")
    colormode(255)
    fillcolor(176,224,230)
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    fillcolor(144,238,144)
    begin_fill()
    fd(a)
    lt(90)
    fd(a/3)
    lt(90)
    fd(a)
    lt(90)
    fd(a/3)
    end_fill()
    pu()
    lt(90)
    fd(a/2)
    lt(90)
    fd(a/4)
    pd()
    rt(90)
    fillcolor('light yellow')
    begin_fill()
    for i in range(4):
        fd(a/4)
        lt(90)
    end_fill()
    fillcolor('firebrick')
    lt(90)
    fd(a/4)
    begin_fill()
    rt(30)
    fd(a/4)
    rt(120)
    fd(a/4)
    rt(30)
    end_fill()
    fd(a/4)
    rt(90)
    fillcolor('peru')
    begin_fill()
    fd(a/14)
    rt(90)
    fd(a/8)
    lt(90)
    fd(a/12)
    lt(90)
    fd(a/8)
    end_fill()
   

def karta10(a):
    pencolor("black")
    colormode(255)
    fillcolor('indian red')
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    fd(a/2)
    fillcolor('blanched almond')
    begin_fill()
    lt(45)
    for i in range(4):
        fd(a/2)
        lt(90)
    lt(45)
    pu()
    fd(a/4)
    pd()
    rt(45)
    for i in range(4):
        fd(a/2)
        lt(90)
    end_fill()

def karta11(a):
    pencolor("black")
    colormode(255)
    fillcolor('azure')
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    lt(90)
    fd(3*a/4)
    rt(90)
    pu()
    fd(8)
    pd()
    fillcolor('Teal')
    begin_fill()
    side = a-16
    for i in range(35):
       fd(side)
       rt(120)
       side = side - 3
    end_fill()
   
    
def karta12(a):
    color('dark salmon', 'moccasin')
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    lt(90)
    fd(a/2)
    bk(5)
    rt(90)
    for i in range(36):
        fd(a)
        lt(170)

def karta13(a):
    pencolor('black')
    colormode(255)
    fillcolor('alice blue')
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    pu()
    fd(a/2)
    pd()
    pencolor('crimson')
    for i in range(10):
        circle((a/20)*i)
    pu()
    lt(90)
    fd(a)
    lt(90)
    pd()
    pencolor('dark green')
    for i in range(10):
        circle((a/20)*i)
    fd(a/2)
    lt(90)
    fd(a/2)
    pencolor('midnight blue')
    for i in range(10):
        circle((a/20)*i)
    pu()
    lt(90)
    fd(a)
    lt(90)
    pd()
    pencolor('dark magenta')
    for i in range(10):
        circle((a/20)*i)

    
def karta14(a):
    pencolor("black")
    colormode(255)
    fillcolor('dark olive green')
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    pu()
    fd(a/2)
    lt(90)
    fd(a/2)
    pd()
    pencolor('spring green')
    for i in range(10):
        circle((a/40)*i)
    rt(90)
    pencolor('aqua')
    for i in range(10):
        circle((a/40)*i)
    rt(90)
    pencolor('deep pink')
    for i in range(10):
        circle((a/40)*i)
    rt(90)
    pencolor('yellow')
    for i in range(10):
        circle((a/40)*i)

def karta15(a):
    pencolor("black")
    colormode(255)
    fillcolor('dark salmon')
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    pu()
    lt(90)
    fd(3*a/4 + 5)
    rt(90)
    fd(a/4)
    pd()
    pencolor('light sky blue')
    side = a
    for i in range(104):
       fd(side//2)
       rt(72) 
       side = side - 2

def karta16(a):
    pencolor("black")
    colormode(255)
    fillcolor('maroon')
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    fd(a/1)
    lt(90)
    fd(a/2)
    fillcolor('dark red')
    begin_fill()
    circle(a/2)
    end_fill()
    pu()
    lt(90)
    fd(a/6)
    rt(90)
    pd()
    fillcolor('brown')
    begin_fill()
    circle(a/3)
    end_fill()
    pu()
    lt(90)
    fd(a/12)
    rt(90)
    pd()
    fillcolor('firebrick')
    begin_fill()
    circle(a/4)
    end_fill()
    pu()
    lt(90)
    fd(a/13)
    rt(90)
    pd()
    fillcolor('light salmon')
    begin_fill()
    circle(a/6)
    end_fill()

def karta17(a):
    pencolor("black")
    colormode(255)
    fillcolor('tan')
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()
    fd(a/2)
    pensize(2)
    pencolor('papaya whip')
    circle(a/4)
    pensize(1)
    pencolor('black')
    fd(a/2)
    lt(90)
    fd(a/2)
    pencolor('thistle')
    pensize(2)
    circle(a/4)
    pensize(1)
    pencolor('black')
    fd(a/2)
    lt(90)
    fd(a/2)
    pensize(2)
    pencolor('light blue')
    circle(a/4)
    pensize(1)
    pencolor('black')
    fd(a/2)
    lt(90)
    fd(a/2)
    pensize(2)
    pencolor('pale green')
    circle(a/4)

def okrenuta(a):
    pencolor("black")
    colormode(255)
    fillcolor('red')
    begin_fill()
    for i in range(4):
        fd(a)
        lt(90)
    end_fill()

#slova i brojevi
a=100

pu()
goto(-250,-250)
fd(a/2)
pd()
for i in range (6):
    turtle.write(chr(i+65))
    pu()
    fd(a)
    pd()

pu()
goto(-250,-250)
lt(90)
fd(a/2)
pd()
for i in range(1,7):
    turtle.write(str(i))
    pu()
    fd(a)
    pd()

#okrenute karte
pu()
rt(90)
goto(-235,-235)
pd()
for i in range(7):
    for j in range(6):
        okrenuta(a)
        pu()
        fd(a)
        pd()
    pu()
    goto(-235,-235+a*i)
    pd()

#memori
b=[i for i in range(0,18)]
for i in range (0,18):
    b.append(i)
shuffle(b,random)
r={}
abc=[chr(i) for i in range(ord('A'),ord('G'))]
jdt=[str(i) for i in range(1,7)]
L1=[]
for i in abc:
    for j in jdt:
        L1.append(i+j)
L2=[]
for i in range(len(b)):
    L2.append([b[i],L1[i]])
##print(L2) ODKOMENTIRATI ZA RJEŠENJA
##print(abc) --||--
##print(jdt) --||--
print('Unosi polja koja želiš otvoriti razdvojena razmakom (npr. A1 B4). ')    
br=18
lista=[]
while br!=0:
    p1=input('polja: ').split(' ')
    if p1[0] in lista or p1[1] in lista:
        print('Jedno od polja već je otvoreno.')
    else:
        crtac(a,L2[(ord(p1[0][0])-65)*6+int(p1[0][1])-1][0],ord(p1[0][0])-65,int(p1[0][1])-1)
        pu()
        home()
        pensize(1)
        pd()
        crtac(a,L2[(ord(p1[1][0])-65)*6+int(p1[1][1])-1][0],ord(p1[1][0])-65,int(p1[1][1])-1)

        pu()
        home()
        pensize(1)
        pd()
        
        if L2[(ord(p1[1][0])-65)*6+int(p1[1][1])-1][0]==L2[(ord(p1[0][0])-65)*6+int(p1[0][1])-1][0]:
            br-=1
            crtac(a,18,ord(p1[0][0])-65,int(p1[0][1])-1)
            crtac(a,18,ord(p1[1][0])-65,int(p1[1][1])-1)
            lista.append(p1[0])
            lista.append(p1[1])
        else:
            crtac(a,19,ord(p1[0][0])-65,int(p1[0][1])-1)
            crtac(a,19,ord(p1[1][0])-65,int(p1[1][1])-1)
        
print('Ti si najveći kralj ')  
        
    
    
    

    
