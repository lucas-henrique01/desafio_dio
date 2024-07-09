print("***********************************************************")
print("\nSeja bem vindo ao Lucbank, onde seu dinheiro rende mais!!!\n")
print("***********************************************************")

Menu = """

[1] Depositar
[2] Sacar 
[3] Extrato
[4] Sair

=> """

saldo = 0 
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(Menu)

    if opcao == "1":
        valor =  float(input("Digite o valor para ser depositado: "))
        print("\nValor depositado com sucesso! Obrigado por usar nossos serviços!\nLucbank com voce sempre!!! ")

        if valor > 0 :
            saldo =+ valor
            extrato += f"deposito: R$ {valor:.2f}\n"
            

        else:
            print("Essa operacao está invalida! O valor informado esta incorreto.")
    
    elif opcao == "2":
        valor = float(input("Digite o valor desejado para saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite 
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("\n***Atençao***\nOperação falhou! Voce nao tem saldo saldo suficiente.")
        
        elif excedeu_limite:
            print("\n***Atençao***\nOperação falhou! O valor de saque exede o limite.")

        elif excedeu_saques: 
            print("\n***Atençao***\nOperação falhou! Número maximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1 

        else:
            print("Operação falhou! O valor informado é invalido.")

    elif opcao == "3": 
        print("\n********** EXTRATO **********")
        print("Nao foram realizado movimentaçoes." if not extrato else extrato)
        print(f"\nSeu saldo: R$ {saldo:.2f}")
        print("*******************************")

    elif opcao == "4":
        break
    else:
        print("Operacao invalida! Por favor selecione novamente a operação desejada.")

  

  
        