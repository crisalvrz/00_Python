lista1=[]

while len(lista1) < 6:
  n = int(input("introduce un numero entre 1 y 999: "))
  if n > 0 and n < 999:
    lista1.append(n)

  else:
    print("Este nuemero no es valido")
    continue
print(lista1)

for i in range(0,len(lista1),1):
    for j in range (i+1,len(lista1),1):
        if lista1[i]>lista1[j]:
            #los intercambio
            aux=lista1[j]
            lista1[j]=lista1[i]
            lista1[i]=aux
print(lista1)