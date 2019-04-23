#!/usr/bin/env python3
# vim: set fileencoding=utf8 :
# Näiteprogramm protsessoriaja planeerijate visualiseerimiseks

from tkinter import *
import tkinter
from tkinter import ttk
from tkinter import messagebox


def puhasta():
    tahvel.delete('all')


# joonistab tahvlile protsesse kujutavad ristkülikud numbrite ja protsesside nimedega
def joonista(jarjend):
    puhasta()
    eelmise_loppx = 20
    kaugus = 0
    list2 = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9', 'P10', ' ']
    värvid = [["blue"], ["green"], ["yellow"], ["red"], ["pink"], ["orange"], ["plum"], ["cyan"], ["purple"], ["gray"],
              ["black"]]
    fill = värvid[0]
    for i in range(len(jarjend)):
        protsess = jarjend[i][0]
        kestus = jarjend[i][1]
        kujund = tahvel.create_rectangle(eelmise_loppx, 60, eelmise_loppx + kestus * 16, 100,
                                         fill=värvid[list2.index(protsess)])
        keskpaik = eelmise_loppx + kestus * 8
        protsessi_id = tahvel.create_text(keskpaik, 80, text=protsess)
        m = tahvel.create_text(eelmise_loppx, 110, text=str(kaugus))
        kaugus += kestus
        eelmise_loppx += kestus * 16
    m = tahvel.create_text(eelmise_loppx, 110, text=str(kaugus))


# teeb järjendist kahetasemelise listi, mida on mugavam töödelda
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


def FCFS(jarjend):
    valjund = [] #loome listi
    counter = 1 #loome muutuja
    jarg = 0 #loome muutuja
    kogu_ooteaeg = 0 #loome muutuja
    for p in sorted(jarjend, reverse=False): #vaatame igat elementi jarjendis
        saabumine = p[0] #omistame muutujale elemendi saabumis aja
        kestus = p[1] #omistame muutujale elemendi kestvusaja
        if saabumine > (jarg): #kui saabumine on suurem, kui jarg
            valjund.append([" ", saabumine - jarg]) #lisame valjundisse tühja elemendi nii pikalt kuni jargmien element
            valjund.append(["P" + str(counter), kestus]) #lisame elemendi jarjendisse
            jarg = saabumine + kestus #suurendame jarge
            counter += 1 #suurendame muutujate
        else: #kui saabumine on võrdne voi vaiksem, kui jarg
            if saabumine < jarg: #kui saabumine on väiksem kui jarg siis...
                kogu_ooteaeg += jarg - saabumine #suurendaem ooteaega
            valjund.append(["P" + str(counter), kestus]) #lisaem valjundisse elemendi
            jarg += kestus #suurendaem jarge
            counter += 1 #suurendame muutujat
    keskm_ooteaeg = round(kogu_ooteaeg / len(jarjend), 2) #omistaem muutujale keskmise ooteaja
    return (valjund, keskm_ooteaeg) #tagastaem jarjendi ja ooteaja


def sorteeri(puder):
    for i in range(len(puder) - 1):

        if puder[i][1] > puder[i + 1][1]:
            muutuja2 = puder[i]
            puder[i] = puder[i + 1]
            puder[i + 1] = muutuja2
    return puder


