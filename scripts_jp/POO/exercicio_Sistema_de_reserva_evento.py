"""
Exercicio: Sistema de Reservas para um Evento

Objetivo: Compreender a definição e utilização de métodos dentro de classes em Python.

Descrição:

Crie uma classe chamada Evento que represente um evento com um número limitado de lugares. A classe deve permitir:
    1 -> Reservar um lugar 
    2 -> Cancelar uma reserva

A classe Evento deve ter os seguintes métodos:
    - reservar(): este método deve diminuir o número de lugares disponíveis em um.
    - cancelar(): este método deve aumentar o número de lugares disponíveis em um.
    - lugares_disponiveis(): este método deve retornar o número de lugares disponíveis. 

Restrições:
    1 -> O evento tem uma capacidade inicial definida (por exempo, 10 lugares).

    2 -> Se tentar reserva um lugar e todos estiverem ocupados, o sistema deve informar que não há lugares disponíveis.

    3 -> Se tentar cancelar uma reserva e todos os lugares estiverem disponíveis, o sistema deve informar que não há
reservas para cancelar
"""

class Evento:

    def __init__(self, capacidade=10):
        

        self.capacidade = capacidade

        self.lugares_disponiveis = capacidade 

    def reservar(self):
        """método para reservar um lugar no evento"""

        if self.lugares_disponiveis == 0:

            print('Desculpe, não há lugares disponíveis para reservar.')

            return 
        
        self.lugares_disponiveis -= 1

        print('Lugar reservado com sucesso')

    def cancelar(self):
        """método que é usado para cancelar a reserva existente"""

        if self.lugares_disponiveis == self.capacidade:

            print('Não há reservas para cancelar.')

            return
        
        self.lugares_disponiveis += 1

        print('Reserva cancelada com sucesso')

    def mostrar_lugares_disponiveis(self):
        """método para mostrar o numero de lugares disponíveis"""

        return f'Lugares disponíveis: {self.lugares_disponiveis}'


# testando a classe
evento = Evento()

print(evento.mostrar_lugares_disponiveis()) # 10 lugares
      
for _ in range(3): # usando o loop for para reservar 3 lugares de uma só vez
    """O _ é um identificador (basicamente uma variável) usado para armazenar o valor de cada item. 
    É uma convenção que indica 'eu não me importo com o valor atual, estou apenas usando o loop para repetição'."""

    evento.reservar()

print(evento.mostrar_lugares_disponiveis()) # 7 lugares 