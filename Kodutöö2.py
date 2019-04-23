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
def joonista(jarjend, algne):
    puhasta()
    x0 = 110 #määrame 0,0  koordinaadid ehk määrame ruudustiku kõige ülemise ja vasakpoolseima asukoha
    y0 = 40
    x1 = 122
    y1 = 52
    tulp = 1 #loendame tuplasid
    rida = 1 #loendame ridu
    kontroll = 0
    tekst0 = tahvel.create_text(x0 - 62, y0 -22, font=("Purisa", 7), text="Etapp") #lisame kirje
    tekst1 = tahvel.create_text(x0 - 22, y0 - 22, font=("Purisa", 7), text="Lisatud")#lisame kirje
    tekst2 = tahvel.create_text(x0 - 22, y0 - 12, font=("Purisa", 7), text="protsess")#lisame kirje
    for i in range(0, 10): #algselt joonistame ruudustiku, mis on 10 kõrge
        tekst3 = tahvel.create_text(x0 -62, y0+6, font=("Purisa", 6), text=str(rida)) #nummerdame read
        rida += 1
        for j in range(0, 50): #joonistame ruudustiku, mi on 50 lai
            if i < 1:
                tekst4 = tahvel.create_text(x0+6, y0-12, font=("Purisa", 6), text=str(tulp)) #nummerdame tulbad
                tulp += 1
            kast = tahvel.create_rectangle(x0, y0, x1, y1,fill="gray") #loome kasti
            keskpaik_x = x0 + 6
            keskpaik_y = y0 + 6
            kriips = tahvel.create_text(keskpaik_x, keskpaik_y, text="-") #täidame sisu kriipsuga
            x0 += 12
            x1 += 12
        x1 = 122
        x0 = 110
        y0 += 12
        y1 += 12
    x0 = 110
    y0 = 40
    x1 = 122
    y1 = 52
    varvid = [["green"], ["red"], ["orange"], ["blue"], ["yellow"], ["purple"], ["SeaGreen1"], ["brown1"], ["pink"],["yellow4"]] #värvide list
    tahed = [["A"], ["B"], ["C"], ["D"], ["E"], ["F"], ["G"], ["H"], ["I"],["J"]] #tähtede list
    kontroll = 10
    suurim=0
    taheke = 0
    kriipsuke = tahvel.create_text(75, 45, font=("Purisa", 7), text="-") #lisame tühja kriipsu
    for a in jarjend: #teeme nii kaua kui jarjendis on elemente
        protsessid = tahvel.create_text(80, 60 + taheke, font=("Purisa", 7), text=algne[jarjend.index(a)]) #lisame algsest jarjendite listist jarjendid külejpeale
        protsessid = tahvel.create_text(66, 60 + taheke, font=("Purisa", 7), text=":")
        tahekesed = tahvel.create_text(60, 60 + taheke, font=("Purisa", 7), text=tahed[jarjend.index(a)]) #lisaem tähed juurde jarjenditele
        taheke += 12
        for b in a:
            if b == "!": #kui jarjend sisaldab hüiumaärk siis
                a0 = 40+(jarjend.index(a)*12)
                keskpaik_x = x0 + 300
                keskpaik_y = a0 +6
                tuhjus = tahvel.create_rectangle(x0-100, a0, 710, a0 + (12 * suurim), fill="white", outline="white") #kustutab koik allapoole jääva
                error = tahvel.create_rectangle(x0,a0,710,a0+12,fill="gray30") #loob errori tahvli
                errorTekst = tahvel.create_text(keskpaik_x, keskpaik_y,font=("Purisa", 7), text="Protsess ei mahu mällu") #lisame eroori tahvlile teksti
                return #lopetame töö
            if (b[1][1]) >= suurim:
                suurim = b[1][1]
            if (b[0][1]) >= kontroll:
                for j in range(0, 50):
                    kast2 = tahvel.create_rectangle(x0, y0+12*(kontroll), x1, y1+12*(kontroll), fill="gray")
                    keskpaik_x = x0 + 6
                    keskpaik_y = y0+12*(kontroll)+6
                    kriips = tahvel.create_text(keskpaik_x, keskpaik_y, text="-")
                    x0 += 12
                    x1 += 12
                tekst3 = tahvel.create_text(48, y0+12*(kontroll) + 6, font=("Purisa", 6), text=str(rida))
                rida += 1
                x0 = 110
                x1=122
                y0 = 40
                kontroll +=1
            sisend_kast = tahvel.create_rectangle(x0+(b[0][0])*12, y0+(b[0][1])*12,
                                                  x0+(b[1][0])*12, y0+(b[1][1])*12, fill=varvid[jarjend.index(a)])
            taht = tahvel.create_text(x0+(b[0][0])*12+6,y0+(b[0][1])*12+6, font=("Purisa", 6), text=tahed[jarjend.index(a)])


