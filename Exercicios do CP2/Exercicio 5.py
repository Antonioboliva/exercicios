num = int(input("Digite um numero entre 1000 a 9999: "))
while num < 1000 or num > 9999:
    print("Entrada invalida")
    num = int(input("Digite um numero: "))

if 1000 <= num <= 9999:
    unidade = num % 10
    dezena = (num // 10) % 10
    centena = (num // 100) % 10
    milha = num // 1000

    print("Unidade: {}".format(unidade))
    print("Dezena: {}".format(dezena))
    print("Centena: {}".format(centena))
    print("Milha: {}".format(milha))
    