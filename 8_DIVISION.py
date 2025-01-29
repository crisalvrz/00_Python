try:
    n1=int(input("Introduce el primer número entero: "))
    n2=int(input("Introduce el segundo número entero: "))
    
    if n2==0:
        print("El resultado es 0")
    else:
        x=n1//n2
        y=n1%n2
    print("La división resultante de dividir ",n1, "entre ", n2, "da un cociente ", x, "y un resto ", y)

except ValueError:
    print("Error, introduce únicamente números.")