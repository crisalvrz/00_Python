atras = int(input("Contemos hacia atrás, dame un número entero: "))
if atras > 0:
    while atras > 0:
        print(atras, ",", end=" ")
        atras-=1
else:
    print("No es un número válido, prueba de nuevo.")