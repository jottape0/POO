# Caixa eletronico simples 

saldo = 0

while True:
    """imprime as opções do menu para o usuário"""
    print("\nCaixa Eletrônico")
    print("1: Verificar Saldo: ")
    print("2: Depositar dinheiro: ")
    print("3: Sacar dinheiro: ")
    print("4: Sair: ")

    """permite que o usuário escolha entre as opções disponíveis"""
    opcao = input("Escolha uma opção (1-4): ")

    """verifica a opção escolhida e a executa"""
    if opcao == "1":

        print(f"Seu saldo é: R$ {saldo:.2f}")
    
    elif opcao == "2":

        deposito = float(input("Digite o valor do depósito: R$ "))

        if deposito > 0: # Verifica se o valor do depósito é positivo
            """saldo = saldo + deposito"""
            saldo += deposito # Adiciona o valor do depósito ao saldo
            print(f"Depósito de R$ {deposito:.2f} realizado com sucesso!") # confirma o depósito
        else:
            print("Valor do depósito inválido!") # informa que o valor do depósito é inválido. 

    elif opcao == "3":

            saque = float(input("Digite o valor do saque: R$ "))
            """verifica se o saque é um valor positivo e se o saque é maior do que o saldo"""
            if saque > 0 and saque <= saldo:
                 
                 """subtrai o valor do saque do saldo"""
                 saldo -= saque 
             
                 print(f"Saque de R$ {saque:.2f} realizado com sucesso!")
            
            else:
                 
                 print("Valor do saque inválido ou saldo insuficiente.")
    
    elif opcao == "4":
         
         print("Obrigado por utilizar o caixa eletrônico. Até mais!!")

         break # Encerra o programa 
    
    else:
         print("Opção inválida. Tente novamente!") # Se o usuário digitar alguma opção inválida, o programa reinicia

