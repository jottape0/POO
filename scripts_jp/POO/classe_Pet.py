class Pet:

    def __init__(self):
        
        self._nome = "" 
        self._idade = 0 
        self._peso = 0.0

    def get_nome(self):
        """método get para o nome. Permite obter o valor do atributo _nome"""

        return self._nome
    
    def set_nome(self, novo_nome):
        """método set para alterar o nome. Permite definir um novo valor para o atributo _nome"""

        if isinstance(novo_nome, str) and novo_nome != "": # O nome deve ser uma string e não pode ser vazio

            self._nome = novo_nome

        else:

            print('Nome inválido.')

    def get_idade(self):
        """método get para a idade. Permite obter o valor do atributo _idade"""

        return self._idade
    
    def set_idade(self, nova_idade): 
        """método set para a idade. Permite definir um novo valor para o atributo _idade"""

        if isinstance(nova_idade, int) and nova_idade >= 0: # A idade deve ser um numero inteiro e deve ser maior ou igual a 0.

            self._idade = nova_idade 

        else:

            print('Idade inválida.')

    def get_peso(self):
        """método get para o peso. Permite obter o valor do atributo _peso"""

        return self._peso
    
    def set_peso(self, novo_peso):
        """método set para o peso. Permite definir um novo valor do atributo _peso"""

        if isinstance(novo_peso, float) and novo_peso > 0:

            self._peso = novo_peso

        else:

            print('Peso inválido.')

    def exibir_info(self):

        print(f'Nome: {self._nome}\nIdade: {self._idade} ano(s)\nPeso: {self._peso} kg')

def mostrar_menu():
    """função para mostrar o menu de opções"""

    print('\n----Menu de Gerenciamento de Pet----')
    print('1. Definir o nome do Pet')
    print('2. Definir a idade do Pet')
    print('3. Definir o peso do Pet')
    print('4. Exibir informações do Pet')
    print('5. Sair')

    escolha = input('Escolha uma opção: ')

    return escolha

def main():
    """função principal que coordena a execução do programa"""

    meu_pet = Pet()

    while True:

        escolha = mostrar_menu()

        if escolha == '1':

            nome = input('Digite o novo nome do pet: ')

            meu_pet.set_nome(nome)

        elif escolha == '2':

            try:

                idade = int(input('Digite a nova idade do pet: '))

                meu_pet.set_idade(idade)

            except ValueError:

                print('Idade inválida. Por favor, insira um número inteiro.')

        elif escolha == '3':

            try:

                peso = float(input('Digite o novo peso do pet: '))

                meu_pet.set_peso(peso)

            except ValueError:

                print('Peso inválido. Por favor, insira um número.')

        elif escolha == '4':

            meu_pet.exibir_info()

        elif escolha == '5':

            print('Programa encerrado. Até mais!')

            break
        
        else:

            print('Opção inválida. Tente novamente.')

main()