def SJF(jarjend):
    valjund = []
    puder = []
    jarg = 0
    ooteaeg = 0

    mitmes = 0
    for i in range(len(jarjend)): #lisan koigile jarndis olevatele elementidele numbri juurde
        jarjend[i].append(mitmes + 1)
        mitmes += 1

    esimene_saabub = jarjend[0][0]
    esimene_kestvus = jarjend[0][1]
    jarg += esimene_kestvus #suurendan järge nii palju kui esimene kestis
    if esimene_saabub > 0: #kui esimene saabunu tuleb hiljem, kui 0 siis täidame ruumi niikaua tühjusega
        valjund.append([" ", jarjend[0][0]]) #lisan tühja osa nii pikalt kuni esimene element saabub
        jarg += esimene_saabub

    valjund.append(["P" + str(jarjend[0][2]), jarjend[0][1]]) #lisan jarjendisse esimese elemendi

    jarjend2 = [] #loome uue jarjendi
    for i in jarjend: #ja lisame siia koik jarjendi elemendid
        jarjend2.append(i)
    del jarjend2[0]

    while len(jarjend2) != 0: #teeme tüskli nii kaua kuni jarjend pole tühi
        for i in jarjend2: #vaatame igat elementi jarjendis
            if i[0] <= jarg: #kui elemendi sissetulemise aeg on väiksem, kui jarjend siis...
                puder.append([i[0], i[1], i[2]])  #...lisame pudru jarjendisse selle elemendi
        for i in puder: #vaatame igat elementi pudrus
            if i in jarjend2: #kui pudru element on jarjend2's siis...
                jarjend2.remove(i) #... kustutame ta jarjendist
        if len(puder) != 0: #kui pudru jarjend ei ole tühi
            puder = sorteeri(puder) #sorteerime pudru jarjendis olevad elemendid
            valjund.append(["P" + str(puder[0][2]), puder[0][1]]) #lisame valjundi jarjendisse elemendi
            ooteaeg += jarg - puder[0][0] #suurendame ootaaeg nii palju, kui antud jarjend pidi ootama
            jarg += puder[0][1] #suurendame jarjendit nii palju kui kaua jarjend tööd tegi
            puder.remove(puder[0]) #kustutame pudru jarjendist just käsitletud elemendi
        else: #kui pudru jarjend on tühi...
            valjund.append([" ", jarjend2[0][0] - jarg])  #lisame valjundisse tühja osa nii pikalt kuni uus element saabub
            jarg += jarjend2[0][0] - jarg #suurendame jarge jälle
    for i in range(len(puder)): #läbime tsüklit nii pikalt, kui pikk on pudru jarjend
        if len(puder) == 0: #kui pudru jarjendi pikkus on 0
            valjund.append([" ", jarjend2[0][0] - jarg]) #lisame tühja osa nii palju kui tuleb uus element
            jarg += jarjend2[0][0] - jarg #suurendame jarjendit
        else: #kui pudru jarjendi pikkus ei ole 0
            valjund.append(["P" + str(puder[0][2]), puder[0][1]]) #lisame valjundisse elemndi
        ooteaeg += jarg - puder[0][0] #suurendame ooteaega
        jarg += puder[0][1] #suurendame jarjendit
        puder.remove(puder[0]) #eemaldale pudru listist elemendi

    keskmine_ooteaeg = (ooteaeg) / (len(jarjend)) #omistame muutujale keskmise ooteaja
    return (valjund, keskmine_ooteaeg) #tagastame jarjendi ja ooteaja


def STRF(jarjend):
    return (valjund, keskmine_ooteaeg)


