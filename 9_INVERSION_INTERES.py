inversion=float(input("Introduce la cantidad de euros a invertir: "))
interes=float(input("Introduce el interés, ej. 0.4%: "))
anyos=int(input("Introduce el número de años: "))

calculo= inversion*pow((1+(interes/100), anyos))
print("Tu beneficio es de ", calculo, "euros.")