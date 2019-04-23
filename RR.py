def RR(jarjend):
    rütm = 3
    valjund = []
    järjekord = []
    järg = 0
    jarjend2 = jarjend
    a = len(jarjend)
    ooteaeg = 0
    
    mitmes = 0
    for i in range(len(jarjend2)):
        jarjend2[i].append(mitmes+1)
        mitmes += 1
    if jarjend[0][0] > 0:
        valjund.append([" ", jarjend[0][0]])
        järg += jarjend[0][0]
        
    esimene_kestvus = jarjend2[0][1]
    if esimene_kestvus <= 3:
        valjund.append(["P" + str(jarjend2[0][2]), jarjend2[0][1]])
        järg += jarjend2[0][1]
        del jarjend2[0]
    else:
        valjund.append(["P" + str(jarjend2[0][2]), 3])
        järjekord.append([jarjend2[0][0],(jarjend2[0][1])-3,jarjend2[0][2]])
        del jarjend2[0]
        järg += 3
                       
    while len(jarjend2) != 0:  
        saabus = jarjend2[0][0]
        kestvus = jarjend2[0][1]
        if saabus <= järg: 
            if kestvus <= 3:
                valjund.append(["P" + str(jarjend2[0][2]), jarjend2[0][1]])
                ooteaeg += järg - jarjend2[0][0]
                järg += jarjend2[0][2]
                del jarjend2[0]
                
            else:
                valjund.append(["P" + str(jarjend2[0][2]), 3])
                järjekord.append([jarjend2[0][0],(jarjend2[0][1])-3,jarjend2[0][2]])
                ooteaeg += järg - jarjend2[0][0]
                del jarjend2[0]
                järg += 3
        else:
            if len(järjekord) != 0:
                if järjekord[0][1] <= 3:
                    valjund.append(["P" + str(järjekord[0][2]), järjekord[0][1]])
                    järg += järjekord[0][1]
                    ooteaeg += järg - järjekord[0][0]
                    del järjekord[0]
                    
                else:
                    valjund.append(["P" + str(järjekord[0][2]), 3])
                    järjekord.append([järjekord[0][0],(järjekord[0][1])-3,järjekord[0][2]])
                    ooteaeg += järg - järjekord[0][0]
                    del järjekord[0]
                    järg += 3
            else:
                valjund.append([" ", jarjend2[0][0] - järg])
                järg += jarjend2[0][0] - järg


    if len(järjekord) != 0:
        if järjekord[0][1] <= 3:
            valjund.append(["P" + str(järjekord[0][2]), järjekord[0][1]])
            järg += järjekord[0][1]
            ooteaeg += järg - järjekord[0][0]
            del järjekord[0]
        else:
            valjund.append(["P" + str(järjekord[0][2]), 3])
            järjekord.append([järjekord[0][0],(järjekord[0][1])-3,järjekord[0][2]])
            ooteaeg += järg - järjekord[0][0]
            del järjekord[0]
            järg += 3
    #else:
        #    valjund.append([" ", jarjend2[0][0] - järg])
         #   järg += jarjend2[0][0] - järg

    keskmine_ooteaeg = (ooteaeg) / (a)
    return print(valjund,keskmine_ooteaeg)
            
jarjend = [[0, 7], [2, 4], [4, 1], [5, 4]]
jarjend2 = [[0, 5], [6, 9], [6, 5], [15, 10]]
jarjend3 = [[0, 2],[0, 4], [12, 4], [15, 5],[21, 10]]
jarjend4 = [[1, 8],[3, 5],[4, 3],[12 ,1],[19, 1]]
RR(jarjend4)