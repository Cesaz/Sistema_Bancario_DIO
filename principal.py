menu = """ 

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor_escolhido = float(input("DIGITE O VALOR DO DEPOSITO: "))

        if valor_escolhido > 0:
            saldo += valor_escolhido
            extrato += f"Depósito: R$ {valor_escolhido:.2f}\n"

        else:
            print("O valor informado é inválido. Tente Novamente")


    elif opcao == "2":
        valor_escolhido = float(input("QUANTO GOSTARIA DE SACAR?: "))
        saldo_insuficiente = valor_escolhido > saldo
        limite_insuficiente = valor_escolhido > limite
        saque_insuficiente = numero_saque >= LIMITE_SAQUES

        if saldo_insuficiente:
            print("NÃO FOI POSSÍVEL REALIZAR O SAQUE! SALDO INSUFICIENTE.")

        elif limite_insuficiente:
            print("NÃO FOI POSSIVEL REALIZAR O SAQUE! LIMITE ACIMA DO PERMITIDO.")

        elif saque_insuficiente:
            print("NÃO FOI POSSÍVEL REALIZAR O SAQUE! QUANTIDADE MAXIMA DE SAQUES UTILIZADAS.")

        elif valor_escolhido > 0:
            saldo -= valor_escolhido
            extrato += f"Saque: R$ {valor_escolhido:.2f}\n"
            numero_saque += 1

        else:
            print("ALGO DEU ERRADO! TENTE NOVAMENTE.")

    elif opcao == "3":
        print("EXTRATO")

    elif opcao == "4":
        break

    else:
        print("OPERAÇÃO INVALIDA, SELECIONE NOVAMENTE A OPÇÃO DESEJADA.")
