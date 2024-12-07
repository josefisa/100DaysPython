from random import randint
magico = [[int() for j in range (11)] for i in range(11)]
fils =[int() for j in range (11)]; cols = [int() for j in range (11)]
dsec =[int() for j in range (1)]; dpal = [int() for j in range (1)]
n = randint(3,10)
if n%2==0:
        n =n+1
i=0;j= int(n/2);k=1
magico[i][j] =k
for k in range(2,n*n+1):
    i -=1; j+=1
    if i<0:
        i = n-1
    if j>n-1:
        j=0
    if magico[i][j] ==0:
        magico[i][j] =k
    else:
        i+=1;j-=1
        if i>n-1:
            i=0
        if j<0:
            j = n-1
        i +=1; magico[i][j] =k
print(" ")
for i in range(n):
    for j in range(n):
        print(" %3d"%magico[i][j], end=" ")
    print(" ")
for i in range(n):
    for j in range(n):
        fils[i] += magico[i][j]; cols[j] += magico[i][j]
        if i==j: 
            dpal[0] += magico[i][j]
        if i+j==n+1:
            dsec[0] += magico[i][j]
print(fils,"\n", cols)
sumas=fils+cols+dpal+dsec
print(sumas)

            
        