def First(jarjend):
    valjund = []

    for i in range(0,len(jarjend)):
        valjund.append([])

    vabadKohad = []
    for x in range(0,20):
        for y in range(0,50):
            vabadKohad.append([])
            vabadKohad[-1].append(y)
            vabadKohad[-1].append(x)

    kast = 0
    veerg =0
    for k in range(0,jarjend[0][0]):
        veerg += 1
        for j in range(0, jarjend[0][1]):
            valjund[0].append([]) #loome kasti
            valjund[0][kast].append([]) #lisame esimese koordinaadi
            valjund[0][kast][0].append(k) #lisame x0
            valjund[0][kast][0].append(j) #lisame y0
            valjund[0][kast].append([])  # lisame teise koordinaadi
            valjund[0][kast][1].append(k+1)  # lisame x1
            valjund[0][kast][1].append(j+1)  # lisame y2
            if (valjund[0][kast][0]) in vabadKohad:
                kustuta = valjund[0][kast][0]
                vabadKohad.remove(valjund[0][kast][0])

            kast += 1
    del jarjend[0] #eemaldame esimese elemendi listist
    jarg = 0
    puder = []
    for i in jarjend:
        veerud = i[0]
        jarg+=1
        kast = 0
        kontroll = False
        while kontroll == False:
            liikunud = 0
            for k in range(0, 50):
                korgus = 0
                if veerud != 0:
                    kontroll = False
                    for j in range(0+jarg, 20):
                        if len(valjund[jarg]) < i[0]*i[1]:
                            if kontroll == True:
                                break
                            puder.append(k)
                            puder.append(j)
                            if puder not in vabadKohad:
                                del puder[0]
                                del puder[0]
                                break
                            if k + veerud > 50:
                                valjund[jarg].append("!")
                                return valjund
                            if (korgus < i[1]):
                                for x in range(0, i[0]-liikunud):
                                    if x+k >=49:
                                        break
                                    tühjus = []
                                    tühjus.append(k+x)
                                    tühjus.append(j)
                                    if tühjus not in vabadKohad:
                                        kontroll = True
                                        del puder[0]
                                        del puder[0]
                                        del tühjus[0]
                                        del tühjus[0]
                                        break
                                    del tühjus[0]
                                    del tühjus[0]
                                if kontroll == True:
                                    break
                                muutuja = valjund[jarg]
                                valjund[jarg].append([])  # lisame esimese koordinaadi
                                valjund[jarg][kast].append([])
                                valjund[jarg][kast][0].append(k)  # lisame x0
                                valjund[jarg][kast][0].append(j)  # lisame y0
                                valjund[jarg][kast].append([])  # lisame teise koordinaadi
                                valjund[jarg][kast][1].append(k + 1)  # lisame x1
                                valjund[jarg][kast][1].append(j + 1)  # lisame y2
                                vabadKohad.remove(valjund[jarg][kast][0])
                                kast +=1
                                korgus +=1
                                if korgus == i[1]:
                                    veerg +=1
                                    veerud -= 1
                                    liikunud +=1
                            del puder[0]
                            del puder[0]
            if k == 49:
                kontroll = True

    return (valjund)

