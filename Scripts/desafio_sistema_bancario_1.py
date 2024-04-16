menu = """
        SANO BANKING
____________________________

====    [1] Depositar   ====
====    [2] Sacar       ====    
====    [3] Extrato     ====
====    [0] Sair        ====
____________________________

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        print("O caixa aceita apenas notas, com o valor de R$10 a R$1000") #Novas infos.
        print("Máximo de 50 cédulas!") #Novas infos.
        valor = float(input("Informe o valor para depósito: ")) #Novas infos.

        if valor >= 10 and valor <= 1000: #Alterei colocando um limite!
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

            print(f"Saldo atual de: R$ {saldo:.2f}") #Coloquei esta opção para que após o depósito, seja exibido o saldo atual da conta.
            
        else:
            print("Valor inválido, operação cancelada.")#Novas infos.
            #Havia inserido aqui o menu2, porém não deu muito certo. E só agora na hora de postar notei que poderia ter deixado ele aqui.
            #Para que alguém pudesse ver e quem sabe me ajudar KK.

    elif opcao == "2":
        print("Valor mínimo para saque é de R$10") #Inseri um limite para saque mínimo.
        valor = float(input("Informe o valor para saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente.")#Novas infos.
            
        elif excedeu_limite:
            print("O valor do saque excede o saldo.")#Novas infos.
            
        elif excedeu_saques:
            print("Número máximo de saques diário excedido, volte amanhã!")#Novas infos.
            
        elif valor > 10: #Teste do valor para saque que agora é de 10 e não mais 0.
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("O valor informado é inválido.")#Novas infos.

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "0":
        print("SANO BANKING agradece a sua CONFIANÇA!")#Novas infos.
        break

    else:
        print("Por favor, selecione um opção válida.")#Novas infos.