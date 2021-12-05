import random
import math
from bokeh.models.mappers import ColorMapper
from bokeh.plotting import figure, show

def graficar(x1, y1, x2 , y2 ):
    grafica = figure(title= "Area de pi con agujas" )
    grafica.scatter(x1,y1,color ="blue")
    grafica.scatter(x2,y2, color= "red")
    show(grafica)


def aventar_agujas(numero_agujas):
    dentro_del_circulo = 0
    X_blue = []
    Y_blue = []
    X_red = []
    Y_red = []

    for _ in range(numero_agujas):
        x = random.random()*random.choice([-1,1])
        y = random.random()*random.choice([-1,1])
        distancia_desde_el_centro = math.sqrt (x**2+ y**2) #radio 1
        if distancia_desde_el_centro <= 1:
            X_blue.append(x)
            Y_blue.append(y)
        else:
            X_red.append(x)
            Y_red.append(y)

        
    graficar(X_blue,Y_blue, X_red, Y_red)
       # if distancia_desde_el_centro <= 1:
        #    dentro_del_circulo += 1



if __name__ == '__main__' :
    aventar_agujas(10000)