def RR(jarjend):
    rütm = 3  #ette antud rütm on 3
    valjund = [] #loome listi
    järjekord = [] #loome listi
    järg = 0 #loome muutuja
    jarjend2 = jarjend
    a = len(jarjend) #anname muutujale a väätuseks jarjendi pikkuse
    ooteaeg = 0 #loome ooteaja

    mitmes = 0
    for i in range(len(jarjend2)): #labime tsüklit nii kaua kuni jarjendil on pikkust
        jarjend2[i].append(mitmes + 1) #lisame jarjendi elemndis olevale elemendile jarjekonnanumbri
        mitmes += 1
    if jarjend[0][0] > 0: #kui esimene element jarjendis on suurem, kui 0
        valjund.append([" ", jarjend[0][0]]) #lisame vlajundi listi tühja elemeni nii pikalt kuni tuleb jargmine element
        järg += jarjend[0][0] #suurendame jarge

    esimene_kestvus = jarjend2[0][1]
    if esimene_kestvus <= 3:#kui esimese elemendi kestvus on alla kolme...
        valjund.append(["P" + str(jarjend2[0][2]), jarjend2[0][1]]) #lisame elemendi valjundi listi
        järg += jarjend2[0][1] #suurendame jarge
        del jarjend2[0] #kustutame jarjendi listist elemendi
    else:
        valjund.append(["P" + str(jarjend2[0][2]), 3]) #lisame valjundi listi elemendi
        järjekord.append([jarjend2[0][0]+3, (jarjend2[0][1]) - 3, jarjend2[0][2]]) #kuna element on pikem kui 3, siis lisame ta jarjekorda
        del jarjend2[0] #kustutame elemendi jarjendist
        järg += 3 #suurendame jarge kolme võraa

    while len(jarjend2) != 0: #teeme tsükli nii kaua kuni jarjendis on elemente
        saabus = jarjend2[0][0]
        kestvus = jarjend2[0][1]
        if saabus <= järg: #kui saamuvise aeg on väiksem, kui jarjendi arv
            if kestvus <= 3: #kui töö  on alla kolme
                valjund.append(["P" + str(jarjend2[0][2]), jarjend2[0][1]])
                if len(järjekord)  != 0 or len(jarjend2) - 1 != 0:
                    ooteaeg += järg - jarjend2[0][0]
                järg += jarjend2[0][1]
                del jarjend2[0]

            else: #kui üle kolme, siis teeme jargnevat:
                valjund.append(["P" + str(jarjend2[0][2]), 3])
                järjekord.append([jarjend2[0][0] + 3, (jarjend2[0][1]) - 3, jarjend2[0][2]])
                if len(järjekord) != 0 or len(jarjend2) - 1 != 0:
                    ooteaeg += järg - jarjend2[0][0]
                del jarjend2[0]
                järg += 3
        else: #kui töö kestvus on suurem kui 3 siis...
            if len(järjekord) != 0: #kui jarjendi pikkus ei ole 0
                if järjekord[0][1] <= 3: #kui elemendi pikkus on alla kolme
                    valjund.append(["P" + str(järjekord[0][2]), järjekord[0][1]]) #
                    if len(järjekord) - 1 != 0 or len(jarjend2) != 0: #kontrollie, kas tegemist viimase elemendiga. Kui viimane elemnt sisi ei lsia enam ooteaega.
                        ooteaeg += järg - järjekord[0][0] - 3
                    järg += järjekord[0][1]
                    del järjekord[0]

                else: #kui elemendi tööpikkus suurem kui 3....
                    valjund.append(["P" + str(järjekord[0][2]), 3])
                    järjekord.append([järjekord[0][0] + 3, (järjekord[0][1]) - 3, järjekord[0][2]])
                    if len(järjekord) - 1 != 0 or len(jarjend2) != 0:
                        ooteaeg += järg - järjekord[0][0]
                    järg += 3
                    del järjekord[0]
            else: #kui jarjend on tühi, siis lisame tühja osa
                valjund.append([" ", jarjend2[0][0] - järg])
                järg += jarjend2[0][0] - järg
    while len(järjekord) != 0: #teeme tsklit nii kaua kuni jarjekorras on elemente
        if len(järjekord) != 0: #kui jarjekord ei ole tuhi
            if järjekord[0][1] <= 3: #ja elemendi töökestvus on alla kolme...
                valjund.append(["P" + str(järjekord[0][2]), järjekord[0][1]]) #lisame elemendi valjundisse
                järg += järjekord[0][1] #suurendaem jarge
                ooteaeg += järg - järjekord[0][0] #suurendaem ooteaega kui vaja
                del järjekord[0] #kustutame elemendi jarjekorrast
            else: #kui pikem, kui 3...
                valjund.append(["P" + str(järjekord[0][2]), 3])
                järjekord.append([järjekord[0][0] + 3, (järjekord[0][1]) - 3, järjekord[0][2]])
                ooteaeg += järg - järjekord[0][0]
                del järjekord[0]
                järg += 3
        else: #kui jarjekord on tühi....
            valjund.append([" ", jarjend2[0][0] - järg])
            järg += jarjend2[0][0] - järg

    keskmine_ooteaeg = (ooteaeg) / (a) #omistame muutujale keskmise ooteaja
    return (valjund, keskmine_ooteaeg) #tagastaem ooteaja ja jarejndi


