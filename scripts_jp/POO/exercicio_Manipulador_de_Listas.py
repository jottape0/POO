"""
Exercicio Manipulador de Listas

Objetivo: Criar uma aplicação que ajuda os usuários a manipular listas de numeros inteiros. A aplicação deve oferecer 
opções para adicionar elementos, remover elementos, encontrar o maior e o menor elemento, calcular a média dos elementos
e mais. 

Requisitos: 

1 -> Crie uma classe chamada ManipuladorDeLista que será responsável por todas as operações de manipulação de Lista:

- adicionar_elemento(elemento): adiciona um elemento no final da lista. 

- remover_elemento(elemento): remove a primeira ocorrência do elemento na lista

- encontrar_maior(): encontra e retorna o maior elemento da lista.

- encontrar_menor(): encontra e retorna o menor elemento da lista

- organizar_lista(): coloca a lista em ordem do menor para o maior ou vice-versa

- calcular_media(): calcula e retorna a media dos elementos na lista

- mostrar_lista(): retorna a lista atual

2 -> Implemente uma função menu() que serve como interface do usuário. Essa função deve mostrar um menu com as opções
de manipulação e realizar a operação escolhida pelo usuário. 

3 -> O programa deve continuar rodando e mostrando o menu até que o usuário escolha sair.
"""


class ManipuladorDeLista: 

    def __init__(self):
        
        self.lista = []

    def adicionar_elemento(self, elemento):
        """método para adicionar elemento na lista"""

        self.lista.append(elemento)

    def remover_elemento(self, elemento):
        """método para remover a primeira ocorrência da lista"""

        try:

            self.lista.remove(elemento)
            
            print(f'O elemento {elemento} foi removido da lista.')

        except ValueError:

            print(f'O elemento {elemento} não foi encontrado na lista.')

    def encontrar_maior(self):

        if self.lista:

            return max(self.lista)
        
        else:

            return 'A lista está vazia.'
        
    def encontrar_menor(self):
        """método para encontrar o menor elemento da lista"""

        if self.lista:

            return min(self.lista)
        
        else:

            return 'A lista está vazia.'

    def organizar_lista_crescente(self):
        """método para organizar a lista de forma crescente"""

        if self.lista: 

            self.lista.sort()

            return self.lista

        else:
            return 'A lista está vazia'
        
    def organizar_lista_decrescente(self):
        """método para organizar a lista de forma decrescente"""

        if self.lista:

            self.lista.sort(reverse=True)

            return self.lista
        
        else:

            return 'A lista está vazia'
   
    def calcular_media(self):
        """método para calcular a média da lista"""

        if self.lista:

            return sum(self.lista) / len(self.lista) 

    def mostrar_lista(self):
        """método para retornar a lista atual"""

        return self.lista

def menu():
    """função para criar um menu interativo até que o usuário deseje sair"""

    manipulador = ManipuladorDeLista()

    while True:

        print('\nEscolha a opção desejada: ')
        print('1. Adicionar elemento')
        print('2. Remover elemento')
        print('3. Encontrar maior elemento')
        print('4. Encontrar menor elemento')
        print('5. Ordenar a lista de forma crescente')
        print('6. Ordenar a lista de forma decrescente')
        print('7. Calcular média')
        print('8. Mostrar lista')
        print('9. Sair')

        escolha = input('\nDigite o número da sua escolha: ')

        if escolha == '1':

            try:
                elemento = int(input('Digite o elemento que deseja adicionar na lista: '))

                manipulador.adicionar_elemento(elemento)

            except ValueError:

                print('Entrada inválida. Por favor, insira um número inteiro.')

        elif escolha == '2':
            try:

                elemento = int(input('Digite o elemento que deseja remover da lista: '))

                manipulador.remover_elemento(elemento)

            except ValueError:

                print('Entrada inválida. Por favor, insira um número inteiro.')

        elif escolha == '3':

            print(f'O maior elemento da lista é: {manipulador.encontrar_maior()}')

        elif escolha == '4':

            print(f'O menor elemento da lista é: {manipulador.encontrar_menor()}')

        elif escolha == '5':

            lista_crescente = manipulador.organizar_lista_crescente()
    
            print(f'A lista {manipulador.mostrar_lista()} foi ordenada de forma crescente.')
            print(f'A lista atual é: {lista_crescente}')

        elif escolha == '6':

            lista_decrescente = manipulador.organizar_lista_decrescente()

            print(f'A lista {manipulador.mostrar_lista()} foi ordenada de forma decrescente.')
            print(f'A lista ordenada é: {lista_decrescente}')

        elif escolha == '7':

            print(f'A média dos elementos da lista é: {manipulador.calcular_media()}')

        elif escolha == '8':

            print(f'A lista atual é: {manipulador.mostrar_lista()}')

        elif escolha == '9':

            print('Programa encerrado. Até mais!!')

            break

        else:

            print('Escolha inválida. Tente novamente!')


if __name__ == '__main__':

    menu()    