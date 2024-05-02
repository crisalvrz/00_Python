#máquina par/impar
i = int(input("Introduce un número:")) #Int engloba input

j = 0
while j <= i:

    if j % 2 == 0:
        print(str(j)+" es par") #str es para convertir nº a texto
    else:
        print(str(j)+" es impar")
    j+=1 #j es iterador; el += es para llegar al nº i