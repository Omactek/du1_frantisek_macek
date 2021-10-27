from turtle import *
from math import sqrt

vertikalni = 4
horizontalni = 4
strana = 20
p_pol = horizontalni*vertikalni
speed(0)

#získání souřadnice vertikalni
d = round(2*(sqrt(strana**2-(strana/2)**2)),2) #výpočet dálky pátého vrcholu šestiúhelníku od prvního
print(d)

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
if p_pol % 2 == 0: #pro sudý počet polí
    for _ in range(int(p_pol/2)):
        x = int(input(f"První hráči, zadejte souřadnici x od 1 do {horizontalni}"))
        while x > horizontalni or x < 1:
            print("Špatný vstup")
            x = int(input(f"První hráči, zadejte souřadnici x od 1 do {horizontalni}"))
        x = x - 1
        y = int(input(f"První hráči, zadejte souřadnici y od 1 do {vertikalni}"))
        while y > horizontalni or y < 1:
            print("Špatný vstup")
            y = int(input(f"První hráči, zadejte souřadnici y od 1 do {vertikalni}"))
        y = y - 1
        
        #vykresleni krizku
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

        #vykresleni kolecka
        


exitonclick()