def sorteeri(puder):
    for i in range(len(puder) - 1):
        for j in range(len(puder) - 1):
            if puder[i][1] > puder[j + 1][1]:
                muutuja2 = puder[i]
                puder[i] = puder[j + 1]
                puder[j + 1] = muutuja2
    return puder


def lisaja(puder, valjund, counter, jarg2, jarjend2, saabumine2, kestvus2, a, sügavus):
    counter2 = 0
    for i in range(a - sügavus):
        saabus = puder[i][0]
        aeg = puder[i][1]
        counter3 = puder[i][2]
        valjund.append(["P" + str(counter3), aeg])
        del (puder[0])
        counter2 += 1
        jarg2 += aeg
        for j in jarjend2:
            if j[0] <= jarg2:
                puder.append([saabumine2, kestvus2, counter])
                counter += 1
                puder = sorteeri(puder)
                del (jarjend2[0])
                sügavus += 1
                return lisaja(puder, valjund, counter, jarg2, jarjend2, saabumine2, kestvus2, a, sügavus)
    return print(valjund)


def SJF(jarjend):
    valjund = []
    puder = []
    jarg = 0
    ooteaeg = 0

    mitmes = 0
    for i in range(len(jarjend)):
        jarjend[i].append(mitmes + 1)
        mitmes += 1

    esimene_saabub = jarjend[0][0]
    esimene_kestvus = jarjend[0][1]
    jarg += esimene_kestvus
    if esimene_saabub > 0:
        valjund.append([" ", jarjend[0][0]])
        ooteaeg += jarjend[0][0]
        jarg += jarjend[0][0]

    valjund.append(["P" + str(jarjend[0][2]), jarjend[0][1]])
    
    jarjend2 = []
    for i in jarjend:
        jarjend2.append(i)
    del jarjend2[0]

    while len(jarjend2) != 0:
        for i in jarjend2:
            if i[0] <= jarg:
                puder.append([i[0], i[1], i[2]])
        for i in puder:
            if i in jarjend2:
                jarjend2.remove(i)
        if len(puder) != 0:
            puder = sorteeri(puder)
            valjund.append(["P" + str(puder[0][2]), puder[0][1]])
            ooteaeg += jarg - puder[0][0]
            jarg += puder[0][1]
            puder.remove(puder[0])
        else:
            valjund.append([" ", jarjend2[0][0] - jarg])
            jarg += jarjend2[0][0] - jarg
            ooteaeg += jarjend2[0][0] -jarg
    for i in range(len(puder)):
        if len(puder) == 0:
            valjund.append([" ", jarjend2[0][0] - jarg])
            jarg += jarjend2[0][0] - jarg
            
        else:
            valjund.append(["P" + str(puder[0][2]), puder[0][1]])
        ooteaeg += jarg - puder[0][0]
        jarg += puder[0][1]
        puder.remove(puder[0])
        
    keskmine_ooteaeg = (ooteaeg)/(len(jarjend))
    return print(valjund, keskmine_ooteaeg)
    # keskm_ooteaeg = 0
    # return (valjund, keskm_ooteaeg)


jarjend = [[0, 7], [2, 4], [4, 1], [5, 4]]
jarjend2 = [[0, 5], [6, 9], [6, 5], [15, 10]]
jarjend3 = [[0, 2],[0, 4], [12, 4], [15, 5],[21, 10]]
jarjend4 = [[1, 8],[3, 5],[4, 3],[12 ,1],[19, 1]]
SJF(jarjend4)