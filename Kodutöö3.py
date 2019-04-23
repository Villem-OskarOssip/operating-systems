#!/usr/bin/env python3
# vim: set fileencoding=utf8 :
# Näiteprogramm protsessoriaja planeerijate visualiseerimiseks
# algne autor Sten-Oliver Salumaa
# refaktoreerinud ja muidu muutnud Meelis Roos
# Meetodid joonista, Best, Worst, First ja Random on lisanud Villem-Oskar Ossip

from tkinter import *
import tkinter
from tkinter import ttk
from tkinter import messagebox
from random import randint


def puhasta():
    tahvel.delete('all')


# joonistab tahvlile protsesse kujutavad ristkülikud numbrite ja protsesside nimedega
def joonista(jarjend):
    puhasta()

    x0=50
    x1=62
    y0=30
    y1=42
    tulp = 0  # loendame tuplasid
    for i in range(0,50):
        kast = tahvel.create_rectangle(x0, y0, x1, y1)  # loome kasti
        tekst4 = tahvel.create_text(x0 + 6, y0 - 12, font=("Purisa", 6), text=str(tulp))  # nummerdame tulbad
        x0 += 12
        x1 += 12
        tulp+=1

    x0=50
    x1=62
    y0=30
    y1=42

    esimene = 0
    sügavus = 1
    eelmine = 0
    viimane = "+"
    sum = 0
    arv=0
    for i in jarjend:
        kontroll=False
        if i[0] == "x":
            if jarjend.count([49])==1:
                rist3 = tahvel.create_rectangle(x0 + (49 * 12), y0, x1 + (49 * 12), y1, fill="white")
            eelmine = 49
        if esimene < 1:
            rist1 = tahvel.create_line(x0 + (10 * 12), y0 , x1 + (10 * 12), y1)
            rist2 = tahvel.create_line(x1 + (10 * 12), y0, x0 + (10 * 12), y1)
            eelmine=10
            esimene+=1
            ring3 = tahvel.create_oval(x0 + (10 * 12) + 6 - 3, y0 + 30 - 3, x0 + (10 * 12) + 6 + 3, y0 + 30 + 3,fill="black")
        if viimane == "-":
            rist5 = tahvel.create_line(x0 + (i[0] * 12), y0, x1 + (i[0] * 12), y1)
            rist6 = tahvel.create_line(x1 + (i[0] * 12), y0, x0 + (i[0] * 12), y1)
            jooned = tahvel.create_line(x0 + (eelmine * 12) + 6, y0 + 30 + ((sügavus) * 12),
                                        x1 + ((i[0] - 1) * 12) + 6, y0 + 30 + ((sügavus) * 12),dash=(3,5))
            ring4 = tahvel.create_oval(x1 + (i[0] * 12) - 6 - 3, y1 + 30 + ((sügavus - 1) * 12) - 3,
                                       x1 + (i[0] * 12) - 6 + 3, y0 + 30 + ((sügavus) * 12) + 3, fill="black")
            arv+=i[0]-eelmine
            if (arv > 0):
                sum += arv
            if (arv<0):
                sum += (arv*(-1))
            arv = 0
            kontroll=True
            viimane="+"
            sügavus+=1
            eelmine=i[0]
        if i[0] != "-" and kontroll==False and i[0] !="x":
            rist3 = tahvel.create_line(x0+(i[0]*12), y0, x1+(i[0]*12), y1)
            rist4 = tahvel.create_line(x1 + (i[0] * 12), y0, x0 + (i[0] * 12), y1)
            jooned = tahvel.create_line(x0 + (eelmine * 12) + 6, y0+30+((sügavus-1)*12), x1 + ((i[0]-1) * 12) + 6, y0+30+((sügavus)*12))
            ring4 = tahvel.create_oval(x1 + (i[0] * 12) - 6 - 3, y1 + 30 + ((sügavus-1) * 12) - 3, x1 + (i[0] * 12) - 6 + 3,y0 + 30 + ((sügavus)* 12) + 3, fill="black")
            arv+=i[0]-eelmine
            if (arv > 0):
                sum += arv
            if (arv<0):
                sum += (arv*(-1))
            arv=0
            sügavus+=1
            eelmine = i[0]
        if i[0] == "-":
            sügavus-=1
            viimane = i[0]

    tekst = tahvel.create_text(x0+50, y1+160, font=("Purisa", 10), text=str("Summaarne teepikkus: " + str(sum)))  # nummerdame tulbad

def FCFS(jarjend):
    return (jarjend)

def SSTF(jarjend):

    valjund = []
    algus = 10
    x = 10000000
    for j in range(len(jarjend)):
        for i in jarjend:
            arv = i[0] - algus
            if (arv < 0):
                arv = arv * (-1)
            if (arv <= x):
                voti = i[0]
                x = arv
        algus = voti
        valjund.append([voti])
        b = jarjend.index([voti])
        del jarjend[b]
        x = 100000000

    return (valjund)

