"""
Exercicio Pet

Instruções do exercício

1 -> Crie uma classe chamada Pet.

2 -> A classe deve ter os seguintes atributos privados: _nome, _idade e _peso.

- utilize métodos 'getters' para cada um desses atributos
- utilize métodos 'setters' para cada um desses atributos

Os setters devem conter as seguintes validações:

- O nome deve ser uma string e não pode ser vazio.
- A idade deve ser um numero inteiro e deve ser maior ou igual a 0.
- O peso deve ser um numero flutuante e deve ser maior que 0

3 -> Adicione um método exibir_info() que mostre as informações do pet. 

Exemplo do código base

class Pet:

    # complete o código aqui
"""

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


# teste de implementação

meu_pet = Pet()

meu_pet.set_nome('Buddy')
meu_pet.set_idade(2)
meu_pet.set_peso(6.5)
meu_pet.exibir_info()