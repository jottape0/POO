# calculadora simples 

while True:

    print("Calculadora simples: ")

    print("1: Adição: ")
    print("2: Subtração: ")
    print("3: Multiplicação: ")
    print("4: Divisão: ")
    print("5: Sair: ")

    opcao = input("\nDigite a sua opção (1-4): ")

    num1 = float(input("\nDigite o primeiro numero: "))
    num2 = float(input("\nDigite o segundo numero: "))
   
    if opcao == "1":
        print(num1 + num2)
    
    elif opcao == "2":
        print(num1 - num2)
    
    elif opcao == "3":
        print(num1 * num2)
    
    elif opcao == "4":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Não é possível realizar uma divisão por zero.")
            continue
    
    elif opcao == "5":
        print("Obrigado por utilizar a calculadora. Até mais!!")
        break

    else:
        print("Opção inválida. Tente novamente!")
    

