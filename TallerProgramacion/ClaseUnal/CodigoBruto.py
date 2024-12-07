import random
n= random.randint(5,8)
m= random.randint(5,8)
ncaballos= n-1
VectorFil=[ -1, -2, -2, -1, +1, +2, +2, +1];VectorCol=[+2, +1, -1, -2, -2, -1, +1, +2]
while m==n:
    m =random.randint(5,8)
print(n);print(m)
cuadrado=[[int(0)for i in range(0,n)]for j in range (0,m)]
nc1 = []; mc1=[]
nc1.append(random.randint(0,m-1))
mc1.append(random.randint(0,n-1))
print(nc1);print(mc1)
cuadrado[nc1[0]][mc1[0]]= 1
j = 0
#for i in VectorFil:
    #j=i
    #if (((n-1)+i)>0 or ((n-1)+i)<=(n-1)) and (((m-1)+VectorCol[j])>0    or ((m-1)+VectorCol[j])<=(m-1)):
            #cuadrado[nc1+i][mc1+VectorCol[j]] = 2

for i in range (1,ncaballos+1):
    nc1.append(random.randint(0,m-1))   
    mc1.append(random.randint(0,n-1))
                
for i in range(0,n):
    for j in range(0,m):
        print("%3d"%cuadrado[j][i],sep=" ",end="" )
    print("")