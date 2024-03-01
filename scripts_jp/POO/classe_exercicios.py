class Jogador:
    
    def __init__(self, nome, posicao, numero_camisa, gols=0):
        
        self.nome = nome 
        self.posicao = posicao 
        self.numero_camisa = numero_camisa
        self.gols = gols

jogador1 = Jogador('Hulk', 'Atacante', 7)

jogador2 = Jogador('Paulinho', 'Atacante', 10)

# print(f'{jogador1.nome} é um {jogador1.posicao} e usa a camisa n° {jogador1.numero_camisa}')

# print(f'{jogador2.nome} é um {jogador2.posicao} e usa a camisa n° {jogador2.numero_camisa}')

jogador1.gols += 2

# print(f'{jogador1.nome} marcou {jogador1.gols} gols')


"""
Exercicio - Informações de Frutas em uma mercearia 

Em uma mercearia, várias frutas são vendidas, e você deseja criar um sistema simples para gerenciar 
as informações sobre essas frutas.

Objetivos: 

1 -> Definir uma classe chamada Fruta.
2 -> Instanciar um ou mais objetos desta classe
3 -> Acessar e exibir os atributos dos objetos instanciados.
"""

class Frutas: 

    def __init__(self, nome, preco_por_kg, quantidade_em_estoque):

        self.nome = nome 
        self.preco_por_kg = preco_por_kg
        self.quantidade_em_estoque = quantidade_em_estoque

    def exibir_info(self):

        print(f'Nome da fruta: {self.nome}')
        print(f'Preco por kg: R$ {self.preco_por_kg}')
        print(f'Quantidade em estoque: {self.quantidade_em_estoque} unidades')

banana = Frutas('Banana', 10.50, 45)
maca = Frutas('Maçã', 9.90, 30)


banana.exibir_info()
print('--------------------------------')
maca.exibir_info()