def SCAN(jarjend):
    valjund = []
    algus = 10
    jarjend.sort()
    pikkus = len(jarjend)
    for j in range(0, pikkus):
        kontroll = False
        for i in jarjend:
            if (i[0] > algus):
                algus = i[0]
                valjund.append([algus])
                b = jarjend.index([algus])
                del jarjend[b]
                kontroll = True
                break
        if (kontroll == False):
            algus = jarjend[0][0]
            if [49] not in valjund:
                valjund.append([49])
                valjund.append(["x"])
            pikkus2 = len(jarjend)
            for l in range(0, pikkus2):
                valjund.append(jarjend[-1])
                b = jarjend.index(jarjend[-1])
                del jarjend[b]

            return (valjund)

def CLOOK(jarjend):
    valjund = []
    algus = 10
    jarjend.sort()
    pikkus = len(jarjend)
    for j in range(0,pikkus):
        kontroll = False
        for i in jarjend:
            if (i[0] > algus):
                algus = i[0]
                valjund.append([algus])
                b = jarjend.index([algus])
                del jarjend[b]
                kontroll = True
                break
        if (kontroll == False):
            algus = jarjend[0][0]
            valjund.append(["-"])
            valjund.append([algus])
            b = jarjend.index([algus])
            del jarjend[b]
            kontroll = True

    return (valjund)

def massiiviks(input_jarjend):
    valjund = []
    jupid = input_jarjend.split(",")
    for i in (jupid):
        valjund.append([int(i)])
    return valjund

def massiiviMeister():
    jarjend = []
    if var.get() == 1:
        return massiiviks(predef1)
    elif var.get() == 2:
        return massiiviks(predef2)
    elif var.get() == 3:
        return massiiviks(predef3)
    elif var.get() == 4:
        try:
            return massiiviks(kasutaja_jarjend.get())
        except:
            messagebox.showerror(title="Viga sisendis", message="Vigane kasutaja muster!")
            return massiiviks(predef1)
    else:
        return massiiviks(predef1)


def kasuvalija(jarjend, algoritm):
    if algoritm == "FCFS":
        return FCFS(jarjend)
    elif algoritm == "SSTF":
        return SSTF(jarjend)
    elif algoritm == "SCAN":
        return SCAN(jarjend)
    elif algoritm == "C-LOOK":
       return CLOOK(jarjend)


def jooksuta_algoritmi(algoritm):
    jarjend = massiiviMeister()
    jarjend2 = jarjend[:]
    valjund = kasuvalija(jarjend, algoritm)
    joonista(valjund)

predef1 = "2,5,13,29,7,1,18,40,49,4"
predef2 = "1,10,44,2,12,3,13,20"
predef3 = "45,6,16,9,33,28,11,37,49,25"

# GUI
raam = Tk()
raam.title("Planeerimisalgoritmid")
raam.resizable(True, True)
raam.geometry("800x600")

var = IntVar()
var.set(1)
Radiobutton(raam, text="Esimene", variable=var, value=1).place(x=10, y=40)
Radiobutton(raam, text="Teine", variable=var, value=2).place(x=10, y=70)
Radiobutton(raam, text="Kolmas", variable=var, value=3).place(x=10, y=100)
Radiobutton(raam, text="Enda oma", variable=var, value=4).place(x=10, y=130)

silt_vali = ttk.Label(raam, text="Vali või sisesta järjend (kujul 1,10,4,2,12,3,13,2)")
silt_vali.place(x=10, y=10)

silt1 = ttk.Label(raam, text=predef1)
silt1.place(x=120, y=40)

silt2 = ttk.Label(raam, text=predef2)
silt2.place(x=120, y=70)

silt3 = ttk.Label(raam, text=predef3)
silt3.place(x=120, y=100)

silt_run = ttk.Label(raam, text="Algoritmi käivitamiseks klõpsa nupule")
silt_run.place(x=10, y=160)

kasutaja_jarjend = ttk.Entry(raam)
kasutaja_jarjend.place(x=120, y=130, height=25, width=240)

tahvel = Canvas(raam, width=800, height=400, background="white")
tahvel.place(x=0, y=220)

Best_nupp = ttk.Button(raam, text="SSTF", command=lambda: jooksuta_algoritmi("SSTF"))
Best_nupp.place(x=100, y=190, height=25, width=80)

Worst_nupp = ttk.Button(raam, text="SCAN", command=lambda: jooksuta_algoritmi("SCAN"))
Worst_nupp.place(x=190, y=190, height=25, width=80)

Random_nupp = ttk.Button(raam, text="C-LOOK", command=lambda: jooksuta_algoritmi("C-LOOK"))
Random_nupp.place(x=280, y=190, height=25, width=80)

First_nupp = ttk.Button(raam, text="FCFS", command=lambda: jooksuta_algoritmi("FCFS"))
First_nupp.place(x=10, y=190, height=25, width=80)

puhasta_nupp = ttk.Button(raam, text="Puhasta väljund", command=lambda: puhasta())
puhasta_nupp.place(x=460, y=190, height=25, width=80)

raam.mainloop()