def Worst(jarjend):
    valjund = []

    for i in range(0,len(jarjend)):
        valjund.append([])

    vabadKohad = []
    for x in range(0,20):
        for y in range(0,50):
            vabadKohad.append([])
            vabadKohad[-1].append(y)
            vabadKohad[-1].append(x)

    kast = 0
    veerg = 0
    for k in range(0,jarjend[0][0]):
        veerg +=1
        for j in range(0, jarjend[0][1]):
            valjund[0].append([]) #loome kasti
            valjund[0][kast].append([]) #lisame esimese koordinaadi
            valjund[0][kast][0].append(k) #lisame x0
            valjund[0][kast][0].append(j) #lisame y0
            valjund[0][kast].append([])  # lisame teise koordinaadi
            valjund[0][kast][1].append(k+1)  # lisame x1
            valjund[0][kast][1].append(j+1)  # lisame y2
            if (valjund[0][kast][0]) in vabadKohad:
                kustuta = valjund[0][kast][0]
                vabadKohad.remove(valjund[0][kast][0])

            kast += 1
    esimeneVaba = jarjend[0][0]
    del jarjend[0] #eemaldame esimese elemendi listist
    jarg = 0
    puder = []
    puder2=[]
    liikumine=0
    for i in jarjend:
        veerud = i[0]
        korgus = 0
        jarg+=1
        kast = 0
        vaba=[]
        parim=[[[]]]
        vahed = []
        for k in range(0+jarg, 20):
            for j in range(0, 50):
                puder.append(j)
                puder.append(k)
                if puder not in vabadKohad:
                    if (k - jarg == 0):
                        vaba.append("-")
                    del puder[0]
                    del puder[0]
                if puder in vabadKohad:
                    if (k - jarg == 0):
                        vaba.append("+")
                    del puder[0]
                    del puder[0]
                if (j == 49) and (k-jarg==0):
                    for t in range(0,len(vaba)):
                        if vaba[t] =="-":
                            if (t >=1) and (vaba[t-1]=="+"):
                                parim.append([[]])
                            if t < len(vaba)-1:
                                if vaba[t+1] == "+":
                                    muutuja = parim[-1][0]
                                    parim[-1][0].append(t+1)
                                    parim[-1][0].append(k)
                                    parim[-1].append(0)
                        if vaba[t] == "+" and t ==0:
                            parim[-1][0].append(t)
                            parim[-1][0].append(k)
                            parim[-1].append(0)
                        if vaba[t] =="+":
                            parim[-1][-1]+=1
                    if parim[-1] == [[]]:
                        del parim[-1]
                    x=0
                    vahe =0
                    for z in range(0,len(parim)):
                        if (vahe <= parim[z][-1]):
                            if (parim[z][-1] > x):
                                if (i[0]<=parim[z][-1]):
                                    vahe = parim[z][-1]
                                    x = parim[z][0][0]
                    if x == 0 and vahe == 0:
                        valjund[jarg].append("!")
                        return valjund
                    if x + i[0] > 50:
                        valjund[jarg].append("!")
                        return valjund
                if (j==49) and (korgus < i[1]):
                    for a in range(0,veerud):
                        valjund[jarg].append([])  # lisame esimese koordinaadi
                        valjund[jarg][kast].append([])
                        valjund[jarg][kast][0].append(x+a)  # lisame x0
                        valjund[jarg][kast][0].append(k)  # lisame y0
                        valjund[jarg][kast].append([])  # lisame teise koordinaadi
                        valjund[jarg][kast][1].append(x+a+1)  # lisame x1
                        valjund[jarg][kast][1].append(k+1)  # lisame y2
                        if valjund[jarg][kast][0] in vabadKohad:
                            vabadKohad.remove(valjund[jarg][kast][0])
                        kast += 1
                    korgus +=1
                    break
    return (valjund)


