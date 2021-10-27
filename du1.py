from turtle import *
from math import sqrt

vertikalni = 4
horizontalni = 4
strana = 20
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
    

exitonclick()