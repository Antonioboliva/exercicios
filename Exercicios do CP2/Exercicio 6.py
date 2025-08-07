import math
while True:
    numero = float (input("Digite um numero decimal: "))
    if numero.is_integer():
        print("Numero inteiro")
    else:
        break

raiz_quadrada = math.sqrt(numero)
teto = math.ceil(numero)
chao = math.floor(numero)
parte_inteira= int(numero)

print("Raiz quadrada: {:.2f}".format(raiz_quadrada))
print("Teto: {:.2f}".format(teto))
print("Chao: {:.2f}".format(chao))
print("Parte inteira: {:.2f}".format(parte_inteira))