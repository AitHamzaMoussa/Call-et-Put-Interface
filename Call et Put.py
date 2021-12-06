from math import *
import pandas as pd
import numpy as np
from scipy.stats.distributions import norm

from tkinter import *

def action():
    N=float(k.get())
    B=float(S.get())
    D=float(T.get())
    F=float(t.get())
    G=float(v.get())
    H = float(r.get())
    D1=float((log(B/N)+(H+0.5*(G**2))*(D-F))/(G*sqrt(D-F)))
    N2=norm.cdf(D1, 0.0, 1.0)
    nd1.delete(0, END)
    nd1.insert(1, N2)

def action2():
    N = float(k.get())
    B = float(S.get())
    D = float(T.get())
    F= float(t.get())
    G=float(v.get())
    H=float(r.get())
    D2 = float((log(B / N) + (H - 0.5 * (G ** 2)) * (D - F)) / (G * sqrt(D - F)))
    N3 = norm.cdf(D2, 0.0, 1.0)
    nd2.delete(0, END)
    nd2.insert(1, N3)

def Call():
    N = float(k.get())
    B = float(S.get())
    D = float(T.get())
    F = float(t.get())
    G = float(v.get())
    H = float(r.get())
    D1 = float((log(B / N) + (H + 0.5 * (G ** 2)) * (D - F)) / (G * sqrt(D - F)))
    N2 = norm.cdf(D1, 0.0, 1.0)
    D2 = float((log(B / N) + (H - 0.5 * (G ** 2)) * (D - F)) / (G * sqrt(D - F)))
    N3 = norm.cdf(D2, 0.0, 1.0)
    N4= B*N2-N*exp(-H*(D-F))*N3

    C.delete(0,END)
    C.insert(0,N4)

def action3():
    N=float(k.get())
    B=float(S.get())
    D=float(T.get())
    F=float(t.get())
    G=float(v.get())
    H = float(r.get())
    D1 = float((log(B / N) + (H + 0.5 * (G ** 2)) * (D - F)) / (G * sqrt(D - F)))
    N2 = norm.cdf(-D1, 0.0, 1.0)
    nd3.delete(0, END)
    nd3.insert(1, N2)

def action4():
    N = float(k.get())
    B = float(S.get())
    D = float(T.get())
    F= float(t.get())
    G=float(v.get())
    H=float(r.get())
    D2 = float((log(B / N) + (H - 0.5 * (G ** 2)) * (D - F)) / (G * sqrt(D - F)))
    N3 = norm.cdf(-D2, 0.0, 1.0)
    nd4.delete(0, END)
    nd4.insert(1, N3)


def Put():
    N = float(k.get())
    B = float(S.get())
    D = float(T.get())
    F = float(t.get())
    G = float(v.get())
    H = float(r.get())
    D1 = float((log(B / N) + (H + 0.5 * (G ** 2)) * (D - F)) / (G * sqrt(D - F)))
    N2 = norm.cdf(-D1, 0.0, 1.0)
    D2 = float((log(B / N) + (H - 0.5 * (G ** 2)) * (D - F)) / (G * sqrt(D - F)))
    N3 = norm.cdf(-D2, 0.0, 1.0)
    N5= N*exp(-H*(D-F))*N3-B*N2

    p.delete(0,END)
    p.insert(0,N5)

fen = Tk()

fen.geometry("900x450")

labelnombre2= Label(fen, text= "Entrer le strike")
labelnombre2.place(x = 20, y = 20)
k= Entry(fen)
k.place(x=200, y=20)

labelnombre2= Label(fen, text= "Entrer le prix en t")
labelnombre2.place(x = 400, y = 20)
S= Entry(fen)
S.place(x=600, y=20)

labelnombre3= Label(fen, text= "Entrer Echeance")
labelnombre3.place(x = 20, y = 60)
T= Entry(fen)
T.place(x=200, y=60)

labelnombre4= Label(fen, text= "Entrer t")
labelnombre4.place(x = 400, y = 60)
t= Entry(fen)
t.place(x=600, y=60)

labelnombre5= Label(fen, text= "Entrer la volatilité")
labelnombre5.place(x = 20, y = 100)
v= Entry(fen)
v.place(x=200, y=100)

labelnombre6= Label(fen, text= "Entrer le taux")
labelnombre6.place(x = 400, y = 100)
r= Entry(fen)
r.place(x=600, y=100)

#******* Cas du Call***********

labelnombre7= Label(fen, text= "Actif risque Call")
labelnombre7.place(x = 20, y = 140)
nd1= Entry(fen)
nd1.place(x=200, y=140)

labelnombre8= Label(fen, text= "Actif sans risque Call")
labelnombre8.place(x = 400, y = 140)
nd2= Entry(fen)
nd2.place(x=600, y=140)

#******* Cas du Call***********

labelnombre9= Label(fen, text= "Actif risque Put")
labelnombre9.place(x = 20, y = 180)
nd3= Entry(fen)
nd3.place(x=200, y=180)

labelnombre10= Label(fen, text= "Actif sans risque Put")
labelnombre10.place(x = 400, y = 180)
nd4= Entry(fen)
nd4.place(x=600, y=180)

#************ valeur du Call *******
labelnombre11= Label(fen, text= "Valeur du Call")
labelnombre11.place(x = 400, y = 220)
C= Entry(fen)
C.place(x=600, y=220)

#************ valeur du Put*******
labelnombre12= Label(fen, text= "Valeur du Put")
labelnombre12.place(x = 400, y = 260)
p= Entry(fen)
p.place(x=600, y=260)

#************ Les Buttons**************

Valider= Button(fen, text= "Actif risque Call", command=action)
Valider.place(x=20, y=240)

Valider2= Button(fen, text= "Actif sans risque Call", command=action2)
Valider2.place(x=20, y=270)
Valider3= Button(fen, text= "Call", command=Call)
Valider3.place(x=20, y=300)
#********PUT*********


Valider6= Button(fen, text= "Put", command=Put)
Valider6.place(x=20, y=390)

Valider4= Button(fen, text= "Actif risque Put", command=action3)
Valider4.place(x=20, y=330)


Valider5= Button(fen, text= "Actif sans risque Put", command=action4)
Valider5.place(x=20, y=360)


fen.mainloop()