def massiiviTeavitaja(massiiv):
    text.delete(1.0, END)
    for jupp in massiiv:
        text.insert(INSERT, str(jupp) + "\n")


def kasuvalija(jarjend, algoritm):
    if algoritm == "SJF":
        return SJF(jarjend)
    elif algoritm == "SRTF":
        return SRTF(jarjend)
    elif algoritm == "RR":
        return RR(jarjend)
    elif algoritm == "FCFS":
        return FCFS(jarjend)


def jooksuta_algoritmi(algoritm):
    jarjend = massiiviMeister()
    massiiviTeavitaja(jarjend)
    (valjund, ooteaeg) = kasuvalija(jarjend, algoritm)
    joonista(valjund)
    keskm_oot = tahvel.create_text(80, 40, text="Keskmine ooteaeg:  " + str(ooteaeg))


predef1 = "0,5;6,9;6,5;15,10"
predef2 = "0,2;0,4;12,4;15,5;21,10"
predef3 = "5,6;6,9;11,3;12,7"

# GUI
raam = Tk()
raam.title("Planeerimisalgoritmid")
raam.resizable(False, False)
raam.geometry("800x400")

var = IntVar()
var.set(1)
Radiobutton(raam, text="Esimene", variable=var, value=1).place(x=10, y=40)
Radiobutton(raam, text="Teine", variable=var, value=2).place(x=10, y=70)
Radiobutton(raam, text="Kolmas", variable=var, value=3).place(x=10, y=100)
Radiobutton(raam, text="Enda oma", variable=var, value=4).place(x=10, y=130)

silt_vali = ttk.Label(raam, text="Vali või sisesta järjend (kujul 1,10;4,2;12,3;13,2)")
silt_vali.place(x=10, y=10)

silt1 = ttk.Label(raam, text=predef1)
silt1.place(x=120, y=40)

silt2 = ttk.Label(raam, text=predef2)
silt2.place(x=120, y=70)

silt3 = ttk.Label(raam, text=predef3)
silt3.place(x=120, y=100)

silt_run = ttk.Label(raam, text="Algoritmi käivitamiseks klõpsa nupule")
silt_run.place(x=10, y=160)

silt_tahvel = ttk.Label(raam, text="Käsil olevad protsessid:")
silt_tahvel.place(x=450, y=10)

kasutaja_jarjend = ttk.Entry(raam)
kasutaja_jarjend.place(x=120, y=130, height=25, width=240)

tahvel = Canvas(raam, width=800, height=180, background="white")
tahvel.place(x=0, y=220)

# LIFO_nupp = ttk.Button(raam, text="LIFO", command = lambda : jooksuta_algoritmi("LIFO"))
# LIFO_nupp.place(x=10, y=190,height=25, width=80)

SJF_nupp = ttk.Button(raam, text="SJF", command=lambda: jooksuta_algoritmi("SJF"))
SJF_nupp.place(x=100, y=190, height=25, width=80)

SRTF_nupp = ttk.Button(raam, text="SRTF", state=DISABLED, command=lambda: jooksuta_algoritmi("SRTF"))
SRTF_nupp.place(x=190, y=190, height=25, width=80)

RR_nupp = ttk.Button(raam, text="RR", command=lambda: jooksuta_algoritmi("RR"))
RR_nupp.place(x=280, y=190, height=25, width=80)

FCFS_nupp = ttk.Button(raam, text="FCFS", command=lambda: jooksuta_algoritmi("FCFS"))
FCFS_nupp.place(x=10, y=190, height=25, width=80)

puhasta_nupp = ttk.Button(raam, text="Puhasta väljund", command=lambda: puhasta())
puhasta_nupp.place(x=460, y=190, height=25, width=80)

text = Text(raam, width=25, height=9)
text.place(x=450, y=30)

raam.mainloop()