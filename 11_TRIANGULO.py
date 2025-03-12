altura = int(input("Introduce un número entre 1 y 200. Este será el alto del triángulo: "))
if 1 <= altura <= 200:
    for i in range(1, altura + 1):
        print("*" * i)
else:
    print("Número no válido. Debe estar entre 1 y 200.")