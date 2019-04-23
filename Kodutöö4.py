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

    x0 = 80
    x1 = 90
    y0 = 30
    y1 = 45
    for i in jarjend:
        if jarjend.index(i) >0:
            Samm = tahvel.create_text(x0 - 30, y0 + 7.5, font=("Purisa", 7), text="Samm " + str(jarjend.index(i)) )
        for j in range(0,50):
            if i[0][j] == "-":
                kast = tahvel.create_rectangle(x0, y0, x1, y1)  # loome kasti
                x0 += 10
                x1 += 10
            else:
                kast = tahvel.create_rectangle(x0, y0, x1, y1, fill="orange")
                taht = tahvel.create_text(x0 + 5, y0 + 7.5, font=("Purisa", 7), text=i[0][j])
                x0 += 10
                x1 += 10
        y0 += 20
        y1 += 20
        x0 = 80
        x1 = 90



def Programm(jarjend):
    kohad=[]
    vaba=[]
    set = []

    for j in range(0, 50):
        vaba.append("-")

    for k in jarjend:
        if "-" not in vaba:
            kohad = []
            return
        kontroll2 = 0
        c = vaba[:]
        kohad.append([])
        kohad[-1].append(c)
        kontroll = 0
        if k[0] in vaba:
            for v in range(0,50):
                if vaba[v] ==k[0]:
                    vaba[v] = "-"
                    kontroll2 = 1
        if  k[0] not in vaba and kontroll2 != 1:
            for z in range(0, 50):
                if kontroll >= int(k[1]):
                    break
                if "-" not in vaba:
                    kohad = []
                    return
                if vaba[z] =="-":
                    vaba[z] = k[0]
                    kontroll+=1
    if "-" not in vaba:
        kohad = []
        return (kohad)
    c = vaba[:]
    kohad.append([])
    kohad[-1].append(c)
    return (kohad)

def Arvutused (jarjend):
    text.delete(1.0, END)
    if len(jarjend)==0:
        text.insert(INSERT, "Töö lõpetati, sest pole piisavalt ruumi.")
        return

    myset = list(set(jarjend[-1][0]))
    poolik = 0
    tahed = []
    kokku =0
    y=0
    for i in myset:
        kontroll1 = 0
        kontroll2 = 0
        kontroll3 = 0
        x = 0
        for j in jarjend[-1][0]:
            if j != "-" and y!=1:
                kokku +=1
            if i == j and kontroll1 == 0:
                kontroll1=1
            if kontroll1==1 and kontroll2==0 and i != j:
                kontroll2=1
            if kontroll1==1 and kontroll2==1 and kontroll3==0 and i==j:
                kontroll3=1
            if kontroll1==1 and kontroll2==1 and kontroll3==1 and x!=1 and j!="-":
                poolik +=1
                tahed.append(j)
                x+=1
        y =1

    a1 = float("{0:.2f}".format((poolik / (len(myset)-1)*100)))

    kast=0
    for i in tahed:
        for j in jarjend[-1][0]:
            if j == i:
                kast+=1

    a2 = float("{0:.2f}".format((kast/kokku)*100))


    text.insert(INSERT, "Allesjäänud failidest on fragmenteerunud " +str(a1)+ "%." + "\n")
    text.insert(INSERT, "Fragmenteerunud failidele kuulub " + str(a2) + "% kasutatud" +"\n"+"ruumist.")


def massiiviks(input_jarjend):
    valjund = []
    jupid = input_jarjend.split(";")
    for i in (jupid):
        tükid = i.split(",")
        valjund.append([tükid[0],tükid[1]])
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
    if algoritm == "Programm":
        return Programm(jarjend)


def jooksuta_algoritmi(algoritm):
    jarjend = massiiviMeister()
    #jarjend2 = jarjend[:]
    valjund = kasuvalija(jarjend, algoritm)
    Arvutused(valjund)
    joonista(valjund)

predef1 = "A,2;B,3;A,-;C,4;D,5;B,-;E,5"
predef2 = "A,4;B,3;C,6;D,5;B,-;E,5;A,-;F,10"
predef3 = "A,2;B,3;C,4;D,5;B,-;E,7;D,-;F,10;A,-;G,1;H,1;G,-;I,10;J,8;I,-"

# GUI
raam = Tk()
raam.title("Planeerimisalgoritmid")
raam.resizable(True, True)
raam.geometry("900x600")

var = IntVar()
var.set(1)
Radiobutton(raam, text="Esimene", variable=var, value=1).place(x=10, y=40)
Radiobutton(raam, text="Teine", variable=var, value=2).place(x=10, y=70)
Radiobutton(raam, text="Kolmas", variable=var, value=3).place(x=10, y=100)
Radiobutton(raam, text="Enda oma", variable=var, value=4).place(x=10, y=130)

silt_vali = ttk.Label(raam, text="Vali või sisesta järjend (kujul A,2;B,3;A,-;C,4;D,5;B,-;E,15). Max 10 faili.")
silt_vali.place(x=10, y=10)

silt1 = ttk.Label(raam, text=predef1)
silt1.place(x=120, y=40)

silt2 = ttk.Label(raam, text=predef2)
silt2.place(x=120, y=70)

silt3 = ttk.Label(raam, text=predef3)
silt3.place(x=120, y=100)

kasutaja_jarjend = ttk.Entry(raam)
kasutaja_jarjend.place(x=120, y=130, height=25, width=240)

tahvel = Canvas(raam, width=900, height=400, background="white")
tahvel.place(x=0, y=220)

First_nupp = ttk.Button(raam, text="Käivita", command=lambda: jooksuta_algoritmi("Programm"))
First_nupp.place(x=10, y=160, height=40, width=80)

puhasta_nupp = ttk.Button(raam, text="Puhasta väljund", command=lambda: puhasta())
puhasta_nupp.place(x=120, y=160, height=40, width=120)

text = Text(raam, width=50, height=9)
text.place(x=450, y=30)

silt_kast = ttk.Label(raam, text="Arvutused: ")
silt_kast.place(x=450, y=10)

raam.mainloop()