def Best(jarjend):
    valjund = []

    for i in range(0, len(jarjend)):
        valjund.append([])

    vabadKohad = []
    for x in range(0, 20):
        for y in range(0, 50):
            vabadKohad.append([])
            vabadKohad[-1].append(y)
            vabadKohad[-1].append(x)

    kast = 0
    veerg = 0
    for k in range(0, jarjend[0][0]):
        veerg += 1
        for j in range(0, jarjend[0][1]):
            valjund[0].append([])  # loome kasti
            valjund[0][kast].append([])  # lisame esimese koordinaadi
            valjund[0][kast][0].append(k)  # lisame x0
            valjund[0][kast][0].append(j)  # lisame y0
            valjund[0][kast].append([])  # lisame teise koordinaadi
            valjund[0][kast][1].append(k + 1)  # lisame x1
            valjund[0][kast][1].append(j + 1)  # lisame y2
            if (valjund[0][kast][0]) in vabadKohad:
                kustuta = valjund[0][kast][0]
                vabadKohad.remove(valjund[0][kast][0])

            kast += 1
    esimeneVaba = jarjend[0][0]
    del jarjend[0]  # eemaldame esimese elemendi listist
    jarg = 0
    puder = []
    puder2 = []
    liikumine = 0
    for i in jarjend:
        veerud = i[0]
        korgus = 0
        jarg += 1
        kast = 0
        vaba = []
        parim = [[[]]]
        vahed = []
        for k in range(0 + jarg, 20):
            for j in range(0, 50):
                puder.append(j)
                puder.append(k)
                if puder not in vabadKohad:
                    if (k - jarg == 0):
                        vaba.append("-")
                    del puder[0]
                    del puder[0]
                if puder in vabadKohad:
                    if (k - jarg == 0):
                        vaba.append("+")
                    del puder[0]
                    del puder[0]
                if (j == 49) and (k - jarg == 0):
                    for t in range(0, len(vaba)):
                        if vaba[t] == "-":
                            if (t >= 1) and (vaba[t - 1] == "+"):
                                parim.append([[]])
                            if t < len(vaba) - 1:
                                if vaba[t + 1] == "+":
                                    muutuja = parim[-1][0]
                                    parim[-1][0].append(t + 1)
                                    parim[-1][0].append(k)
                                    parim[-1].append(0)
                        if vaba[t] == "+" and t == 0:
                            parim[-1][0].append(t)
                            parim[-1][0].append(k)
                            parim[-1].append(0)
                        if vaba[t] == "+":
                            parim[-1][-1] += 1
                    if parim[-1] == [[]]:
                        del parim[-1]
                    x = 0
                    vahe = 50
                    for z in range(0, len(parim)):
                        if (i[0] <= parim[z][-1]):
                            if (parim[z][-1] < vahe):
                                vahe = parim[z][-1]
                                x = parim[z][0][0]
                    if x == 0 and vahe == 0:
                        valjund[jarg].append("!")
                        return valjund
                    if x + i[0] > 50:
                        valjund[jarg].append("!")
                        return valjund
                if (j == 49) and (korgus < i[1]):
                    for a in range(0, veerud):
                        valjund[jarg].append([])  # lisame esimese koordinaadi
                        valjund[jarg][kast].append([])
                        valjund[jarg][kast][0].append(x + a)  # lisame x0
                        valjund[jarg][kast][0].append(k)  # lisame y0
                        valjund[jarg][kast].append([])  # lisame teise koordinaadi
                        valjund[jarg][kast][1].append(x + a + 1)  # lisame x1
                        valjund[jarg][kast][1].append(k + 1)  # lisame y2
                        if valjund[jarg][kast][0] in vabadKohad:
                            vabadKohad.remove(valjund[jarg][kast][0])
                        kast += 1
                    korgus += 1
                    break
    return (valjund)


def Random(jarjend):
    valjund = []

    for i in range(0, len(jarjend)):
        valjund.append([])

    vabadKohad = []
    for x in range(0, 20):
        for y in range(0, 50):
            vabadKohad.append([])
            vabadKohad[-1].append(y)
            vabadKohad[-1].append(x)

    kast = 0
    veerg = 0
    for k in range(0, jarjend[0][0]):
        veerg += 1
        for j in range(0, jarjend[0][1]):
            valjund[0].append([])  # loome kasti
            valjund[0][kast].append([])  # lisame esimese koordinaadi
            valjund[0][kast][0].append(k)  # lisame x0
            valjund[0][kast][0].append(j)  # lisame y0
            valjund[0][kast].append([])  # lisame teise koordinaadi
            valjund[0][kast][1].append(k + 1)  # lisame x1
            valjund[0][kast][1].append(j + 1)  # lisame y2
            if (valjund[0][kast][0]) in vabadKohad:
                kustuta = valjund[0][kast][0]
                vabadKohad.remove(valjund[0][kast][0])

            kast += 1
    esimeneVaba = jarjend[0][0]
    del jarjend[0]  # eemaldame esimese elemendi listist
    jarg = 0
    puder = []
    puder2 = []
    liikumine = 0
    for i in jarjend:
        veerud = i[0]
        korgus = 0
        jarg += 1
        kast = 0
        vaba = []
        parim = [[[]]]
        vahed = []
        for k in range(0 + jarg, 20):
            for j in range(0, 50):
                puder.append(j)
                puder.append(k)
                if puder not in vabadKohad:
                    if (k - jarg == 0):
                        vaba.append("-")
                    del puder[0]
                    del puder[0]
                if puder in vabadKohad:
                    if (k - jarg == 0):
                        vaba.append("+")
                    del puder[0]
                    del puder[0]
                if (j == 49) and (k - jarg == 0):
                    for t in range(0, len(vaba)):
                        if vaba[t] == "-":
                            if (t >= 1) and (vaba[t - 1] == "+"):
                                parim.append([[]])
                            if t < len(vaba) - 1:
                                if vaba[t + 1] == "+":
                                    muutuja = parim[-1][0]
                                    parim[-1][0].append(t + 1)
                                    parim[-1][0].append(k)
                                    parim[-1].append(0)
                        if vaba[t] == "+" and t == 0:
                            parim[-1][0].append(t)
                            parim[-1][0].append(k)
                            parim[-1].append(0)
                        if vaba[t] == "+":
                            parim[-1][-1] += 1
                    if parim[-1] == [[]]:
                        del parim[-1]
                    x = 0
                    vahe = 0
                    kontroll = False
                    lugeja = 0
                    while kontroll != True:
                        muutuja = (randint(0, len(parim) - 1))
                        if (vahe <= parim[muutuja][-1]):
                            if (parim[muutuja][-1] > x):
                                if (i[0]<=parim[muutuja][-1]):
                                    x = parim[muutuja][0][0]
                                    vahe = parim[muutuja][-1]
                                    kontroll = True
                                if lugeja ==10:
                                    break
                            lugeja += 1
                    if x == 0 and vahe == 0:
                        valjund[jarg].append("!")
                        return valjund
                    if x + i[0] > 50:
                        valjund[jarg].append("!")
                        return valjund
                if (j == 49) and (korgus < i[1]):
                    for a in range(0, veerud):
                        valjund[jarg].append([])  # lisame esimese koordinaadi
                        valjund[jarg][kast].append([])
                        valjund[jarg][kast][0].append(x + a)  # lisame x0
                        valjund[jarg][kast][0].append(k)  # lisame y0
                        valjund[jarg][kast].append([])  # lisame teise koordinaadi
                        valjund[jarg][kast][1].append(x + a + 1)  # lisame x1
                        valjund[jarg][kast][1].append(k + 1)  # lisame y2
                        if valjund[jarg][kast][0] in vabadKohad:
                            vabadKohad.remove(valjund[jarg][kast][0])
                        kast += 1
                    korgus += 1
                    break
    return (valjund)


