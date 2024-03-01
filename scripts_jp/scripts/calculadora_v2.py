def nome(nome: str) -> str:
    """Função que retorna o nome do usuário"""
    return f'Bem-vindo, {nome.title()}'

def escolher():
    """Função que o usuário escolhe para realizar a operação"""
    return 'Escolha uma opção. Sendo: \n a: adição.\n s: subtração.\n m: multiplicação.\n d: divisão.\n e: exponenciacao.\n p: porcentagem.\n historico: visualizar histórico de operações.\n'

def soma(a: float, b: float) -> float:
    """Função que realiza a soma dos números informados."""
    resultado = a + b
    historico_operacoes.append(f'{a} + {b} = {resultado}')
    return resultado

def subtracao(a: float, b: float) -> float:
    """Função que realiza a subtração dos números informados."""
    resultado = a - b
    historico_operacoes.append(f'{a} - {b} = {resultado}')
    return resultado

def multiplicacao(a: float, b: float) -> float:
    """Função que realiza a multiplicação dos números informados."""
    resultado = a * b
    historico_operacoes.append(f'{a} * {b} = {resultado}')
    return resultado

def divisao(a: float, b: float) -> float:
    """Função que realiza a divisão dos números informados."""
    if b != 0:
        resultado = a / b
        historico_operacoes.append(f'{a} / {b} = {resultado}')
        return resultado
    else:
        raise ZeroDivisionError('Não é possível dividir por zero.')

def exponenciacao(a: float, b: float) -> float:
    resultado = a ** b
    historico_operacoes.append(f'{a} ** {b} = {resultado}')
    return resultado

def porcentagem(a: float, b: float, c: int) -> float:
    resultado = (a / b) * 100
    historico_operacoes.append(f'{a} % de {b} = {resultado}')
    return resultado

def exibir_historico():
    print("\nHistórico de Operações:")
    for operacao in historico_operacoes:
        print(operacao)

# Inicialização do histórico
historico_operacoes = []

nome_usuario = input('Digite seu nome: ')
print(nome(nome_usuario))

while True:
    print(escolher())
    opcao_usuario = input('Digite a opção desejada (a, s, m, d, e, p) ou digite "sair" para encerrar o programa: ')

    if opcao_usuario == 'historico':
        exibir_historico()
        continue  # Reinicia o loop sem executar o código abaixo

    if opcao_usuario in ('a', 's', 'm', 'd', 'e', 'p'):
        try:
            num1 = float(input('Digite o primeiro número: '))
            num2 = float(input('Digite o segundo número: '))

            if opcao_usuario == 'a':
                print('O resultado da sua soma é: ')
                print(soma(num1, num2))
            elif opcao_usuario == 's':
                print('O resultado da sua subtração é: ')
                print(subtracao(num1, num2))
            elif opcao_usuario == 'm':
                print('O resultado da sua multiplicação é: ')
                print(multiplicacao(num1, num2))
            elif opcao_usuario == 'd':
                print('O resultado da sua divisão é: ')
                print(divisao(num1, num2))
            elif opcao_usuario == 'e':
                print('O resultado da sua exponenciação é: ')
                print(exponenciacao(num1, num2))
            elif opcao_usuario == 'p':
                print('O resultado da sua porcentagem é: ')
                print(round(porcentagem(num1, num2, 100), 2))
        except ValueError:
            print('Por favor, digite números válidos.')
    else:
        print(f'Obrigado por utilizar o programa, {nome_usuario.title()}')
        break
