sexo = input("Digite o sexo (M/F): ").strip().upper()

while sexo != "M" and sexo != "F":
    print("Sexo inválido. Tente novamente.")
    sexo = input("Digite o sexo (M/F): ").strip().upper()

    if sexo == "M":
        print("Homem")
    elif sexo == "F":
        print("Mulher")