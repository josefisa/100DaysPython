
Limite = 50000; SumaIzq =0; SumaDer = 0

for n in range (1,Limite):
    SumaIzq = SumaIzq + (1/n)

print(f'El resultado es: \n {SumaIzq}\n')

for n in range(Limite,1):
    SumaDer =SumaDer + (1/n)
    
print(f'El otro resultado es: \n {SumaIzq}\n')