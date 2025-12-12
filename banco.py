# SISTEMA BANCÁRIO SIMPLES EM PYTHON (PROCEDURAL)

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

print("=== SISTEMA BANCÁRIO ===")

while True:
    print("""
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair
""")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        valor = float(input("Valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado!")
        else:
            print("Valor inválido.")

    elif opcao == "2":
        valor = float(input("Valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente.")
        elif excedeu_limite:
            print("Valor maior que o limite de R$ 500.")
        elif excedeu_saques:
            print("Número de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Saque realizado!")
        else:
            print("Valor inválido.")

    elif opcao == "3":
        print("\n===== EXTRATO =====")
        print("Não houve movimentações." if not extrato else extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("===================\n")

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida.")

