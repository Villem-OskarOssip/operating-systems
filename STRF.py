def STRF(jarjend):
    valjund = []
    jarg = 0
    jarg1=0
    kogu_ooteaeg = 0
    counter=1
    saabunud_programmid=[]
    programmide_järjekord=[]
    tühi_pikkus=0
    abiList=[]
    programmi_nr=1
    kogu_ooteajast_maha_lahutatav=0

    for p in sorted(jarjend):
        saabumine = p[0]
        kestus = p[1]
        
        if saabumine > jarg:
            jarg = saabumine + kestus
        else:
            jarg+=kestus
            
    for element in jarjend:
        element.append("P"+str(counter))
        element.append(0)
        counter+=1

    
    for i in range(jarg+1):
        
        for d in jarjend:
            if d[0]<=i:
                if saabunud_programmid.count(d)==0 and abiList.count(d)==0:
                    saabunud_programmid.append(d)
                    abiList.append(d)
        
        try:
            if valjund.index([" ",tühi_pikkus])!=len(valjund)-1: 
                tühi_pikkus=0
        except:
            pass
        
        if len(saabunud_programmid)!=0:
            
            if saabunud_programmid[0][1]!=0:
                saabunud_programmid = sorted(saabunud_programmid,key=itemgetter(1))
                juba_tehtud_protsessi=0
                
                if valjund.count([saabunud_programmid[0][2],saabunud_programmid[0][3]])!=0 and valjund.index([saabunud_programmid[0][2],saabunud_programmid[0][3]])==len(valjund)-1:
                    valjund.remove([saabunud_programmid[0][2],saabunud_programmid[0][3]])
                valjund.append([saabunud_programmid[0][2],((saabunud_programmid[0][3])+1)])
        
                saabunud_programmid[0][3]+=1
                saabunud_programmid[0][1]-=1
            else:
                
                saabunud_programmid.pop(0)
                saabunud_programmid = sorted(saabunud_programmid,key=itemgetter(1))
                if len(saabunud_programmid)!=0:
                    if valjund.count([saabunud_programmid[0][2],saabunud_programmid[0][3]])!=0 and valjund.index([saabunud_programmid[0][2],saabunud_programmid[0][3]])==len(valjund)-1:
                        valjund.remove([saabunud_programmid[0][2],saabunud_programmid[0][3]])
                    valjund.append([saabunud_programmid[0][2],(saabunud_programmid[0][3])+1])
                    
                    saabunud_programmid[0][3]+=1
                    saabunud_programmid[0][1]-=1
                if len(saabunud_programmid)==0 and i!=jarg:
                    
                    tühi_pikkus+=1
                    valjund.append([" ",tühi_pikkus])
                    
        else:
           
            if(valjund.count([" ",tühi_pikkus]))!=0 and valjund.index([" ",tühi_pikkus])==len(valjund)-1:
                valjund.remove([" ",tühi_pikkus])
            tühi_pikkus+=1
            valjund.append([" ",tühi_pikkus])

    for pr in range(len(jarjend)):
        programm="P"+str(programmi_nr)
        aega_programmile_kulunud=0
        for v in valjund:
            if v[0]==programm:
                kogu_ooteajast_maha_lahutatav-=aega_programmile_kulunud
                programmi_uus_aeg=v[1]-aega_programmile_kulunud
                aega_programmile_kulunud+=v[1]
                v[1]=programmi_uus_aeg
                
        programmi_nr+=1

    for g in valjund:
        for m in range(len(jarjend)):
            if jarjend[m][2]==g[0]:
                kogu_ooteaeg+=jarg1-jarjend[m][0]
                jarg1+=g[1]
        if(g[0]==" "):
            
            jarg1+=g[1]

    kogu_ooteaeg+=kogu_ooteajast_maha_lahutatav
    keskm_ooteaeg=round(kogu_ooteaeg/(counter-1),2)
    

jarjend = [[0, 7], [2, 4], [4, 1], [5, 4]]
jarjend2 = [[0, 5], [6, 9], [6, 5], [15, 10]]
jarjend3 = [[0, 2],[0, 4], [12, 4], [15, 5],[21, 10]]
jarjend4 = [[1, 8],[3, 5],[4, 3],[12 ,1],[19, 1]]
STRF(jarjend4)