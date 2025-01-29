numero= input("Introduce un número para convertir a binario: ")
binario= numero
if numero >= 0:
    return bin(numero).replace("0b", "")
else:
    return "-" + bin(abs(numero)).replace("0b", "")