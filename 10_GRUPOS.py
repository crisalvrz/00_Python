#Los alumnos se dividen en grupos A y B de acuerdo a sexo y nombre; el a tiene mujeres con nombre anterior a la M y hombres posterior a N
#El b or el resto. Escribe un programa que pregunte el nombre y sexo y muestre por pantalla a que grupo pertenece.
nombre = input("Introduce tu nombre: ")
sexo = input("Introduce la letra que corresponde a tu género (F/M): ").strip().upper()
primera_letra = nombre[0].upper()

if (sexo == "F" and primera_letra < "M") or (sexo == "M" and primera_letra > "N"):
    print("Perteneces al grupo A.")
else:
    print("Perteneces al grupo B.")