class Carro:

    def __init__(self, marca, modelo, cor) -> None:
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0 # inicializa o atributo velocidade atual do carro com 0

    def acelerar(self):
        """método que aumenta a velocidade do carro em 10km/h"""

        self.velocidade += 10
        """incrementa a velocidade atual em 10km/h"""

        print(f'Velocidade atual: {self.velocidade}km/h')
        """exibe a velocidade atual do carro"""

    def frear(self):
        """método que diminui a velocidade do carro em 10km/h"""
        
        self.velocidade -= 10
        """decrementa a velocidade atual em 10km/h"""

        if self.velocidade < 0:
            self.velocidade = 0
        """garante que a velocidade não se torne negativa"""

        print(f'Velocidade atual: {self.velocidade}km/h')
        """exibe a velocidade atual do carro"""

    def exibir_info(self):
        """método que exibe as informações básicas do carro"""

        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.cor}')
        """exibe a marca, modelo e a cor do carro"""

carro1 = Carro('Toyota', 'Corolla', 'Branco')
"""instanciando objetos da classe Carro"""

carro1.exibir_info()
carro1.acelerar()
carro1.frear()


carro2 = Carro('Ford', 'Fiesta', 'Azul')
"""instanciando objetos da classe Carro"""

print('\n----------------------------------------\n') 

carro2.exibir_info()
carro2.acelerar()
carro2.frear()


print('\n**********************************************************\n')

# Exemplo pedindo informações ao usuário

class Carro:

    def __init__(self, marca, modelo, cor) -> None:
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0 # inicializa o atributo velocidade atual do carro com 0

    def acelerar(self):
        """método que aumenta a velocidade do carro em 10km/h"""

        self.velocidade += 10
        """incrementa a velocidade atual em 10km/h"""

        print(f'Velocidade atual: {self.velocidade}km/h')
        """exibe a velocidade atual do carro"""

    def frear(self):
        """método que diminui a velocidade do carro em 10km/h"""
        
        self.velocidade -= 10
        """decrementa a velocidade atual em 10km/h"""

        if self.velocidade < 0:
            self.velocidade = 0
        """garante que a velocidade não se torne negativa"""

        print(f'Velocidade atual: {self.velocidade}km/h')
        """exibe a velocidade atual do carro"""

    def exibir_info(self):
        """método que exibe as informações básicas do carro"""

        print(f'Marca: {self.marca}, Modelo: {self.modelo}, Cor: {self.cor}, Velocidade: {self.velocidade}km/h')
        """exibe a marca, modelo e a cor do carro"""


lista_carros = []

while True:

    print('\n----Menu----')
    print('1-> Adicionar novo carro')
    print('2-> Exibir informações dos carros')
    print('3-> Acelerar um carro')
    print('4-> Frear um carro')
    print('5-> Sair')

    escolha = input('Escolha uma opção: ')

    if escolha == '1':

        marca = input('Digite a marca do carro: ')
        modelo = input('Digite o modelo do carro: ')
        cor = input('Digite a cor do carro: ')

        novo_carro = Carro(marca, modelo, cor)
        lista_carros.append(novo_carro)

    elif escolha == '2':

        if lista_carros:
            for carro in lista_carros:
                carro.exibir_info()
        else:
            print('Nenhum carro adicionado na lista.')
    
    elif escolha == '3':

        modelo = input('Digite o modelo do carro que você deseja acelerar: ')

        for carro in lista_carros:
            if carro.modelo == modelo:
                carro.acelerar()
                break

            else:
                print('Modelo não encontrado.')

    elif escolha == '4':

        modelo = input('Digite o modelo do carro que você deseja frear: ')

        for carro in lista_carros:
            if carro.modelo == modelo:
                carro.frear()
                break
    
    elif escolha == '5':

        print('Programa encerrado')

        break

    else:

        print('Opção inválida. Tente novamente!')
    