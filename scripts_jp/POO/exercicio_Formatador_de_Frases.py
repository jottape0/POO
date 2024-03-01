"""
Requisitos: 

    Crie uma classe chamada FormatadorDeFrase que será responsável por todas as operações de formatação.

1: A classe deve possuir os seguintes métodos: 

-> para_maiusculas(): converte toda a frase para maiusculas.
-> para_minusculas(): converte toda a frase para minusculas.
-> capitalizar(): capitaliza a primeira letra da frase.
-> formato_titulo(): converte a primeira letra de cada palavra da frase para maiuscula.
-> contar_vogais(): conta e retorna o numero de vogais na frase.
-> contar_consoantes(): conta e retorna o numero de consoantes na frase.
-> tamanho_frase(): conta e retorna o tamanho da respectiva frase
-> contar_letra(): conta e retorna o numero de ocorrencias da respectiva letra na frase.
-> procurar_palavra(): conta e retorna o numero de ocorrencias de uma palavra especifica na frase.
-> obter_frase(): retorna a frase atual.

2: Implemente uma função menu que serve como interface do usuário. Essa função deve mostrar um menu com as opções 
de formatação e realizar a operação escolhida pelo usuário.

3: O programa deve continuar rodando e mostrando o menu até que o usuário escolha sair.

Detalhes: 
    O programa deve ser case-insensitive para contagem e pesquisa de palavras. Você pode assumir que o usuário entrará 
apenas com caracteres alfabeticos e espaços.
"""

class FormatadorDeFrase: 
    """definindo a classe FormatadorDeFrases"""

    def __init__(self, frase):
        
        self.frase = frase

    def para_maiusculas(self):
        """método para formatar a frase completa em letras maiúsculas"""

        self.frase = self.frase.upper()

    def para_minusculas(self):
        """método para formatar a frase completa em letras minúsculas"""

        self.frase = self.frase.lower()

    def capitalizar(self):
        """método para deixar a primeira letra da frase maiúscula"""

        self.frase = self.frase.capitalize()

    def formato_titulo(self):
        """método para converter a frase para o formato de título"""

        self.frase = self.frase.title()

    def contar_vogais(self):
        """método para contar o número de vogais na frase"""

        vogais = 'aeiouáéíóúàèìòùãõâêîôû'

        contagem = 0

        frase_minuscula = self.frase.lower()

        for letra in frase_minuscula:

            if letra in vogais:

                contagem += 1

        return contagem
    
    def contar_consoantes(self):
        """método para contar o número de consoantes na frase"""

        consoantes = 'bcdfghjklmnopqrstvwxyzç'

        contagem = 0

        frase_minuscula = self.frase.lower()

        for letra in frase_minuscula:

            if letra in consoantes:

                contagem += 1
        
        return contagem
    
    def tamanho_frase(self):
        """método para contar o tamanho da palavra ou frase"""

        frase_sem_espacos = ''.join(self.frase.split())

        tamanho = len(frase_sem_espacos)

        return tamanho

    def contar_letra(self, letra):
        """método para contar a ocorrência de uma letra em uma frase"""

        return self.frase.lower().count(letra.lower()) # usa o método count() para contar o número de ocorrência de uma letra em uma frase
    
    def procurar_palavra(self, palavra):
        """método para procurar e contar o número de ocorrências de uma palavra específica na frase"""

        return self.frase.lower().count(palavra.lower()) # usa o método count() para contar o número de ocorrência da palavra

    def obter_frase(self):
        """método para retornar a frase atual"""

        return self.frase


def menu():
    """definindo a função menu, que será a interface do usuário para o programa"""

    print('\nBem vindo ao formatador de frase!')

    frase = input('Por favor, digite uma frase: ')

    formatador = FormatadorDeFrase(frase)
    """cria um objeto 'formatador' da classe FormatadorDeFrase, passando a frase digitada como argumento"""

    while True:

        """
        para_maiusculas(): converte toda a frase para maiusculas.
        para_minusculas(): converte toda a frase para minusculas.
        capitalizar(): capitaliza a primeira letra da frase.
        formato_titulo(): converte a primeira letra de cada palavra da frase para maiuscula.
        contar_vogais(): conta e retorna o numero de vogais na frase.
        contar_consoantes(): conta e retorna o numero de consoantes na frase.
        contar_letra(): conta e retorna o numero de ocorrencias da respectiva letra na frase.
        procurar_palavra(): conta e retorna o numero de ocorrencias de uma palavra especifica na frase.
        obter_frase(): retorna a frase atual.
        """
        print(f'\nA frase escolhida foi: {frase}')
        print('\nEscolha uma opção para formatar a sua frase: ')
        print('1. Converter para maiúsculas')
        print('2. Converter para minúsculas')
        print('3. Capitaliza a primeira letra da frase')
        print('4. Converter para o formato de título')
        print('5. Contar vogais')
        print('6. Contar consoantes')
        print('7. Contar o tamanho da frase')
        print('8. Contar letras')
        print('9. Pesquisar palavra')
        print('10. Mostar frase atual')
        print('11. Sair')

        escolha = input('\nDigite o número da sua escolha: ')

        if escolha == '1':

            formatador.para_maiusculas()

        elif escolha == '2':

            formatador.para_minusculas()

        elif escolha == '3':
            
            formatador.capitalizar()

        elif escolha == '4':

            formatador.formato_titulo()

        elif escolha == '5':

            print(f'Total de vogais: {formatador.contar_vogais()}')

        elif escolha == '6':

            print(f'Total de consoantes: {formatador.contar_consoantes()}')

        elif escolha == '7':

            print(f'A frase possui: {formatador.tamanho_frase()} caracteres')

        elif escolha == '8':

            letra_escolhida = input(f'Qual letra você deseja saber o número de ocorrências da frase "{frase}": ')

            print(f"O total de ocorrências da letra {letra_escolhida} é: {formatador.contar_letra(letra_escolhida)}")

        elif escolha == '9':

            palavra = input('Digite a palavra que você quer pesquisar: ')

            contagem = formatador.procurar_palavra(palavra)

            if contagem > 0:

                print(f'A palavra "{palavra}" aparece {contagem} vez(es) na frase "{frase}"')

            else:

                print(f'A palavra "{palavra}" não foi encontrada na frase/texto.')

        elif escolha == '10':

            print(f'\nFrase atual: {formatador.obter_frase()}')
            continue

        elif escolha == '11':

            print('Saindo do programa. Até mais!!')

            break
            
        print('Frase atual: ', formatador.obter_frase())



if __name__ == '__main__':
    """verifica se o script está sendo executado como programa principal e, nesse caso, chama a função menu"""
    menu()



        

    