def massiiviks(input_jarjend):
    valjund = []
    jupid = input_jarjend.split(";")
    for i in range(len(jupid)):
        hakkliha = jupid[i].split(",")
        saabumine = int(hakkliha[0])
        kestus = int(hakkliha[1])
        valjund.append([saabumine, kestus])
    return valjund


# otsustab, millist järjendit teha kahetasemeliseks massiiviks
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

def massiiviTeavitaja(massiiv):
    text.delete(1.0, END)
    for jupp in massiiv:
        text.insert(INSERT, str(jupp) + "\n")


def kasuvalija(jarjend, algoritm):
    if algoritm == "First-Fit":
        return First(jarjend)
    elif algoritm == "Best-Fit":
        return Best(jarjend)
    elif algoritm == "Worst-Fit":
        return Worst(jarjend)
    elif algoritm == "Random-Fit":
       return Random(jarjend)


def jooksuta_algoritmi(algoritm):
    jarjend = massiiviMeister()
    jarjend2 = jarjend[:]
    massiiviTeavitaja(jarjend)
    valjund = kasuvalija(jarjend, algoritm)
    joonista(valjund, jarjend2)
    #keskm_oot = tahvel.create_text(80, 40, text="Keskmine ooteaeg:  " + str(ooteaeg))


predef1 = "4,5;2,7;9,2;4,6;7,1;6,4;8,8;3,6;1,10;9,2"
predef2 = "1,10;6,6;3,9;2,4;1,6;5,2;1,4;5,2;2,1;2,7"
predef3 = "5,10;6,6;3,9;8,4;3,6;5,12;1,4;15,3;3,4;9,7"

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

silt_vali = ttk.Label(raam, text="Vali või sisesta järjend (kujul 3,5;2,7;8,2;4,6;7,1;6,4;8,8;3,6;1,10;9,2)")
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

Best_nupp = ttk.Button(raam, text="Best-Fit", command=lambda: jooksuta_algoritmi("Best-Fit"))
Best_nupp.place(x=100, y=190, height=25, width=80)

Worst_nupp = ttk.Button(raam, text="Worst-Fit", command=lambda: jooksuta_algoritmi("Worst-Fit"))
Worst_nupp.place(x=190, y=190, height=25, width=80)

Random_nupp = ttk.Button(raam, text="Random-Fit", command=lambda: jooksuta_algoritmi("Random-Fit"))
Random_nupp.place(x=280, y=190, height=25, width=80)

First_nupp = ttk.Button(raam, text="First-Fit", command=lambda: jooksuta_algoritmi("First-Fit"))
First_nupp.place(x=10, y=190, height=25, width=80)

puhasta_nupp = ttk.Button(raam, text="Puhasta väljund", command=lambda: puhasta())
puhasta_nupp.place(x=460, y=190, height=25, width=80)

text = Text(raam, width=25, height=9)
text.place(x=450, y=30)

raam.mainloop()