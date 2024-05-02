edad = int(input("Edad:"))
lugar = input("lugar:")
nombre = input("nombre:")

lista = [edad,lugar,nombre]

for i, element in enumerate(lista):
    if i == 0:
        if lista[i] <18:
            print("(menor de edad) "+str(lista[0]))
    else:         
       print(element)

print(str(len(lista)-1))