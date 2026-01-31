def valida_senha(senha):
    temMaisQue8Caracteres = False
    temCaracterMaiusculo = False
    temCaracterEspecial = False

    if len(senha) > 7:
        temMaisQue8Caracteres = True
        print("passou aqui 1")

    for caracter in senha:

        if ord(caracter) > 64 or ord(caracter) < 91:
            temCaracterMaiusculo = True
            print("passou aqui 2")

        if ord(caracter) > 32 or ord(caracter) < 47:
            temCaracterEspecial = True
            print("passou aqui 3")

    return temMaisQue8Caracteres and temCaracterMaiusculo and temCaracterEspecial


