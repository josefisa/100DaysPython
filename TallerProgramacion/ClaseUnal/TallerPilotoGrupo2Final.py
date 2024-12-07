#Programa para Taller Piloto

import math

print("Taller Piloto - Cuadrante 4 (X positivo Y negativo)"); print()
print("""Participantes: 
        Esteban DeFelipe Diaz - edefelipe
        José Emanuel Figueroa - jfigueroas
        Cesar Augusto Gonzalez  - cesgonzalezbe"""); print()

print(" *** Ejecución Inicializada *** "); print()
# Inicio de calculo de area
RadioCir = 5.0
AreaCir = math.pi*(RadioCir*RadioCir)
AreaCirCua = AreaCir/4
#print("Area de Cuadrante en ese circulo = "); print(AreaCirCua)

#Calculo de vertices de TrianguloVerde
PuntoAx = 4.59; PuntoAy= 1.99; PuntoDx = 3; PuntoDy = -4; PuntoCx = -4; PuntoCy = -3

mCD = (PuntoCy-PuntoDy)/(PuntoCx-PuntoDx) #Pendiente entre los puntos C y D
#print("Pendiente entre CD = "); #print(mCD)
IntersectoY = -(PuntoDx*mCD) + (PuntoDy);# print(IntersectoY) #Ecuacion de la recta
PuntoGx =0; PuntoGy=IntersectoY
#print(" B ");print(IntersectoY)

mAD = (PuntoAy-PuntoDy)/(PuntoAx-PuntoDx) #Pendiente entre los puntos A y D
#print("Pendiente entre AD = "); #print(mAD)
IntersectoY = -(PuntoDx*mAD) + (PuntoDy); # print(IntersectoY) #Ecuacion de la recta
IntersectoX = -IntersectoY/mAD; #print(IntersectoX)
PuntoFy =0; PuntoFx=IntersectoX

#Calculo del area de la forma 2
DisFD = math.sqrt( ((PuntoFy-PuntoDy)*(PuntoFy-PuntoDy)) + ((PuntoFx-PuntoDx)*(PuntoFx-PuntoDx)) )
#print(DisFD)

DisGD = math.sqrt( ((PuntoGy-PuntoDy)*(PuntoGy-PuntoDy)) + ((PuntoGx-PuntoDx)*(PuntoGx-PuntoDx)) )
#print(DisGD)

DisGF = math.sqrt( ((PuntoGy-PuntoFy)*(PuntoGy-PuntoFy)) + ((PuntoGx-PuntoFx)*(PuntoGx-PuntoFx)) )
#print(DisGF)

#Formula de Herón.

S = (DisGF +DisFD +DisGD)/2 #Semiperimetro
AreaTri = math.sqrt ( S*(S-DisGF)*(S-DisFD)*(S-DisGD))
print("El area del triangulo 2 en cuadrante 4= ");print(AreaTri); print()

#Calculo del Area de la forma 4.

#Area de Triangulo 
PuntoCx = 0; PuntoCy = 0; 
 
DisCD = math.sqrt( ((PuntoCy-PuntoDy)*(PuntoCy-PuntoDy)) + ((PuntoCx-PuntoDx)*(PuntoCx-PuntoDx)) )
#print(DisCD)

DisGD = math.sqrt( ((PuntoGy-PuntoDy)*(PuntoGy-PuntoDy)) + ((PuntoGx-PuntoDx)*(PuntoGx-PuntoDx)) )
#print(DisGD)

DisGC = math.sqrt( ((PuntoGy-PuntoCy)*(PuntoGy-PuntoCy)) + ((PuntoGx-PuntoCx)*(PuntoGx-PuntoCx)) )
#print(DisGC)

#Formula de Herón.

S = (DisGC +DisCD +DisGD)/2 #Semiperimetro
AreaTri = math.sqrt ( S*(S-DisGC)*(S-DisCD)*(S-DisGD))
#print("El area del triangulo 2 en cuadrante 4= ");print(AreaTri)

Angulo = math.degrees(math.acos( ((DisGD*DisGD ) - ( (DisGC*DisGC) + (DisCD*DisCD) ))/( -2 *DisGC*DisCD ) ))
#print("Angulo");print(Angulo)
Area4 = ((Angulo/360)*AreaCir) - AreaTri
print("El area de la figura 4 es = "); print(Area4);print()

#Leer un punto dado
V = True
while V == True: 
        Xp = input(" Defina el punto X  "); Xp = float(Xp)
        Yp = input(" Defina el punto Y  "); Yp = float(Yp)
        print()
        
        if(Xp<=7.5 and Xp >=-7.5 and Yp <= 7.5 and Yp >=-7.5):
                if(Xp >0 and Yp >0):
                        print("El punto esta en la region 5");V = False
                elif(Xp <0 and Yp >0):
                        print("El punto esta en la region 5");V = False
                elif(Xp <0 and Yp <0):
                        print("El punto esta en la region 5");V = False
                elif(Xp >=0 and Yp <=0):
                        print("El punto esta en el cuadrante 4")
                        #Calculo sobre el circulo
                        RadioComp = math.sqrt((Xp*Xp)+(Yp*Yp)) 
                        #Calculo de recta GD
                        mGD = (PuntoDx-PuntoGx)/(PuntoDy-PuntoGy)
                        bGD = PuntoDy - mGD*PuntoDx
                        CompbGD = Yp - (mGD*Xp)
                        #Calculo de recta GF
                        mGF = (PuntoFx-PuntoGx)/(PuntoFy-PuntoGy)
                        bGF = PuntoFy - mGF*PuntoFx
                        CompbGF = Yp - (mGF*Xp)
                        
                        #Calculo de recta DF
                        mDF = (PuntoFx-PuntoDx)/(PuntoFy-PuntoDy)
                        bDF = PuntoFy - mDF*PuntoFx
                        CompbDF = Yp - (mAD*Xp)
                        #print(CompbDF); print(IntersectoY)
                        
                        if((RadioComp == RadioCir) or (Xp == 0 or Yp ==0) or (CompbGD == bGD) or (CompbGF == bGF) or (CompbDF == IntersectoY)):
                                print("El punto esta en la frontera");V = False
                        elif(RadioComp > RadioCir):
                                print("El punto esta en la región 5");V = False
                        elif((CompbGD < bGD) and (RadioComp < RadioCir) and (CompbGF < bGF)):        
                                print("El punto esta en la región 4");V = False
                        elif(CompbGF > bGF):
                                print("El punto esta en la región 1");V = False
                        elif(CompbDF < IntersectoY):
                                print(" El punto esta en la región 3");V = False
                        else:
                                print(" El punto esta en la region 2");V = False
                
        else:
                print(" El númmero se sale del evaluador necesario ")
                V = True

print();print()        
print(  " *** Ejecución finalizada *** ")