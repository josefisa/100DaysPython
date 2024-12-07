#Programa para Taller Piloto
#Esteban DeFelipe Diaz   C.C. 1 013 259 005
#José Emanuel Figueroa   C.C. 1 121 953 225
#Cesar Augusto Gonzalez  C.C. 1 000 219 893

import random
from math import sqrt

print("Parcial Programación Grupo2. tema 2.\n")
print("""Participantes: 
        Esteban DeFelipe Diaz - edefelipe
        José Emanuel Figueroa - jfigueroas
        Cesar Augusto Gonzalez  - cesgonzalezbe\n""")

print(" *** Ejecución Inicializada *** \n")

#Calculo de vertices de puntos en el circulo
PuntoAx = 4.59; PuntoAy= 1.99; PuntoDx = 3; PuntoDy = -4; PuntoCx = -4; PuntoCy = -3; PuntoBx = -2.45; PuntoBy = 4.36
PuntoGx = 4.062; PuntoGy = 0; PuntoFx=0; PuntoFy=-3.571; PuntoEx = -3.368; PuntoEy = 0; PuntoHx=0; PuntoHy=3.535

#Cálculo de pendientes puntos principales
mCD = (PuntoCy-PuntoDy)/(PuntoCx-PuntoDx); bCD = PuntoDy - mCD*PuntoDx #Pendiente entre los puntos C y D
mAD = (PuntoAy-PuntoDy)/(PuntoAx-PuntoDx); bAD = PuntoAy - mAD*PuntoAx #Pendiente entre los puntos A y D
mAB = (PuntoAy-PuntoBy)/(PuntoAx-PuntoBx); bAB = PuntoBy - mAB*PuntoBx #Pendiente entre los puntos A y B
mCB = (PuntoCy-PuntoBy)/(PuntoCx-PuntoBx); bCB = PuntoCy - mCB*PuntoCx #Pendiente entre los puntos C y B

#Cáculo de pendientes puntos rectas internas
mFE = (PuntoFy-PuntoEy)/(PuntoFx-PuntoEx); bFE = PuntoFy - mFE*PuntoFx #Pendiente entre los puntos C y D
mEH = (PuntoEy-PuntoHy)/(PuntoEx-PuntoHx); bEH = PuntoEy - mEH*PuntoEx #Pendiente entre los puntos A y D
mHG = (PuntoHy-PuntoGy)/(PuntoHx-PuntoGx); bHG = PuntoHy - mHG*PuntoHx #Pendiente entre los puntos A y B
mHF = (PuntoGy-PuntoFy)/(PuntoGx-PuntoFx); bHF = PuntoHy - mHF*PuntoHx #Pendiente entre los puntos C y B

print("x")
def pitagoras(x,y):
    hipotenusa = sqrt((x**2)+(y**2))
    return hipotenusa

def pendiente(x,y):
    pen = ()

print("x")
Longitud = random.randint(350,950)

YL =[]; XL=[]; Reg = [0,0,0,0,0,0]
for i in range(0,Longitud):
    YL.append((random.randint(-775,775))*0.01)
    XL.append((random.randint(-775,775))*0.01)
    
print("..El numero de puntos (N): ",(len(YL)+1))  
    
for i in range(len(YL)):
    x = XL[i]; y = YL[i]
    
    CorteEH = y-(mEH*x)
    CorteCB = y-(mCB*x)
    CorteAB = y-(mAB*x)
    
    CorteFE = y-(mFE*x)
    CorteCD = y-(mCD*x)
    CorteCB = y-(mCB*x)
    
    if(x==0) or ((pitagoras(x,y))==5) or (y==0) or (CorteEH==bEH):
        Reg[0]+=1
    elif(x>0 or pitagoras(x,y)<5):
        Reg[5]+=1
    
    if(y>0):
        if(CorteEH<bEH):
            Reg[1] +=1
        elif(CorteCB>bCB):
            Reg[3]+=1
        elif(CorteAB>bAB):
            Reg[4]+=1
        else:
            Reg[2]+=1
    else:
        if(CorteFE>bFE):
            Reg[1] +=1
        elif(CorteCB>bCB):
            Reg[3]+=1
        elif(CorteCD<bCD):
            Reg[4]+=1
        else:
            Reg[2]+=1

print("..La cantidad de puntos por region es de:\n","Región 0: ",Reg[0],"\n Región 1: ",Reg[1],"\n Región 2: ",Reg[2],"\n Región 3: ",Reg[3],"\n Región 4: ",Reg[4],"\n Región 5: ",Reg[5])
print(" ****Ejecución Finalizada***\n")