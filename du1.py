from turtle import left,right,up,down,setposition,circle,color,width,speed,forward,exitonclick
from math import sqrt

def wrong_input():
    print("Špatný vstup")

vertikalni = int(input("Zadejte vertikalni počet polí: "))
while vertikalni < 1:
    wrong_input()
    vertikalni = int(input("Zadejte vertikalni počet polí: "))

horizontalni = int(input("Zadejte horizontální počet polí: "))
while horizontalni < 1:
    wrong_input()
    horizontalni = int(input("Zadejte horizontální počet polí: "))

strana = 20
p_pol = horizontalni*vertikalni #počet polí
speed(0)

d = round(2*(sqrt(strana**2-(strana/2)**2)),2) #výpočet dálky pátého vrcholu šestiúhelníku od prvního

#vykreslení sítě
for i in range(vertikalni):
    up()
    setposition(0,d*i)
    down()
    for _ in range(horizontalni):
        for _ in range(7):
            forward(strana)
            left(60)
        forward(strana)
        right(60)

#hra
width(2)
for v in range(p_pol): #opakuje dokud není počet zahrání stejný jako počet polí
    if v % 2 == 0: #pro prvního hráče
        x = int(input(f"První hráči, zadejte souřadnici x od 1 do {horizontalni}: "))
        while x > horizontalni or x < 1: #zabraňuje vstupu mimo pole
            wrong_input()
            x = int(input(f"První hráči, zadejte souřadnici x od 1 do {horizontalni}: "))
        x = x - 1 #převod na souřadnice, které používá turtle
        y = int(input(f"První hráči, zadejte souřadnici y od 1 do {vertikalni}: "))
        while y > vertikalni or y < 1: #zabraňuje vstupu mimo pole
            wrong_input()
            y = int(input(f"První hráči, zadejte souřadnici y od 1 do {vertikalni}: "))
        y = y - 1 #převod na souřadnice, které používá turtle
            
        #vykresleni krizku
        color("blue")
        sourad_y = y + (x*0.5)
        up()
        setposition(strana*x*1.5,d*sourad_y)
        down()
        left(60)
        forward(2*strana)
        up()
        setposition(strana*x*1.5,d*(sourad_y+1))
        down()
        right(120)
        forward(2*strana)
        left(60)

    else:  #pro druhého hráče
        x = int(input(f"Druhý hráči, zadejte souřadnici x od 1 do {horizontalni}: "))
        while x > horizontalni or x < 1:
            wrong_input()
            x = int(input(f"Druhý hráči, zadejte souřadnici x od 1 do {horizontalni}: "))
        x = x - 1
        y = int(input(f"Druhý hráči, zadejte souřadnici y od 1 do {vertikalni}: "))
        while y > vertikalni or y < 1:
            wrong_input()
            y = int(input(f"Druhý hráči, zadejte souřadnici y od 1 do {vertikalni}: "))
        y = y - 1   

        #vykreslení kolečka
        color("red")
        sourad_y = y + (x*0.5)
        up()
        setposition(strana*x*1.5+(strana*0.5),d*sourad_y+(d*0.2))
        down()
        circle(d*0.3)

print("Hra skončila")

exitonclick()