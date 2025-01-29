# CALCULADORA DE ÍNDICE DE MASA CORPORAL
estatura =float(input("Escriba su estatura en metros: "))
peso =float(input("Escriba su peso: "))
imc=round((peso/(estatura*estatura)),2)

print("Tu índice de masa corporal es: ", imc)
